def main():
    try:
        shows_vistos = int(input("Ingrese cuántos shows musicales ha visto en el último año: "))
        mas_de_3 = shows_vistos > 3
        print("¿Ha visto más de 3 shows musicales en el último año?:", mas_de_3)
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()
