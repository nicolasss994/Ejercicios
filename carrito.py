precios = {
    "pan": 1000, 
    "leche": 1200, 
    "queso": 3500, 
    "jamon": 2800,
    "yogur": 600
}

carrito = []
total = 0

while True:
    print()
    print("Pan: 1000")
    print("Leche: 1200")
    print("Queso: 3500")
    print("Jamon: 2800")
    print("Yorgut: 600")
    print()
    opcion = input("Que producto desear agregar al carrito? Escribe 'pagar' para pagar: ").lower()
    print()
    
    if opcion == "pagar":
        if not carrito:
            print("Actualmente no tienes nada en tu carrito.")
        else:
            print("TOTAL DE LAS COMPRAS")
            for i in carrito:
                valor = precios[i]
                total += valor
                print(f"- {i}: {valor}")
            print()
            print(f"Has pagado exitosamente: {total}")
            break
    else:
        if opcion not in precios:
            print("No tenemos ese producot.")
        else:
            carrito.append(opcion)
            print(f"El producto '{opcion} se ha agregado a tu carrito exitosamente.")
        
            