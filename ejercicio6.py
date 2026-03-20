menu = input("Bienvenido, tenemos pizza, hamburguesa y ensalada, que quiere? ").lower()

match menu:
    case "pizza":
        opcion = input("Quiere familiar o individual? ").lower()
        if opcion == "familiar":
            print("Aqui tiene su pizza familiar")
        elif opcion == "individual":
            print("Aqui tiene su pizza individual")
        else:
            print("Opcion invalida")
    case "hamburguesa":
        opcion = input("Quiere con queso o sin queso? ").lower()
        if opcion == "con queso":
            print("Aqui tiene su hamburguesa con queso")
        elif opcion == "sin queso":
            print("Aqui tiene su hamburguesa sin queso")
        else:
            print("Opcion invalida")
    case "ensalada":
        print("Preparando ensalada fresca")
    case _:
        print("No tenemos eso disculpe")
        