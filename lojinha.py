import pandas as pd

def forca_opcao(msg, conjunto_opcoes, msg_erro = 'Inválido!'):
    opcoes = '\n'.join(conjunto_opcoes)
    print(opcoes)
    escolha = input(msg)
    while escolha not in conjunto_opcoes:
        print(msg_erro)
        escolha = input(msg)
    return escolha

def acha_index(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i

carros = {
    'modelo': ['Opala', 'Marea', 'Kombi', 'Celta', 'Uno', 'Monza'],
    'potência (cv)': [172, 130, 250, 140, 100, 120],
    'consumo (km/l)': [1, 3, 8, 7, 15, 2],
    'cor': ['laranja', 'verde', 'branco', 'preto', 'prata', 'vinho'],
    'ano': ['1972', '2004', '1985', '2014', '2001', '1975'],
    'estoque': [1, 1, 1, 1, 1, 1]
}


escolha = forca_opcao("Escolha um carro:\n-> ", carros['modelo'])
index_escolha = acha_index(carros['modelo'], escolha)

for key in carros.keys():
    print(key, carros[key][index_escolha])
