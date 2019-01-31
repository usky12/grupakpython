def ordenamiento_insercion(lista_n):
    for i in range(len(lista_n)):
        minimo = i

        for j in range(i,len(lista_n)):
            """
            print(lista_n[minimo],lista_n[j])
            """
            if lista_n[j]<lista_n[minimo]:
                minimo=j
                """
                print("-->pos",minimo,"pas a pos->", i)
                """
        if minimo != i:
            aux = lista_n[i]
            lista_n[i] = lista_n[minimo]
            lista_n[minimo] = aux
            """
            print(lista_n)
            """

#ordenamiento por seleccion

if __name__ == '__main__':
    lista_n = [6, 5, 3, 1, 8, 7, 2, 4, ]
    ordenamiento_insercion(lista_n)
    """
    print(lista_n)
    """