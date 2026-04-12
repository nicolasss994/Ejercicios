import random

paquetes_cargados = 0
decision = input("Bienvenido al analisis de la carga, escribe [empezar] para iniciar o (salir) para cancelar el analisis: ").lower()

while paquetes_cargados < 5:
    if decision == "empezar":
        analisis_paquete = random.randint(1, 10)
        if analisis_paquete == 1:
            print("PAQUETE EN ALERTA DE INCENDIO, APAGANDO SISTEMA")
            break
        elif analisis_paquete <=3:
            print("Este paquete esta roto, pasando al siguiente...")
            continue
        else:
            paquetes_cargados += 1
            print(f"Paquete bueno, cargado exitosamente y hasta ahora hay {paquetes_cargados} cargados.")
    elif decision == "salir":
        print("Saliendo...")
        break
    else:
        print("Opcion invalida.")
        break