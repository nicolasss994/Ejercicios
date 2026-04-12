numeros = [-10, 90, -48, 47, 4, 6, 1, 3, 2, -2, -9, -5, -43, 5, 11, 89, -22, 69]
limpios = []

for positivos in numeros:
    if positivos >= 0:
        limpios.append(positivos)
else:
    limpios.sort()
    limpios = tuple(limpios)
    print(limpios)
