while True:
    patente_ingresada = input("Ingresa una patente valida: ").upper()

    if len(patente_ingresada) > 6:
        print("Patente invalida, debe tener exactamente 6 caracteres.")
    else:
            if patente_ingresada[:4].isalpha() and patente_ingresada[-2:].isdigit():
                print(f"La patente {patente_ingresada} es valida.")
                break
            else:
                print("Patente invalida.")