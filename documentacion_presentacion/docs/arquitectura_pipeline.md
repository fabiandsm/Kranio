# 🏗 Arquitectura del Pipeline ETL

## Visión General

El pipeline ETL procesa datos de e-commerce para generar insights de negocio utilizados por dashboards y reportes analíticos.

El flujo transforma datos crudos provenientes de múltiples fuentes en información confiable y estructurada para análisis.

---

## Componentes Principales

### 1. Extracción (Extract)

**Propósito:** Obtener datos desde múltiples fuentes externas.

**Tecnologías utilizadas:**
- SQLAlchemy
- Requests
- PyArrow

**Fuentes de datos:**
- API REST de plataforma e-commerce
- Base de datos transaccional PostgreSQL
- Archivos CSV de proveedores externos

**Características:**
- Extracción incremental para optimizar rendimiento
- Reintentos automáticos ante fallos
- Validación básica de integridad de datos

---

### 2. Transformación (Transform)

**Propósito:** Limpiar, validar y enriquecer datos antes de su almacenamiento.

**Operaciones principales:**
- Limpieza de valores faltantes y outliers
- Normalización de formatos
- Cálculo de métricas derivadas (ventas, margen, etc.)
- Validación de reglas de negocio

---

### 3. Carga (Load)

**Propósito:** Almacenar datos procesados para su consumo analítico.

**Destinos:**
- Data Warehouse en PostgreSQL con modelo dimensional
- Data Lake en almacenamiento S3 particionado
- Cache Redis para dashboards de alta velocidad

---

## Flujo de Datos

API E-commerce → Validación → Limpieza → Enriquecimiento → DW
↓ ↓ ↓ ↓ ↓
PostgreSQL DB → Normalización → Reglas → Agregaciones → S3