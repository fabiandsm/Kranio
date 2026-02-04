# executive_summary.py
executive_summary = {
    'titulo': 'Implementación de Pipeline ETL para Analytics E-commerce',
    
    'resumen_ejecutivo': """
Se ha implementado un pipeline ETL moderno que transforma datos crudos de e-commerce 
en insights accionables, mejorando la toma de decisiones comerciales.
""",
    
    'problema': """
- Reportes manuales tomaban 3 días
- Datos inconsistentes entre sistemas
- Falta de insights en tiempo real
- Costos operativos elevados por procesos manuales
""",
    
    'solucion': """
Pipeline ETL automatizado con:
- Extracción desde 5+ fuentes de datos
- Procesamiento en tiempo real
- Data warehouse dimensional optimizado
- Dashboards self-service para negocio
""",
    
    'beneficios': {
        'eficiencia': 'Reducción de 3 días a 4 horas en reportes',
        'calidad': '99.5% de datos validados automáticamente',
        'escalabilidad': 'Soporte para 10x crecimiento de datos',
        'roi': 'Retorno de inversión en 8 meses'
    },
    
    'metricas_clave': {
        'volumen_procesado': '500GB/día',
        'tiempo_respuesta': '< 30 minutos',
        'disponibilidad': '99.9%',
        'usuarios_activos': '150+ analistas'
    },
    
    'riesgos_mitigados': [
        'Monitoreo 24/7 con alertas automáticas',
        'Backups diarios con recuperación en < 4 horas',
        'Arquitectura tolerante a fallos',
        'Procesos de testing automatizados'
    ],
    
    'roadmap': {
        'fase_1_completada': 'Pipeline core operativo',
        'fase_2_actual': 'ML y advanced analytics',
        'fase_3_planificada': 'Real-time personalization'
    },
    
    'recomendaciones': [
        'Expandir uso a más equipos de negocio',
        'Implementar ML para predicción de demanda',
        'Integrar con sistemas CRM existentes',
        'Capacitar a 50+ usuarios adicionales'
    ]
}

def generar_presentacion_ejecutiva(summary):
    """Generar slides de presentación ejecutiva"""
    
    slides = [
        {
            'titulo': summary['titulo'],
            'contenido': summary['resumen_ejecutivo'],
            'tipo': 'titulo'
        },
        {
            'titulo': 'El Problema',
            'contenido': summary['problema'],
            'tipo': 'problema',
            'visual': 'before_after_diagram'
        },
        {
            'titulo': 'La Solución',
            'contenido': summary['solucion'],
            'tipo': 'solucion',
            'visual': 'architecture_diagram'
        },
        {
            'titulo': 'Beneficios Clave',
            'contenido': summary['beneficios'],
            'tipo': 'beneficios',
            'visual': 'metrics_dashboard'
        },
        {
            'titulo': 'Métricas de Éxito',
            'contenido': summary['metricas_clave'],
            'tipo': 'metricas',
            'visual': 'kpi_cards'
        },
        {
            'titulo': 'Riesgos y Mitigaciones',
            'contenido': summary['riesgos_mitigados'],
            'tipo': 'riesgos',
            'visual': 'risk_matrix'
        },
        {
            'titulo': 'Roadmap Futuro',
            'contenido': summary['roadmap'],
            'tipo': 'roadmap',
            'visual': 'timeline'
        },
        {
            'titulo': 'Recomendaciones',
            'contenido': summary['recomendaciones'],
            'tipo': 'recomendaciones',
            'visual': 'action_items'
        }
    ]
    
    return slides