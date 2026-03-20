velocidad = int(input("A cuantos kms va el auto? "))

if velocidad > 120:
    print("Vas a exceso de velocidad")
elif velocidad >= 61 and velocidad <= 120:
    print("Vas muy rapido")
elif velocidad >= 20 and velocidad <= 60:
    print("Velocidad moderada")
else:
    print("Vas muy lento")