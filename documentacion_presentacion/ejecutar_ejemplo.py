from src.validador_datos_ventas import validar_datos_ventas

datos_ventas = [
    {'precio': 100, 'fecha': '2024-01-01'},
    {'precio': -50, 'fecha': '2024-01-02'}
]

resultado = validar_datos_ventas(datos_ventas)

print(resultado)
