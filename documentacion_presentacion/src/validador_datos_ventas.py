def validar_datos_ventas(datos):
    """
    Valida que los datos de ventas cumplan criterios básicos de calidad.
    """
    errores = []

    for i, fila in enumerate(datos):
        if fila.get('precio', 0) <= 0:
            errores.append(f"Fila {i}: precio inválido")
        if not fila.get('fecha'):
            errores.append(f"Fila {i}: fecha faltante")

    return {
        'valido': len(errores) == 0,
        'errores': errores,
        'total_filas': len(datos)
    }
