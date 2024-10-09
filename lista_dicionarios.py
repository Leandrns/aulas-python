def forca_opcao(msg, lista_opcoes, msg_erro = "Inválido"):
    for i in range(len(lista_opcoes)):
        print(lista_opcoes[i])
    escolha = input(f"{msg}\n-> ")
    while escolha not in lista_opcoes:
        print(msg_erro)
        escolha = input(f"{msg}\n-> ")
    return escolha

# QUESTÃO 2 - Printa escolha do usuário
vinhos = {
    "nome": ["Pérgola", "Cai-Cai Balão", "Bordoux"],
    "preco": [22.9, 62.5, 150.9],
    "origem": ["Brasil", "Argentina", "Chile"]
}

indices = {vinhos["nome"][i]: i for i in range(len(vinhos["nome"]))}

for key in vinhos.keys():
    print(vinhos[key])

'''escolha = input("Escolha um vinho: ")
index = indices[escolha]

for key in vinhos.keys():
    print(f"{key}: {vinhos[key][index]}")'''

# QUESTÃO 3 - Printa o mais caro
mais_caro = vinhos["preco"][0]
'''print("MAIS CARO")
for i in range(len(vinhos["preco"]) - 1):
    if mais_caro < vinhos["preco"][i+1]:
        mais_caro = vinhos["preco"][i+1]

index_mais_caro = vinhos["preco"].index(mais_caro)
for key in vinhos.keys():
    print(f"{key}: {vinhos[key][index_mais_caro]}")'''

# QUESTÃO 4 - Printa o mais barato
mais_barato = vinhos["preco"][0]
'''print("MAIS BARATO")
for i in range(len(vinhos["preco"]) - 1):
    if mais_barato > vinhos["preco"][i+1]:
        mais_barato = vinhos["preco"][i+1]

index_mais_barato = vinhos["preco"].index(mais_barato)
for key in vinhos.keys():
    print(f"{key}: {vinhos[key][index_mais_barato]}")'''

# QUESTÃO 5 - Cadastrar vinho
s_ou_n = ['sim', 'não']
'''cadastrar = forca_opcao("Deseja cadastrar um novo vinho?", s_ou_n)
if cadastrar == s_ou_n[0]:
    for key in vinhos.keys():
        novo = input(f"Digite o novo {key}:\n-> ")
        vinhos[key].append(novo)
print(vinhos)'''

# QUESTÃO 6
remover = forca_opcao("Deseja remover um vinho?", s_ou_n)
if remover == s_ou_n[0]:
    vinho = forca_opcao("Qual vinho vc quer remover?", vinhos["nome"])
    index_remover = indices[vinho]
    for key in vinhos.keys():
        vinhos[key].pop(index_remover)
print(vinhos)
