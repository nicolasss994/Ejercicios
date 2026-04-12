usuarios_registrados = []

while True:
    
    while True:
        nombre = input("Con que usuario te quieres registrar? Debe tener al menos 5 caracteres: ")
        
        if len(nombre) < 5:
            print("Tiene menos de 5 caracteres, prueba con otro")
        else:
            print("Usuario definido correctamente")
            break

    
    while True:
        contraseña = input("Con que contraseña te quieres registrar? Debe tener 8 caracteres y al menos un numero: ")
        
        tiene_numero = False 
        
        for letra in contraseña:
            if letra.isdigit():
                tiene_numero = True
        
        if len(contraseña) < 8:
            print("Tiene menos de 8 caracteres")
        elif not tiene_numero:
            print("No tiene al menos un numero")
        else:
            print("Contraseña válida")
            break

   
    usuarios_registrados.append({
        "Usuario": nombre,
        "Contraseña": contraseña
    })

    print("Usuario registrado correctamente")
    break

print(usuarios_registrados)