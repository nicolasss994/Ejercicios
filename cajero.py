saldo = 50000
historial = []

while True:
    print()
    print("-"*7 + " CAJERO AUTOMATICO " + "-"*7)
    print("1. Ver saldo")
    print("2. Retirar dinero")
    print("3. Ver historial")
    print("4. Salir")
    print()
    decision = input("Inserta una opcion: ")
    print("\n")
    
    match decision:
        case "1":
            print(f"Actualmente tienes {saldo}")
        case "2":
            cantidad = int(input("Cuanto dinero quieres retirar?: "))
            if cantidad > saldo:
                print("No tienes esa cantidad de dinero.")
            else:
                saldo -= cantidad
                historial.append(f"Retiro de {cantidad}")
                print(f"Has retirado exitosamente {cantidad}, te queda {saldo} de saldo")
        case "3":
            print("-"*7 + " HISTORIAL DE RETIROS " + "-"*7)
            for retiro in historial:
                print(f"- {retiro}")
        case "4":
            print("Saliendo....")
            break
        case _:
            print("Opcion invalida")