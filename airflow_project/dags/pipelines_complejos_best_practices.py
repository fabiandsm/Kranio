from airflow import DAG
from airflow.decorators import task
from airflow.utils.task_group import TaskGroup
from airflow.utils.trigger_rule import TriggerRule
from airflow.utils.dates import days_ago
import random
import logging

logger = logging.getLogger(__name__)

with DAG(
    dag_id="pipeline_avanzado_complejo",
    start_date=days_ago(1),
    schedule=None,
    catchup=False,
    tags=["best_practices", "branching", "taskflow"],
) as dag:

    @task
    def inicio():
        logger.info("Inicio del pipeline")
        return "inicio_ok"

    @task
    def validar_calidad():
        calidad = random.choice(["alta", "media", "baja"])
        logger.info(f"Calidad detectada: {calidad}")
        return calidad

    @task.branch
    def decidir_ruta(calidad):
        if calidad == "alta":
            return "procesamiento.procesamiento_rapido"
        elif calidad == "media":
            return "procesamiento.procesamiento_completo"
        else:
            return "procesamiento.procesamiento_pesado"

    with TaskGroup("procesamiento") as procesamiento:

        @task
        def procesamiento_rapido():
            logger.info("Procesamiento rápido")
            return "rapido_ok"

        @task
        def procesamiento_completo():
            logger.info("Procesamiento completo")
            return "completo_ok"

        @task
        def procesamiento_pesado():
            logger.info("Procesamiento pesado")
            return "pesado_ok"

        procesamiento_rapido()
        procesamiento_completo()
        procesamiento_pesado()

    @task(trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS)
    def fin():
        logger.info("Fin del pipeline")

    inicio_task = inicio()
    calidad = validar_calidad()
    ruta = decidir_ruta(calidad)

    inicio_task >> calidad >> ruta >> procesamiento >> fin()
