mes = int(input("Dame el mes del año en numeros: "))

if mes in (12, 1, 2):
    print("verano")
elif mes in (3, 4, 5):
    print("Otoño")
elif mes in (6, 7, 8):
    print("invierno")
elif mes in (9, 10, 11):
    print("primavera")
else:
    print("mes invalido")
    