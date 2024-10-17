def acha_menor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i
    return indice_menor

def selection_sort(numeros):    # RUIM
    ordenada = []
    while numeros:
        indice = acha_menor(numeros)
        elemento = numeros.pop(indice)
        ordenada.append(elemento)
    return ordenada

numeros = [7,4,1,3,2,0,8,6,9,5]

def selection_sort_2(numeros):    # RUIM
    for i in range(len(numeros)):
        # Corrige o delay (sem o +i, pega o indice da lista reduzida mas troca com o indice na lista original)
        indice_menor = acha_menor(numeros[i:])
        aux = numeros[i]
        numeros[i] = numeros[indice_menor]
        numeros[indice_menor] = aux
    return numeros

# Os algoritmos acima são quadráticos O(n²) = são ruins

def bubble_sort(numeros):
    ops = 0
    for j in range(len(numeros)):
        trocas = 0
        for i in range(len(numeros)-1-j):   # -j pq o maior já vai para o último, ent nao precisa testar dnv
            if numeros[i] > numeros[i+1]:
                aux = numeros[i]
                numeros[i] = numeros[i+1]
                numeros[i+1] = aux
                trocas += 1
            ops += 1
        if trocas == 0:
            print(ops)
            return numeros


# Busca binária
num = 25
def raiz_binaria(num):
    inicio = 0
    fim = num
    while True:
        chute = (inicio + fim)/2
        if chute**2 > num:
            fim = chute
        else:
            inicio = chute
        if fim - inicio <= 0.0001:
            return chute

def raiz_binaria_recursiva(num, inicio, fim):
    chute = (inicio + fim)/2
    if fim - inicio >= 0.001:
        if chute**2 > num:
            fim = chute
        else:
            inicio = chute
        chute = raiz_binaria_recursiva(num, inicio, fim)
    return chute

def verifica_numero(msg):   # função recursiva
    num = input(msg)
    if not num.isnumeric():
        num = verifica_numero(msg)
    return num

lista = [5,3,4,2,8,9,7,10,6,1]
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    menores = [elem for elem in lista if elem < pivo]
    maiores = [elem for elem in lista if elem > pivo]
    print(menores, [pivo], maiores)
    menores_ordenada = quick_sort(menores)
    maiores_ordenada = quick_sort(maiores)
    return menores_ordenada + [pivo] + maiores_ordenada

lista = quick_sort(lista)
print(lista)
