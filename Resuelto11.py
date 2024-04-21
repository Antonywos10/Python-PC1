def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados

def main():
    lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
    lista_sin_duplicados = eliminar_duplicados(lista_original)
    print("Lista original:", lista_original)
    print("Lista sin duplicados:", lista_sin_duplicados)

if __name__ == "__main__":
    main()
