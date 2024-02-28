def saludar_usuario():
    nombre_usuario = input("Ingrese su nombre: ")
    mensaje_saludo = f"Hola, {nombre_usuario}! ¡Bienvenido master!"
    print(mensaje_saludo)


if __name__ == "__main__":
    saludar_usuario()


def contador_numero():
    numero = int(input("Ingresar un numero entero positivo: "))
    if numero < 0:
        print("Incorrecto, ingresar un numero entero positivo")
        return
    for i in range(1,numero + 1):
        print(i)

if __name__ == "__main__":
    contador_numero()