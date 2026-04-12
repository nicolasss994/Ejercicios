clase = [{
    "nombre": "PEPE",
    "notas": [3.0, 7.0, 1.0],
    "asistencia": 87
    },     
    {
    "nombre": "ANA",
    "notas": [7.0, 7.0, 5.6],
    "asistencia": 34
    }, 
    {
    "nombre": "MANUEL",
    "notas": [5.6, 6.7, 5.8],
    "asistencia": 76
    }]

for alumno in clase:
    promedio = sum(alumno["notas"]) / len(alumno["notas"])
    alumno["promedio"] = promedio
    
    if promedio >= 4.0 and alumno["asistencia"] >= 75:
        alumno["estado"] = "Aprobado"
    else:
        alumno["estado"] = "Reprobado"
print("-"*7 + " ALUMNOS " + "-"*7)
for alumno in clase:
    print(f"- {alumno["nombre"]}: {alumno["promedio"]:.1f} está {alumno["estado"]}")
    
    