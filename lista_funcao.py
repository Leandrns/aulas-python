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
'''def conta_letras(lista):
    quantidades = []
    for i in range(len(lista)):
        quantidades.append(len(lista[i]))
    return quantidades

strings =["azul", "roxo", "amarelo", "lilás", "abacate"]
print(conta_letras(strings))'''

# QUESTÃO 06
'''def encontra_comuns(lista1, lista2):
    comuns = []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                comuns.append(lista1[i])
                break
    return comuns

multiplos_2 = [2, 4, 6, 8, 10, 12, 14]
multiplos_3 = [3, 6, 9, 12, 15, 18]
multiplos_4 = [4, 8, 12, 16, 20]
print(encontra_comuns(multiplos_4, multiplos_3))'''

# QUESTÃO 07
'''def verifica_crescente(numeros):
    crescente = True
    for i in range(len(numeros)-1):
        if numeros[i+1] > numeros[i]:
            crescente = True
        else:
            crescente = False
            break

    return crescente

numeros_crescente = [1, 2, 3, 4]
numeros_nao_crescente = [2, 3, 1, 4]
print(verifica_crescente(numeros_crescente))'''

# QUESTÃO 08
'''def inverte_lista(lista):
    lista_inversa = []
    for i in range(len(lista)-1, -1, -1):
        lista_inversa.append(lista[i])
    return lista_inversa

numeros = [2, 4, 6, 8]
print(inverte_lista(numeros))'''

# QUESTÃO 09


# QUESTÃO 10
