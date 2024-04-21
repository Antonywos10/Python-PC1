def saludo_usuario():
    # Solicitar al usuario que ingrese su nombre
    nombre = input("Por favor, introduce tu nombre de usuario: ")
    
    # Mostrar un mensaje de saludo personalizado
    print(f"¡Hola {nombre}!")

if __name__ == "__main__":
    saludo_usuario()
