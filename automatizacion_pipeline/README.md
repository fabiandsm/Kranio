# Apache Airflow – DAGs Funcionales y Automatización de Pipelines

Este repositorio contiene la implementación de **DAGs funcionales en Apache Airflow**, desarrollados como ejercicios prácticos para comprender la creación, ejecución y monitoreo de workflows basados en **grafos dirigidos acíclicos (DAGs)**.

El proyecto fue desplegado utilizando **Apache Airflow 2.9.3 sobre Docker en Windows**, siguiendo buenas prácticas de configuración, diagnóstico y orquestación de pipelines.

---

## 📌 Objetivo del ejercicio

- Instalar y configurar Apache Airflow.
- Crear DAGs con múltiples tareas.
- Definir dependencias simples y complejas entre tareas.
- Ejecutar y monitorear DAGs desde la interfaz web.
- Verificar logs de ejecución.
- Comprender el uso de operadores básicos de Airflow.

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
│   ├── saludo_diario.py
│   ├── dependencias_complejas.py
│   ├── operadores_sensores.py
│   ├── operadores_sensores.png
│   └── README.md
└── docker-compose.yml
```

---

## 🚀 DAG 1: Saludo Diario

### Descripción

DAG introductorio que permite validar la correcta instalación y funcionamiento de Apache Airflow.

- **DAG ID**: `saludo_diario`
- **Schedule**: `@daily`
- **Catchup**: deshabilitado

### Flujo de ejecución

```
tarea_bash → tarea_python → tarea_esperar
```

### Resultado esperado

- Ejecución secuencial de las tareas.
- Visualización correcta del flujo en Graph View.
- Logs accesibles desde la interfaz web.

---

## 🧩 DAG 2: Pipeline de Ventas con Dependencias Complejas

Como parte del ejercicio de automatización, se implementó un DAG que modela un **pipeline ETL de ventas**, incorporando ejecución paralela y sincronización explícita entre tareas.

- **DAG ID**: `pipeline_ventas_complejo`
- **Schedule**: `@daily`
- **Catchup**: deshabilitado

---

### 1️⃣ Visualización del grafo de dependencias

El DAG fue visualizado utilizando **Graph View** en la interfaz web de Apache Airflow, permitiendo verificar visualmente el flujo de ejecución y las dependencias entre tareas.

**Flujo verificado:**

```
preparar_entorno → [extraer_api_ventas, extraer_db_productos]
extraer_api_ventas → validar_datos_api → transformar_ventas ↘
extraer_db_productos → validar_datos_db → transformar_productos ↘
                                   join_ventas_productos
                                             ↓
                                    cargar_data_warehouse
                                             ↓
                                   enviar_reporte_ejecucion
```

El grafo confirma ejecución paralela en las etapas de extracción y validación, seguida de una sincronización explícita en la etapa de *join* antes de la carga final.

---

### 2️⃣ Pruebas de ejecución del DAG

Para validar el correcto funcionamiento del pipeline se realizaron los siguientes escenarios:

**Prueba del DAG sin scheduler:**
```bash
airflow dags test pipeline_ventas_complejo 2024-01-01
```

**Ejecución manual del DAG:**
```bash
airflow dags trigger pipeline_ventas_complejo
```

**Revisión de logs de la tarea final:**
```bash
airflow tasks logs pipeline_ventas_complejo enviar_reporte_ejecucion 2024-01-01
```

Los logs confirman que el pipeline se ejecuta correctamente hasta la generación del reporte final.

---

### 3️⃣ Verificación conceptual

**a) Elección entre PythonOperator y BashOperator**

El `PythonOperator` se utiliza cuando la tarea requiere lógica de negocio, procesamiento de datos o validaciones mediante código Python.  
El `BashOperator` es más adecuado para ejecutar comandos del sistema operativo o tareas simples de preparación del entorno, como la creación de directorios o ejecución de scripts shell.

**b) Ventajas de definir dependencias explícitas**

Definir dependencias explícitas permite ejecutar tareas en paralelo, representar claramente el flujo mediante un grafo acíclico, evitar ejecuciones incorrectas y facilitar el monitoreo, debugging y mantenimiento del pipeline.

---

## ✅ Resultados

- DAGs cargados correctamente sin errores.
- Ejecuciones exitosas de todas las tareas.
- Dependencias simples y complejas correctamente definidas.
- Visualización y monitoreo desde Airflow Web UI.
- Logs accesibles para validación de ejecución.

---

## 🧠 Conclusiones

El desarrollo de estos DAGs permitió consolidar los conceptos fundamentales de Apache Airflow, incluyendo la definición de workflows, uso de operadores, paralelismo, dependencias complejas y monitoreo de ejecuciones en un entorno Docker.

---
## 📂 DAG 3: Pipeline con Sensores y Operador Personalizado

Este DAG incorpora **sensores y operadores personalizados**, simulando un escenario real de ingesta de datos dependiente de eventos externos.

- **DAG ID**: `pipeline_con_sensores_y_operador_custom`
- **Schedule**: `@hourly` (ejecutado manualmente durante pruebas)
- **Catchup**: deshabilitado

### Flujo del DAG
```
esperar_archivo_datos
        ↓
validar_datos_ventas
        ↓
procesar_datos_ventas
        ↓
generar_reporte
        ↓
limpiar_archivos
```

---

## 🧠 Verificación conceptual

**¿Cuándo usar sensores?**  
Se utilizan sensores cuando la ejecución de un pipeline depende de una condición externa, como la llegada de archivos o la disponibilidad de datos.

**¿Ventajas de operadores personalizados?**  
Permiten encapsular lógica de negocio específica, mejorar la reutilización de código y mantener DAGs más limpios.
## 📌 Autor

**Fabián Díaz**  
Proyecto de aprendizaje en Ciencia de Datos / Data Engineering.
