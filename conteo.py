conteo_letras = {}
frase = input("Dime una frase: ").lower()

for letra in frase:
    if letra != " ":
        if letra in conteo_letras:
            conteo_letras[letra] += 1
        else:
            conteo_letras[letra] = 1

for letra in sorted(conteo_letras):
    print(letra, ": ", conteo_letras[letra]) 