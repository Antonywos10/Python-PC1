def main():
    try:
        hora_str = input("Ingrese la hora en formato HH:MM (24 horas): ")
        hora_split = hora_str.split(":")
        hora = float(hora_split[0]) + float(hora_split[1]) / 60
        
        if 7 <= hora < 8:
            print("Es hora de desayunar.")
        elif 12 <= hora < 13:
            print("Es hora de almorzar.")
        elif 18 <= hora < 19:
            print("Es hora de cenar.")
    except ValueError:
        print("Error: Por favor ingrese una hora válida en formato HH:MM (24 horas).")

if __name__ == "__main__":
    main()
