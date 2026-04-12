ventas = [
    {"prod": "pan", "monto": 1000}, 
    {"prod": "leche", "monto": 1200}, 
    {"prod": "pan", "monto": 1000},
    {"prod": "queso", "monto": 3500},
    {"prod": "pan", "monto": 1000}
]

total_dinero = 0
contador_pan = 0

for producto in ventas:
    total_dinero += producto['monto']
    if producto['prod'] == "pan":
        contador_pan += 1
print(f"Se vendieron {contador_pan} con un total de {total_dinero}")