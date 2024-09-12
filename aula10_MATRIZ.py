import matplotlib.pyplot as plt

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

linhas = 1000
colunas = 1000
raio = linhas//2
circulo = gera_matriz(linhas, colunas)
raio2 = 0.9*raio
#Criando borda do circulo
for i in range(linhas):
    for j in range(colunas):
        if (i - raio)**2 + (j - raio)**2 <= raio**2 and (i - raio)**2 + (j - raio)**2 >= raio2**2:
            circulo[i][j] = i

plt.imshow(circulo)
plt.show()
