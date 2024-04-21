def calcular_propina():
    try:
        # Solicitar al usuario el monto del consumo en el restaurante
        consumo = float(input("¿Cuánto fue tu consumo en el restaurante? $"))
        
        # Solicitar al usuario el porcentaje de propina que desea dejar
        porcentaje_propina = float(input("¿Qué porcentaje de propina deseas dejar? (Ejemplo: 15 para 15%) "))
        
        # Calcular la cantidad de dinero a dejar como propina
        propina = consumo * (porcentaje_propina / 100)
        
        # Mostrar el resultado
        print(f"Deberías dejar ${propina:.2f} como propina.")
        
    except ValueError:
        print("Por favor, introduce una cantidad válida.")

if __name__ == "__main__":
    calcular_propina()
