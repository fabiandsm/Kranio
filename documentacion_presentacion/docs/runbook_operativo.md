# 🛠 Runbook Operativo del Pipeline

Este documento describe procedimientos operativos para mantener el pipeline funcionando correctamente.

---

## Inicio Diario

Checklist operativo:

- Verificar conectividad de fuentes de datos
- Validar espacio en disco (>20% libre)
- Confirmar estado de servicios críticos
- Ejecutar pipeline manual si falla ejecución automática

---

## Monitoreo

El pipeline se monitorea mediante:

- Dashboard Grafana con métricas en tiempo real
- Alertas automáticas mediante PagerDuty
- Logs centralizados en stack ELK

---

## Recuperación de Desastres

Procedimientos disponibles:

- Backups diarios del Data Warehouse
- Reprocesamiento histórico disponible
- Failover automático entre regiones

---

Este proceso asegura continuidad del servicio ante incidentes operativos.
