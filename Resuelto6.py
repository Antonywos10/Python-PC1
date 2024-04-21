def calcular_precio_entrada(edad):
    if edad < 4:
        return 0
    elif 4 <= edad <= 18:
        return 5
    else:
        return 10

def main():
    try:
        edad = int(input("Ingrese la edad del cliente: "))
        precio_entrada = calcular_precio_entrada(edad)
        print("El precio de la entrada es: ${}".format(precio_entrada))
    except ValueError:
        print("Error: Por favor ingrese una edad válida.")

if __name__ == "__main__":
    main()
