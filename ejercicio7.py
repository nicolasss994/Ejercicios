vigencia = input("Tu pasaporte esta vigente? (Si/no): ").lower()

if vigencia == "si":
 motivo = input("""Cual es el motivo de su viaje?
 - Turismo
 - Trabajo
 - Estudio
 - Otro
 Ingrese: """).lower()
 match motivo:
    case "turismo":
        print("Permiso concedido por 90 dias")
    case "trabajo":
        print("Debe presentar su contrato labroal en el modulo 5")
    case "estudio":
        print("Debe presentar su comprobante de matricula")
    case _:
        print("Por favor, espere a un oficial de migracion")
elif vigencia == "no":
 print("No puedes ingresar al pais, dirigete a la oficina de tramites")
else:
    print("Respuesta no valida")