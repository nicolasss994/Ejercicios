patentes = ["  ab-cd-12  ", "EF-GH-34", " ij-kl-56 ", "mn-op-78"]
patentes_limpias = []

for patente in patentes:
    limpia = patente.strip().replace("-", "").upper()
    patentes_limpias.append(limpia)
print("-"*15, " PATENTES LIMPIAS ", "-"*15)
for patente in patentes_limpias:
    print(f"- {patente}")