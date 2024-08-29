import matplotlib.pyplot as plt

def print_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def mostra_elemento_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"Matriz[{i}][{j}] = {matriz[i][j]}")
    return

matriz_3x3 = [[1,2,3], [4,5,6], [7,8,9]]
'''mostra_elemento_matriz(matriz_3x3)
print_matriz(matriz_3x3)'''

def gera_matriz(linhas, colunas):
     matriz = []
     for i in range(linhas):
         sub_lista = []
         for j in range(colunas):
             sub_lista.append(i+j)
         matriz.append(sub_lista)
     return matriz

matriz = gera_matriz(10, 10)
print_matriz(matriz)
print(len(matriz))
'''plt.imshow(matriz, 'hot')
plt.colorbar()
plt.show()'''
