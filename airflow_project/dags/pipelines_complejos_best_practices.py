from airflow import DAG
from airflow.decorators import task, branch
from airflow.utils.dates import days_ago

with DAG(
    dag_id="pipeline_avanzado_complejo",
    start_date=days_ago(1),
    schedule=None,
    catchup=False,
    tags=["windows", "taskflow"],
) as dag:

    @task
    def inicio():
        return "ok"

    @task
    def validar_calidad():
        return True

    @branch
    def decidir_ruta(validacion):
        if validacion:
            return "ruta_ok"
        return "ruta_error"

    @task
    def ruta_ok():
        return "success"

    @task
    def ruta_error():
        return "fail"

    i = inicio()
    v = validar_calidad()
    d = decidir_ruta(v)

    i >> v >> d
    d >> [ruta_ok(), ruta_error()]
