import matplotlib.pyplot as plt
# QUESTÃO 03
def print_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def gera_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        sub_lista = []
        for j in range(colunas):
            sub_lista.append(0)
        matriz.append(sub_lista)
    return matriz

def diagonal_para_1 (matriz_quadrada):
    for i in range(len(matriz_quadrada)):
        matriz[i][i] = 1
    return

matriz = gera_matriz(8, 8)
'''diagonal_para_1(matriz)
print_matriz(matriz)'''

# QUESTÃO 04
def contra_diagonal_para_1(matriz_quadrada):
    for i in range(len(matriz_quadrada)):
        matriz[i][len(matriz_quadrada) - 1 - i] = 1
    return

'''contra_diagonal_para_1(matriz)
print_matriz(matriz)'''

# QUESTÃO 05
def trigonal_inferior(matriz_quadrada):
    for i in range(len(matriz_quadrada)):
        for j in range(i):
            matriz_quadrada[i][j] = 1
    return
def trigonal_superior(matriz_quadrada):
    for i in range(len(matriz_quadrada)):
        for j in range(i):
            matriz_quadrada[j][i] = 1
    return

'''trigonal_inferior(matriz)
trigonal_superior(matriz)
print_matriz(matriz)'''

# QUESTÃO 06
def transposta(matriz_quadrada):
    for i in range(len(matriz_quadrada)):
        for j in range(i):
            aux = matriz_quadrada[i][j]
            matriz_quadrada[i][j] = matriz_quadrada[j][i]
            matriz_quadrada[j][i] = aux
    return

'''trigonal_superior(matriz)
transposta(matriz)
print_matriz(matriz)
'''

# QUESTÃO 08
def xadrez(matriz_quadrada):
    for i in range(len(matriz_quadrada)):
        for j in range(len(matriz_quadrada)):
            if (i+j) % 2 == 0:
                matriz_quadrada[i][j] = 1
    return

xadrez(matriz)
print_matriz(matriz)
plt.imshow(matriz, 'gray')
plt.show()