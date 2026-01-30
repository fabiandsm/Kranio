from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime, timedelta
import random
import logging

logger = logging.getLogger(__name__)

# =========================
# Funciones
# =========================

def validar_calidad_datos(ti):
    calidad = random.choice(["alta", "media", "baja"])
    logger.info(f"Calidad detectada: {calidad}")
    ti.xcom_push(key="calidad", value=calidad)
    return calidad

def decidir_procesamiento(ti):
    calidad = ti.xcom_pull(task_ids="validar_calidad", key="calidad")

    if calidad == "alta":
        return "procesamiento_rapido"
    elif calidad == "media":
        return "procesamiento_completo"
    else:
        return "procesamiento_pesado.paso1"

def procesamiento_rapido():
    logger.info("Procesamiento rápido")

def procesamiento_completo():
    logger.info("Procesamiento completo")

def paso(nombre):
    logger.info(f"Ejecutando {nombre}")

# =========================
# DAG
# =========================

default_args = {
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "execution_timeout": timedelta(hours=1)
}

with DAG(
    dag_id="pipelines_complejos_best_practices",
    description="Pipeline avanzado con Branching y TaskGroup",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
    tags=["avanzado", "branching", "taskgroup"]
) as dag:

    inicio = EmptyOperator(task_id="inicio")

    validar = PythonOperator(
        task_id="validar_calidad",
        python_callable=validar_calidad_datos
    )

    decidir = BranchPythonOperator(
        task_id="decidir_ruta",
        python_callable=decidir_procesamiento
    )

    ruta_rapida = PythonOperator(
        task_id="procesamiento_rapido",
        python_callable=procesamiento_rapido
    )

    ruta_completa = PythonOperator(
        task_id="procesamiento_completo",
        python_callable=procesamiento_completo
    )

    # ✅ TaskGroup correctamente dentro del DAG
    with TaskGroup(group_id="procesamiento_pesado") as procesamiento_pesado:
        paso1 = PythonOperator(
            task_id="paso1",
            python_callable=paso,
            op_args=["paso1"]
        )

        paso2 = PythonOperator(
            task_id="paso2",
            python_callable=paso,
            op_args=["paso2"]
        )

        paso3 = PythonOperator(
            task_id="paso3",
            python_callable=paso,
            op_args=["paso3"]
        )

        paso1 >> paso2 >> paso3

    union = EmptyOperator(
        task_id="union_rutas",
        trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS
    )

    fin = EmptyOperator(task_id="fin")

    # =========================
    # Dependencias
    # =========================

    inicio >> validar >> decidir
    decidir >> [ruta_rapida, ruta_completa, procesamiento_pesado]
    [ruta_rapida, ruta_completa, procesamiento_pesado] >> union >> fin
