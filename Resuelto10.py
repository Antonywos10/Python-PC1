def eliminar_elementos(lista):
    indices_a_eliminar = [0, 4, 5]
    lista_resultante = [valor for indice, valor in enumerate(lista) if indice not in indices_a_eliminar]
    return lista_resultante

def main():
    lista_original = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
    lista_filtrada = eliminar_elementos(lista_original)
    print("Lista original:", lista_original)
    print("Lista después de eliminar los elementos en las posiciones 0, 4 y 5:", lista_filtrada)

if __name__ == "__main__":
    main()
