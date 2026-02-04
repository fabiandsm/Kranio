# 🧠 Decisiones Arquitectónicas del Pipeline

## Escalabilidad

El sistema fue diseñado para soportar crecimiento de datos y usuarios.

### Escalabilidad Horizontal
- Uso de múltiples workers de Airflow
- Paralelización de tareas ETL

### Escalabilidad Vertical
- Ajuste de recursos por componente según carga

### Auto-scaling
- Recursos asignados dinámicamente según volumen de procesamiento

---

## Fiabilidad

Se implementan mecanismos para asegurar continuidad operativa.

- Reintentos automáticos configurados según tipo de error
- Circuit breakers para dependencias externas
- Backups diarios con retención de 30 días

---

## Mantenibilidad

El sistema está diseñado para facilitar mantenimiento y evolución.

- Arquitectura modular por componentes
- Configuración externa mediante variables de entorno
- Logging estructurado para debugging y monitoreo
