# Validador de Datos de Ventas

## Propósito
Este componente valida la calidad básica de los datos de ventas antes de ser procesados
en un pipeline ETL o sistema de analítica.

Su objetivo es detectar errores tempranos y prevenir fallos posteriores en el pipeline.

---

## Parámetros
- **datos** (`list[dict]`):  
  Lista de diccionarios que representan registros de ventas.

Ejemplo de estructura esperada:
```python
{
  "precio": float,
  "fecha": str
}
