import requests
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

def print_dic(dic, level = 0):
    for key in dic.keys():
        if type(dic[key]) is not dict:
            print(f"{level*' '}{key}: {dic[key]}")
        else:
            level += 2
            print(f"\n{key}")
            print_dic(dic[key], level)
            level -= 2

def comprar():
    while True:
        escolha = forca_opcao("Escolha um carro:", carros['modelo'])
        index_escolha = indices[escolha]
        for key in carros.keys():
            print(f"{key}: {carros[key][index_escolha]}")

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
                if carrinho['Valor Total'] != 0:
                    print("Preencha seus dados de endereço:")
                    carrinho['Endereço'] = endereco()
                    print("Indo para o seu carrinho...")
                    return
                print("Não há nenhum produto no carrinho.")

        else:
            ver_mais = forca_opcao("Quer ver outra opção?", s_ou_n)
            if ver_mais == s_ou_n[1]:
                break

def endereco():
    while True:
        cep = input("Digite seu CEP: ")
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        if response.status_code == 200:
            response = response.json()
            infos = ''
            for key in response.keys():
                infos += f'\n{key}: {response[key]}'
            print(infos)
            validar_endereco = forca_opcao("As informações estão corretas?", s_ou_n)
            if validar_endereco == s_ou_n[0]:
                response['unidade'] = input("Digite o número: ")
                response['complemento'] = input("Digite o complemento: ")
                return response
        print("CEP inválido!")

def remover():
    escolha = forca_opcao("Qual carro você deseja remover?", carros['modelo'])
    indice_remover = indices[escolha]
    for key in carros.keys():
        carros[key].pop(indice_remover)
    return


def cadastrar():
    for key in carros.keys():
        if dic_types[key] == int:
            while True:
                try:
                    info = int(input(f"Digite o novo(a) {key}: "))
                    break
                except:
                    print("Deve ser um número inteiro!")

        elif dic_types[key] == float:
            while True:
                try:
                    info = float(input(f"Digite o novo(a) {key}: "))
                    break
                except:
                    print("Deve ser um número float!")

        else:
            info = input(f"Digite o novo(a) {key}: ")
        carros[key].append(info)
    return

def atualizar():
    opcoes_atualizacao = list(carros.keys())
    opcoes_atualizacao.append("Total")
    escolha = forca_opcao("Qual carro você quer atualizar?", carros['modelo'])
    indice_escolha = indices[escolha]
    tipo_atualizacao = forca_opcao("Qual tipo de atualização?", opcoes_atualizacao)
    if tipo_atualizacao == opcoes_atualizacao[len(opcoes_atualizacao) - 1]:
        for key in carros.keys():
            carros[key][indice_escolha] = input(f"Diga o novo(a) {key} do carro {escolha}: ")
    else:
        carros[tipo_atualizacao][indice_escolha] = input(f"Digite o novo(a) {tipo_atualizacao} do carro {escolha}: ")
    return

def converte_float(key):
    while True:
        try:
            info = float(input(f"Diga o novo {key}: "))
            break
        except:
            print("Deve ser float!")
    return info


def converte_int(key):
    while True:
        try:
            info = int(input(f"Diga o novo {key}: "))
            break
        except:
            print("Deve ser inteiro!")
    return info

carros = {
    'modelo': ['Opala', 'Marea', 'Kombi', 'Celta', 'Uno', 'Monza'],
    'potência (cv)': [172, 130, 250, 140, 100, 120],
    'consumo (km/l)': [1., 3., 8., 7., 15., 2.],
    'cor': ['laranja', 'verde', 'branco', 'preto', 'prata', 'vinho'],
    'ano': ['1972', '2004', '1985', '2014', '2001', '1975'],
    'preço (R$)': [50., 10., 5., 1000000., 100., 200.],
    'estoque': [10, 8, 7, 5, 11, 9]
}

dic_types = {
    'potência (cv)': converte_int,
    'consumo (km/l)': converte_float,
    'preço (R$)': converte_int,
    'estoque': converte_float
}

'''for key in dic_types.keys():
    carros[key].append(dic_types[key](key))'''

texto = "Bagre branco, branco bagre."
texto = texto.lower()
for char in ',.:;!?':
    texto = texto.replace(char, '')
print(texto)
texto = texto.split(' ')
print(texto)
contagem = {}
for palavra in texto:
    if palavra in contagem.keys():
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
print(contagem)

indices = {carros['modelo'][i]: i for i in range(len(carros['modelo']))}

'''print(indices)

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


funcao = ['cliente', 'funcionário']
cliente_ou_funcionario = forca_opcao("Qual a sua função?", funcao)
operacoes = ['remover', 'cadastrar', 'atualizar']

if cliente_ou_funcionario == funcao[0]:
    comprar()
    print_dic(carrinho)

else:
    operacao = forca_opcao("Qual operação quer realizar?", operacoes)
    if operacao == operacoes[0]:
        remover()
    elif operacao == operacoes[1]:
        cadastrar()
    else:
        atualizar()
    indices = {carros['modelo'][i]: i for i in range(len(carros['modelo']))}
    print(pd.DataFrame(carros))'''



