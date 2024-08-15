# QUESTÃO 01
'''def soma_lista(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

numeros = [4, 8, 8, 9, 2, 12, 44]
print(soma_lista(numeros))
'''
# QUESTÃO 02
'''def encontra_maior(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior

numeros = [4, 8, 88, 99, 2, 12, 44]
print(encontra_maior(numeros))'''

# QUESTÃO 03
'''def comeca_com_a(lista):
    strings_com_a = []
    for i in range(len(lista)):
        if lista[i][0] == 'a':
            strings_com_a.append(lista[i])
    return strings_com_a

strings =["azul", "roxo", "amarelo", "lilás", "abacate"]
print(comeca_com_a(strings))
'''

# QUESTÃO 04
'''def encontra_pares(lista):
    lista_pares = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            lista_pares.append(lista[i])
    return lista_pares

numeros = [4, 7, 88, 99, 2, 13, 44]
print(encontra_pares(numeros))'''

# QUESTÃO 05
def conta_letras(lista):
    quantidades = []
    for i in range(len(lista)):
        quantidades.append(len(lista[i]))
    return quantidades

strings =["azul", "roxo", "amarelo", "lilás", "abacate"]
print(conta_letras(strings))