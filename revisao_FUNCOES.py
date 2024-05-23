def verifica_numero(msg, msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    num = int(num)
    return num

#Função equivalente a: lista.index(elemento)
#Retorna o indice do elemento
def meu_index(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return

#Verifica se um elemento está na lista
def meu_in(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False

#Forçando o usuário a escolher uma opção usando a função meu_in
def forca_opcao(lista_opcoes, msg):
    msg_erro = '\n'.join(lista_opcoes)
    opcao = input(msg)
    while not meu_in(lista_opcoes, opcao):
        print(f"Opção inválida! Somente essas:\n{msg_erro}")
        opcao = input(msg)
    return opcao

#Encontrando o maior pressupondo que o maior é o primeiro
#Retorna o local do maior
def encontra_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice_maior = i
    return indice_maior

#Encontrando o menor pressupondo que o menor é o primeiro
#Retorna o local do menor
def encontra_menor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i
    return indice_menor

'''vinhos = ["Tinto", "Branco", "Seco", "Rose"]
precos = [30, 40, 50, 60]
vinho = forca_opcao(vinhos, "Escolha um vinho: ")
local_vinho = meu_index(vinhos, vinho)
print(f"O {vinhos[local_vinho]} custa {precos[local_vinho]}")

preco_maior = encontra_maior(precos)
print(f"{vinhos[preco_maior]}")'''

lista = [1,2,3,4,5,6,7,8,9]
ultimo = len(lista) - 1
for i in range(len(lista)//2):
    aux = lista[i]
    lista[i] = lista[ultimo - i]
    lista[ultimo - i] = aux
print(lista)
