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
mostra_elemento_matriz(matriz_3x3)