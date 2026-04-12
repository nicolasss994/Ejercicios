repuestos = {"aceite": 25000, "bujias": 12000, "pastillas": 35000, "filtro": 8000}
presupuesto = int(input("Cual es tu presupuesto maximo?: "))
alcanzables = []

for repuesto, precio in repuestos.items():
    if precio <= presupuesto:
        alcanzables.append(repuesto)
if not alcanzables:
    print("No te alcanza para nada.")
else:
    print("Te alcanzan los siguientes repuestos:")
    for repuesto in alcanzables:
        print(f"- {repuesto}")
        