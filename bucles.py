numeros = [5, 10, 15, 20]
subjects = ["matemáticas", "historia", "lenguaje", "ciencia"]
word = "Python"
suma = 0

for posicion, numero in enumerate(numeros, start=1):
    print(posicion, "-", numero)
print(" ")
for materia, numero1 in zip(subjects[::-1], numeros[::-1]):
    print(materia, "-", numero1)
print(" ")
for letra in word:
    print(letra.upper())
print(" ")
for letra in word[::-1]:
    print(letra.upper())
print(" ")
for numero3 in numeros:
    suma += numero3
    print(f"Suma acumulada: {suma}")