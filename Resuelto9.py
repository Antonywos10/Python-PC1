def invertir_lista(lista):
    return lista[::-1]

def main():
    lista_original = ['Di', 'buen', 'día', 'a', 'papa']
    lista_invertida = invertir_lista(lista_original)
    print("Lista original:", lista_original)
    print("Lista invertida:", lista_invertida)

if __name__ == "__main__":
    main()

