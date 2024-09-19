import pandas as pd

def forca_opcao(msg, conjunto_opcoes, msg_erro = 'Inválido!'):
    opcoes = '\n'.join(conjunto_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n-> ")
    while escolha not in conjunto_opcoes:
        print(msg_erro)
        escolha = input(f"{msg}\n{opcoes}\n-> ")
    return escolha

def acha_index(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i

def forca_numero(msg, msg_erro = 'Inválido'):
    num = input(msg + "\n-> ")
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg + "\n-> ")
    return int(num)

carros = {
    'modelo': ['Opala', 'Marea', 'Kombi', 'Celta', 'Uno', 'Monza'],
    'potência (cv)': [172, 130, 250, 140, 100, 120],
    'consumo (km/l)': [1, 3, 8, 7, 15, 2],
    'cor': ['laranja', 'verde', 'branco', 'preto', 'prata', 'vinho'],
    'ano': ['1972', '2004', '1985', '2014', '2001', '1975'],
    'preço': [50, 10, 5, 1000000, 100, 200],
    'estoque': [10, 8, 7, 5, 11, 9]
}

indices = {}
for i in range(len(carros['modelo'])):
    indices[carros['modelo'][i]] = i
print(indices)

s_ou_n = ['sim', 'não']

carrinho = {
    'Carros': {},
    'Valor Total': 0,
    'Endereço': {
        'Rua': '',
        'CEP': '',
        'Número': ''
    }
}

while True:
    escolha = forca_opcao("Escolha um carro:", carros['modelo'])
    index_escolha = indices[escolha]
    for key in carros.keys():
        print(key, carros[key][index_escolha])

    comprar = forca_opcao("Você vai comprar esse carro?", s_ou_n)
    if comprar == s_ou_n[0]:
        qntd = forca_numero(f'Quantos {escolha} você quer?')
        if carros['estoque'][index_escolha] >= qntd:
            carros['estoque'][index_escolha] -= qntd
            carrinho['Valor Total'] += qntd * carros['preço'][index_escolha]
            if escolha not in carrinho['Carros'].keys():
                carrinho['Carros'][escolha] = qntd
            else:
                carrinho['Carros'][escolha] += qntd
        else:
            print(f"Não há {qntd} de {escolha} no estoque. Voltando ao início...")
            continue

        encerrar = forca_opcao("Quer encerrar a compra?", s_ou_n)
        if encerrar == s_ou_n[0]:
            print("Preencha seus dados de endereço:")
            for key in carrinho['Endereço'].keys():
                carrinho['Endereço'][key] = input(f"{key}:\n->")
            print("Indo para o seu carrinho...")
            print(carrinho)
            break

    else:
        ver_mais = forca_opcao("Quer ver outra opção?", s_ou_n)
        if ver_mais == s_ou_n[1]:
            break
