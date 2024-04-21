def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def main():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        print("\nSeleccione una opción:")
        print("1. Mostrar la suma de los dos números")
        print("2. Mostrar la resta de los dos números (el primero menos el segundo)")
        print("3. Mostrar la multiplicación de los dos números")
        opcion = int(input("Ingrese el número de opción: "))

        if opcion == 1:
            print("La suma es:", sumar(num1, num2))
        elif opcion == 2:
            print("La resta es:", restar(num1, num2))
        elif opcion == 3:
            print("La multiplicación es:", multiplicar(num1, num2))
        else:
            print("Opción inválida. Por favor ingrese una opción válida (1, 2 o 3).")
    except ValueError:
        print("Error: Por favor ingrese números válidos.")

if __name__ == "__main__":
    main()
