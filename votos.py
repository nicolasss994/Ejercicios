votos = ["Ana", "Pepe", "Ana", "Luis", "Ana", "Pepe", "Luis", "Ana"]
conteo = {}
ganador = ""
max_votos = 0

for persona in votos:
    if persona not in conteo:
        conteo[persona] = 1
    else:
        conteo[persona] += 1
for persona, cantidad in conteo.items():
    if cantidad > max_votos:
        max_votos = cantidad    
        ganador = persona
print("-"*15, " CANTIDAD DE VOTOS ", "-"*15)
for persona, cantidad in sorted(conteo.items()):
    print(f"- {persona}: {cantidad}")
print(f"Ganador: {ganador}")
        