
def seleccion(A):
    for i in range(len(A)):
        minimo=i

        for j in range(i,len(A)):
            print(A[minimo],A[j])

            if(A[j]<A[minimo]):
                minimo=j
                print("-->posicion",minimo,"pasa a posicion->", i)
        if(minimo != i):
            aux = A[i]
            A[i] = A[minimo]
            A[minimo] = aux
            print(A)


#ordenamiento por seleccion
A = [6, 5, 3, 1, 8, 7, 2, 4, ]
print(A)
seleccion(A)