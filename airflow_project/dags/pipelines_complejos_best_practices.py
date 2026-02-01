from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta
import random


def validar_calidad_datos(**context):
    calidad = random.choice(["alta", "media", "baja"])
    context["ti"].xcom_push(key="calidad", value=calidad)
    return calidad


def decidir_procesamiento(**context):
    calidad = context["ti"].xcom_pull(
        task_ids="validar_calidad", key="calidad"
    )

    if calidad == "alta":
        return "procesamiento_rapido"
    else:
        return "procesamiento_completo"


def procesamiento_rapido():
    return "Procesado rápido"


def procesamiento_completo():
    return "Procesado completo"


with DAG(
    dag_id="pipeline_avanzado_complejo",
    description="Pipeline con patrones avanzados y best practices",
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=5),
        "execution_timeout": timedelta(hours=1),
    },
) as dag:

    inicio = EmptyOperator(task_id="inicio")

    validar = PythonOperator(
        task_id="validar_calidad",
        python_callable=validar_calidad_datos,
    )

    decidir = BranchPythonOperator(
        task_id="decidir_ruta",
        python_callable=decidir_procesamiento,
    )

    ruta_rapida = PythonOperator(
        task_id="procesamiento_rapido",
        python_callable=procesamiento_rapido,
    )

    ruta_completa = PythonOperator(
        task_id="procesamiento_completo",
        python_callable=procesamiento_completo,
    )

    with TaskGroup("procesamiento_pesado") as procesamiento_group:
        paso1 = EmptyOperator(task_id="paso1")
        paso2 = EmptyOperator(task_id="paso2")
        paso3 = EmptyOperator(task_id="paso3")

        paso1 >> paso2 >> paso3

    union = EmptyOperator(task_id="union_rutas")
    fin = EmptyOperator(task_id="fin")

    inicio >> validar >> decidir
    decidir >> [ruta_rapida, ruta_completa, procesamiento_group]
    [ruta_rapida, ruta_completa, procesamiento_group] >> union >> fin
