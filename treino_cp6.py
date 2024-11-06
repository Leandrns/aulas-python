def bubble_sort(numeros):
    ops = 0
    for j in range(len(numeros)):
        trocas = 0
        for i in range(len(numeros)-1-j):
            if numeros[i] > numeros[i+1]:
                aux = numeros[i]
                numeros[i] = numeros[i+1]
                numeros[i+1] = aux
                trocas += 1
        if trocas == 0:
            return numeros


lista = [3,1,4,6,5,2,8,7]
lista = bubble_sort(lista)
print(lista)