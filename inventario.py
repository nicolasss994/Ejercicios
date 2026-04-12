productos = {
    "aceite": 2500,
    "arroz": 1500,
    "leche": 1200
}

while True:
    print("\n" + "-"*15)
    print("1. Ver inventario")
    print("2. Cambiar producto")
    print("3. Salir del menú")
    print("-"*15)
    
    opcion = input("Elige una opción: ")
    
    match opcion:
        case "1":
            print("\n--- INVENTARIO ACTUAL ---")
            for producto, precio in productos.items():
                print(f"• {producto.capitalize()}: ${precio}")
        
        case "2":
            nombre_viejo = input("Que producto quieres actualizar?: ").lower()
            
            if nombre_viejo in productos:
                nuevo_nombre = input("Nuevo nombre para el producto?: ").lower()
                nuevo_precio = int(input("Nuevo precio?: "))
                
                if nombre_viejo != nuevo_nombre:
                    del productos[nombre_viejo]
                
                productos[nuevo_nombre] = nuevo_precio
                print(f"\nActualizado: {nuevo_nombre} a ${nuevo_precio}")
            else:
                print(f"\nEl producto '{nombre_viejo}' no existe en el inventario.")
                
        case "3":
            print("Saliendo del sistema...")
            break
            
        case _:
            print("⚠️ Opción inválida, intenta de nuevo.")