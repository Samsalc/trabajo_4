def saludar_usuario():
    nombre_usuario = input("Ingrese su nombre: ")
    mensaje_saludo = f"Hola, {nombre_usuario}! ¡Bienvenido master!"
    print(mensaje_saludo)


if __name__ == "__main__":
    saludar_usuario()
