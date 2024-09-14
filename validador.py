#Creo y defino la funcion validar_contraseña
def validar_contraseña(contraseña):

 #le agrego la funcion len para obtener la longitud  
    if len(contraseña) < 8:
        return False

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    
    caracteres_especiales = "!@#$%^&*"

  #Itero mediante un ciclo for  
    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        elif caracter in caracteres_especiales:
            tiene_especial = True

    # Verificar si cumple con todos los criterios
    if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial:
        return True
    else:
        return False

# Solicitar al usuario que ingrese una contraseña
contraseña_usuario = input("Por favor, ingresa una contraseña: ")

# Validar la contraseña
if validar_contraseña(contraseña_usuario):
    print("Contraseña válida.")
else:
    print("Contraseña no válida. Asegúrate de que tenga al menos 8 caracteres, una mayúscula, una minúscula, un número y un carácter especial.")
