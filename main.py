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



def suma(x, y):
    return x + y


def multiplicar(x, y):
    return x * y


def division(x, y):
    if y != 0:
        return (x / y)

    else:
        print("No se puede dividir entro 0")
        return None


def resta(x, y):
    return x - y


opcion = input("Ingrese el numero de la opcion deseada (1 = suma, 2 = multiplicacion, 3 = division, 4 = resta): ")
if opcion == '1':
    numero_uno = float(input("Ingrese el primer numero: "))
    numero_dos = float(input("Ingrese el segundo numero: "))
    resultado = suma(numero_uno, numero_dos)
    print(f"El resultado de la suma es: {resultado}")

elif opcion == '2':
    numero_uno = float(input("Ingrese el primer numero: "))
    numero_dos = float(input("Ingrese el segundo numero: "))
    resultado = multiplicar(numero_uno, numero_dos)
    print(f"El resultado de la multiplicacion es: {resultado}")

elif opcion == '3':
    numero_uno = float(input("Ingrese el primer numero: "))
    numero_dos = float(input("Ingrese el segundo numero: "))
    resultado = division(numero_uno, numero_dos)
    print(f"El resultado de la division es: {resultado}")

else:
    numero_uno = float(input("Ingrese el primer numero: "))
    numero_dos = float(input("Ingrese el segundo numero: "))
    resultado = resta(numero_uno, numero_dos)
    print(f"El resultado de la resta es: {resultado}")