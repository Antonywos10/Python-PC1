def suma_enteros_hasta_N(N):
    suma = 0
    for i in range(1, N + 1):
        suma += i
    return suma

def main():
    try:
        N = int(input("Ingrese un entero positivo: "))
        if N <= 0:
            print("Error: Por favor ingrese un entero positivo.")
        else:
            resultado = suma_enteros_hasta_N(N)
            print("La suma de todos los enteros desde 1 hasta {} es: {}".format(N, resultado))
    except ValueError:
        print("Error: Por favor ingrese un número entero válido.")

if __name__ == "__main__":
    main()
