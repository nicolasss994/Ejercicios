cantidad = int(input("Cuantas monedas quieres cambiar? "))
opcion = input("""A que tipo de moneda quieres cambiar?
A. dolares
B. euros
C. pesos 
Ingresa tu opcion """).lower()

match opcion:
    case "dolares":
        print(f"Has cambiado {cantidad} monedas a {cantidad} dolares")
    case "euros":
        print(f"Has cambiado {cantidad} monedas a {cantidad} euros")
    case "pesos":
        print(f"Has cambiado {cantidad} monedas a {cantidad*10} pesos")
    case _:
        print("cambio no valido.")