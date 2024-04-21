def calcular_peso_total(payasos, munecas):
    peso_payaso = 112  # Peso de cada payaso en gramos
    peso_muneca = 75   # Peso de cada muñeca en gramos
    peso_total = (payasos * peso_payaso) + (munecas * peso_muneca)
    return peso_total

def main():
    try:
        payasos = int(input("Ingrese el número de payasos vendidos: "))
        munecas = int(input("Ingrese el número de muñecas vendidas: "))
        peso_total = calcular_peso_total(payasos, munecas)
        print("El peso total del paquete que será enviado es: {} gramos".format(peso_total))
    except ValueError:
        print("Error: Por favor ingrese un número válido de payasos y muñecas.")

if __name__ == "__main__":
    main()
