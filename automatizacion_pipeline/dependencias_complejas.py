from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

def extraer_ventas():
    """Simular extracción de datos de ventas"""
    print("Extrayendo datos de ventas...")
    return {"registros": 1000}

def validar_datos():
    """Validar calidad de datos"""
    print("Validando 1000 registros...")
    return {"validos": 950, "errores": 50}

def transformar_datos():
    """Aplicar transformaciones de negocio"""
    print("Transformando 950 registros válidos...")
    return {"transformados": 950}

def cargar_data_warehouse():
    """Cargar a data warehouse"""
    print("Cargando 920 registros...")
    return {"cargados": 920}

def enviar_reporte_final():
    """Enviar reporte de ejecución"""
    print("Pipeline completado: 920 registros procesados")

# Configurar DAG
dag = DAG(
    'pipeline_ventas_complejo',
    description='Pipeline ETL de ventas con dependencias complejas',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    default_args={
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
    }
)

# Tareas de extracción
extraer_api = PythonOperator(
    task_id='extraer_api_ventas',
    python_callable=extraer_ventas,
    dag=dag
)

extraer_db = PythonOperator(
    task_id='extraer_db_productos',
    python_callable=lambda: {"productos": 500},
    dag=dag
)

# Tarea de preparación
preparar_entorno = BashOperator(
    task_id='preparar_entorno',
    bash_command='mkdir -p /tmp/etl_ventas',
    dag=dag
)

# Validaciones
validar_api = PythonOperator(
    task_id='validar_datos_api',
    python_callable=validar_datos,
    dag=dag
)

validar_db = PythonOperator(
    task_id='validar_datos_db',
    python_callable=lambda: {"productos_validos": 480},
    dag=dag
)

# Transformaciones
transformar_ventas = PythonOperator(
    task_id='transformar_ventas',
    python_callable=transformar_datos,
    dag=dag
)

transformar_productos = PythonOperator(
    task_id='transformar_productos',
    python_callable=lambda: {"productos_transformados": 480},
    dag=dag
)

# Join
join_datos = PythonOperator(
    task_id='join_ventas_productos',
    python_callable=lambda: {"registros_completos": 920},
    dag=dag
)

# Carga
cargar_dw = PythonOperator(
    task_id='cargar_data_warehouse',
    python_callable=cargar_data_warehouse,
    dag=dag
)

# Reporte
reporte = PythonOperator(
    task_id='enviar_reporte_ejecucion',
    python_callable=enviar_reporte_final,
    dag=dag
)

# Dependencias
preparar_entorno >> [extraer_api, extraer_db]
extraer_api >> validar_api >> transformar_ventas
extraer_db >> validar_db >> transformar_productos
[transformar_ventas, transformar_productos] >> join_datos
join_datos >> cargar_dw >> reporte
