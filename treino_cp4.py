import matplotlib.pyplot as plt

def gera_fibonacci(qntd):
    a = 1
    b = 1
    fibo = []
    for i in range(qntd):
        c = a + b
        a = b
        b = c
        fibo.append(c)
    return fibo

#gera_fibonacci(8)

def seleciona_primos(lista):
    primos = []
    for i in range(len(lista)):
        divisores = 2
        for j in range(2, int(lista[i]**0.5)+1):
            if lista[i] % j == 0:
                divisores += 1
        if divisores == 2:
            primos.append(lista[i])
    return primos

def gera_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        sub_lista = []
        for j in range(colunas):
            sub_lista.append(0)
        matriz.append(sub_lista)
    return matriz

def print_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

fibo = gera_fibonacci(20)
'''print(fibo)
print(seleciona_primos(fibo))'''

matriz = gera_matriz(100, 100)
#print_matriz(matriz)
lista = [2, 3, 5, 13, 89]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        for k in range(len(lista)):
            if i + j == lista[k]:
                matriz[i][j] = 1

print_matriz(matriz)
plt.imshow(matriz)
plt.show()