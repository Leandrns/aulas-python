'''def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    num = int(num)
    return num
ano = verifica_numero("Ano de nascimento: ")
print(ano)
qtd = verifica_numero("Quantidade de garrafas: ")
print(qtd)'''

'''def busca_elemento(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False
numeros = [4984, 84984, 984, 88, 7, 548, 87, 412, 96]
buscar = 984
print(busca_elemento(numeros, buscar))

professores = ['Danilo', 'André', 'Yan', 'Allen', 'Lucas', 'Fábio', 'Celso']
prof = 'Rafael'
print(busca_elemento(professores, prof))'''

#EXERCÍCIO 01
#Fazer uma função que recebe uma lista de números e retorna a soma
'''def soma_lista(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma
numeros = [4,8,8,6,3,0,1,2]
print(soma_lista(numeros))

def media_lista(lista):
    soma = soma_lista(lista)
    media = soma / len(lista)
    return media'''

#EXERCÍCIO 02
#Fazer uma função que recebe uma lista de números e retorna uma lista com os pares
'''def filtrar_pares(lista):
    pares = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
    return pares
numeros = [2,5,4,6,7,10,88,50,51,77]
print(filtrar_pares(numeros))'''

#EXERCÍCIO 03
#Fazer uma função que recebe uma string e conta a quantidade de vogais
'''def conta_vogais(string):
    qtd_vogais = 0
    vogais = ['a', 'e', 'i', 'o', 'u']
    for char in range(len(string)):
        if string[char] in vogais:
            qtd_vogais += 1
    return qtd_vogais
palavra = "ban"
print(f"'{palavra}' tem {conta_vogais(palavra)} vogais.")'''

#Função que obriga o usuário a escrever um item da lista
'''def obriga_escolha(msg, msg_erro, lista):
    opcao = input(msg)
    while opcao not in lista:
        print(msg_erro)
        opcao = input(msg)
    return opcao
vinhos = ['Tinto', 'Rose', 'Seco']
erro = '\n'.join(vinhos)    #join: insere um caractere entre os itens da lista
escolha = obriga_escolha("Diga seu vinho favorito: ", f"Somente:\n{erro}", vinhos)'''

#Encontrar o maior elemento de uma lista
def encontra_maior(numeros):
    indice_maior = 0
    maior = numeros[indice_maior]
    for i in range(len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i]
            indice_maior = i
    return indice_maior
precos = [10, 20, 30, 10000, 50]
carros = ['Up', 'Gol', 'Cruze', 'Celta', 'Uno']
local_mais_caro = encontra_maior(precos)
print(f"O carro mais caro é o {carros[local_mais_caro]}"
      f" e custa {precos[local_mais_caro]}")
