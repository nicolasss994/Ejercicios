horas = int(input("Cuantas horas estuviste estacionado? "))

if horas <= 0:
    print("ERROR")
else:
    tipo = input("Que tippo de vehiculo es? moto ($2 por hora), auto ($5 por hora) o camion ($10 por hora): ").lower()
    match tipo:
        case "moto":
            if horas > 8:
                print(f"Por estar mas de 8 horas tiene un descuento de 10%, y has estado {horas}, por eso debes pagar {horas*2*0.9}")
            else:
                print(f"Has estado {horas} horas estacionado, por ende debes pagar {horas*2}")
        case "auto":
            if horas > 8:
                print(f"Por estar mas de 8 horas tiene un descuento de 10%, y has estado {horas}, por eso debes pagar {horas*5*0.9}")
            else:
                print(f"Has estado {horas} horas estacionado, por ende debes pagar {horas*5}")
        case "camion":
            if horas > 8:
                print(f"Por estar mas de 8 horas tiene un descuento de 10%, y has estado {horas}, por eso debes pagar {horas*10*0.9}")
            else:
                print(f"Has estado {horas} horas estacionado, por ende debes pagar {horas*10}")
        case _:
                print("INVALIDO")