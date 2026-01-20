# Apache Airflow – Primer DAG Funcional

Este repositorio contiene la implementación de un **DAG funcional en Apache Airflow**, desarrollado como ejercicio introductorio para comprender la creación, ejecución y monitoreo de workflows basados en **grafos dirigidos acíclicos (DAGs)**.

El proyecto fue desplegado utilizando **Apache Airflow 2.9.3 sobre Docker en Windows**, siguiendo buenas prácticas de configuración y diagnóstico.

---

## 📌 Objetivo del ejercicio

- Instalar y configurar Apache Airflow.
- Crear un DAG simple con múltiples tareas.
- Definir dependencias entre tareas (workflow).
- Ejecutar y monitorear el DAG desde la interfaz web.
- Verificar logs de ejecución.

---

## 🛠️ Tecnologías utilizadas

- **Python 3.12**
- **Apache Airflow 2.9.3**
- **Docker & Docker Compose**
- **PostgreSQL 15**
- **Windows 11**

---

## 📁 Estructura del proyecto

```
airflow_docker/
├── dags/
│   └── saludo_diario.py
├── docker-compose.yml
└── README.md
```

---

## 🚀 Descripción del DAG

### DAG: `saludo_diario`

- **Schedule**: `@daily`
- **Catchup**: deshabilitado
- **Tareas**:
  1. `tarea_bash`: ejecuta un comando Bash.
  2. `tarea_python`: ejecuta una función Python.
  3. `tarea_esperar`: simula procesamiento con un `sleep`.

### Flujo de ejecución

```
tarea_bash → tarea_python → tarea_esperar
```

---

## 🧩 Código del DAG

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def saludar():
    print("¡Hola desde Airflow!")
    return "Saludo completado"

with DAG(
    dag_id="saludo_diario",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["ejemplo", "saludo"],
) as dag:

    tarea_bash = BashOperator(
        task_id="tarea_bash",
        bash_command='echo "Ejecutando tarea bash"'
    )

    tarea_python = PythonOperator(
        task_id="tarea_python",
        python_callable=saludar
    )

    tarea_esperar = BashOperator(
        task_id="tarea_esperar",
        bash_command="sleep 5"
    )

    tarea_bash >> tarea_python >> tarea_esperar
```

---

## ▶️ Ejecución del proyecto

1. Levantar los servicios:
   ```bash
   docker compose up -d
   ```

2. Acceder a la interfaz web:
   ```
   http://localhost:8080
   ```

3. Activar el DAG `saludo_diario`.

4. Ejecutar manualmente con **Trigger DAG**.

5. Revisar los logs de la tarea `tarea_python` para verificar la salida:
   ```
   ¡Hola desde Airflow!
   ```

---

## ✅ Resultados

- DAG cargado correctamente sin errores.
- Ejecución exitosa de todas las tareas.
- Validación del uso de grafos y workflows.
- Correcto uso de Airflow en entorno Docker.

---

## 🧠 Conclusiones

Este ejercicio permite comprender los conceptos fundamentales de Apache Airflow, incluyendo la definición de DAGs, el uso de operadores, la gestión de dependencias y la ejecución de workflows en un entorno productivo.

---

## 📌 Autor

**Fabián Díaz**  
Proyecto de aprendizaje en Ciencia de Datos / Data Engineering.
