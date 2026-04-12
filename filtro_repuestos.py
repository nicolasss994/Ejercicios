stock = {
    "mazda demio": ["filtro aire", "bieletas", "pastillas freno"],
    "toyota yaris": ["bujias", "filtro aceite", "kit embrague"],
    "suzuki swift": ["correa alternador", "disco freno"]
}
auto = input("Que auto es? Tenemos repuestos de mazda demio, toyota yaris y suzuki swift: ").lower()
repuesto = input("Que repuesto necesitas?: ").lower()

if auto in stock:
    if repuesto in stock[auto]:
        print(f"Si tenemos el repuesto {repuesto} para el {auto}")
    else:
        print(f"No tenemos ese repuesto para el {auto} pero si tenemos los siguientes:")
        for f in stock[auto]:
            print(f"- {f}")
else:
    print("No tenemos repuestos para ese auto.")