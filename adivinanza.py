import random
intentos = 15
numero_bueno = random.randint(1, 100)
while intentos > 0:
    numero = int(input(f"Ingresa el numero, actualmente te quedan {intentos}: "))
    if numero == numero_bueno:
        print(f"Felicidades! Lo has logrado con {intentos} intentos restantes, el numero era {numero_bueno}")
        break
    elif numero < numero_bueno:
        intentos -= 1
        print("El numero bueno es mayor.")
    else: 
        intentos -= 1
        print("El numero bueno es menor.")
else:
    print(f"Perdiste, el numero era {numero_bueno}")