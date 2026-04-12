autos = [
    {"marca": "Mazda", "modelo": "Demio", "año": 2008, "color": "Rojo"},
    {"marca": "Toyota", "modelo": "Yaris", "año": 2015, "color": "Azul"},
    {"marca": "Suzuki", "modelo": "Swift", "año": 2012, "color": "Rojo"},
    {"marca": "Mazda", "modelo": "3", "año": 2020, "color": "Negro"}
]
opcion = input("Ingresa una marca: ").capitalize()
encontrado = False

print("-"*15, " FILTRO DE AUTOS ", "-"*15)
for filtro in autos:
    if  filtro["marca"] == opcion:
       encontrado = True
       if filtro["año"] < 2010:
           print(f"- Marca: {filtro["marca"]} | Modelo: {filtro["modelo"]} | Color: {filtro["color"]} | Año: {filtro["año"]} (Requiere revision tecnica.)")
       else:
           print(f"- Marca: {filtro["marca"]} | Modelo: {filtro["modelo"]} | Color: {filtro["color"]} | Año: {filtro["año"]}")
if not encontrado:
    print("No tenemos vehiculos de esa marca actualmente.")
    
    