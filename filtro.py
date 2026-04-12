usuarios = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Iquique"},
    {"nombre": "Juan", "edad": 17, "ciudad": "Santiago"},
    {"nombre": "Marta", "edad": 30, "ciudad": "Iquique"},
    {"nombre": "Edu", "edad": 18, "ciudad": "Iquique"}
]
encontrado = False
opcion = input("Dime el nombre de la ciudad: ").capitalize()

for usuario in usuarios:
    if usuario["ciudad"] == opcion and usuario["edad"] >= 18:
        print(f"Encontramos a {usuario['nombre']}, que tiene {usuario['edad']} años y vive en {usuario['ciudad']}")
        encontrado = True
if not encontrado:
    print("No se encontraron persoans")
