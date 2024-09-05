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

# QUESTÃO 07


# QUESTÃO 08
def xadrez(matriz_quadrada):
    for i in range(len(matriz_quadrada)):
        for j in range(len(matriz_quadrada)):
            if (i+j) % 2 == 0:
                matriz_quadrada[i][j] = 1
    return

'''xadrez(matriz)
print_matriz(matriz)
plt.imshow(matriz, 'gray')
plt.show()'''

# QUESTÃO 09
def create_circle_pattern(matrix_size):
    # Cria uma matriz de zeros com tamanho 'matrix_size'
    matrix = gera_matriz(matrix_size, matrix_size)

    # Calcula o centro da matriz
    center = matrix_size // 2

    # Define o raio do círculo
    radius = center

    # Preenche a matriz com o padrão de círculo
    for y in range(matrix_size):
        for x in range(matrix_size):
            # Calcula a distância do ponto (x, y) ao centro da matriz
            distance = ((x - center) ** 2 + (y - center) ** 2)**0.5
            # Se a distância for menor ou igual ao raio, define o valor da matriz como 255 (branco)
            if distance <= radius:
                matrix[y][x] = 1
    return matrix


# Tamanho da matriz (deve ser um valor par para que o círculo fique centralizado)
matrix_size = 1001

# Cria a matriz com o padrão de círculo
matrix = create_circle_pattern(matrix_size)

# Cria a imagem com matplotlib
plt.imshow(matrix, 'gray')
plt.show()