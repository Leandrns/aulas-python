'''senha_certa = '1234'
senha = input("Digite sua senha: ")
tentativas = 1
while senha != senha_certa and tentativas < 3:
    print("Senha incorreta!")
    senha = input("Digite sua senha: ")
    tentativas += 1
print("Acesso liberado!")'''

'''vinho1 = "Chapinha"
vinho2 = "Pérgola"

opcao = input(f"Escolha um vinho [{vinho1}][{vinho2}]: ")
while not (opcao == vinho1 or opcao == vinho2):
    opcao = input(f"Escolha um vinho [{vinho1}][{vinho2}]: ")

if opcao == vinho1:
    print("R$50")
else:
    print("R$60")'''

'''num = input("Diga um número: ")
while not num.isnumeric():
    print("Deve ser um número!")
    num = input("Diga um número: ")
num = int(num)'''

'''while True:
    num = input("Diga um número: ")
    if num.isnumeric():
        num = int(num)
        if num > 10 and num < 20:
            break
        print("Não está entre 10 e 20")
        continue
    print("Não é um número")'''

#QUESTAO 2
'''nome = input("Digite seu nome: ")
while len(nome) <= 3:
    print("O nome deve ter mais que três caracteres.")
    nome = input("Digite seu nome: ")

while True:
    idade = input("Digite sua idade: ")
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            break
        print("Não está entre 0 e 150.")
    else:
        print("Não é um número.")

while True:
    salario = input("Digite seu salário: ")
    if salario.isnumeric():
        salario = int(salario)
        if salario > 0:
            break
        print("Deve ser maior que 0.")
    else:
        print("Deve ser um número.")

sexo = input("Digite seu sexo, masculino[m] feminino[f]: ")
while not (sexo == 'm' or sexo == 'f'):
    print("Escolha uma das opções!")
    sexo = input("Digite seu sexo, masculino[m] ou feminino[f]: ")
    
estado_civil = input("Digite seu estado civil, solteiro[s], casado[c], viúvo[v] ou divorciado[d]: ")
while not (estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd'):
    print("Escolha uma das opções!")
    estado_civil = input("Digite seu estado civil, solteiro[s], casado[c], viúvo[v] ou divorciado[d]: ")
'''

#QUESTAO 7
'''num = 1
while num <= 10:
    mult = 1    #reinicia a variável mult
    print(f"Tabuada do {num}")
    while mult <= 10:
        print(f"{num} x {mult} = {num * mult}")
        mult += 1
    num += 1
    print()'''

#QUESTAO 12
'''n = 0
soma = 0
while True:
    nota = input(f"Digite a {n+1}ª nota: ")
    if nota.isnumeric():
        nota = int(nota)
        n += 1
        soma += nota
        opcao = input("Deseja adicionar mais uma nota? [sim][não]: ")
        while not (opcao == 'sim' or opcao == 'não'):
            opcao = input("Deseja adicionar mais uma nota? [sim][não]: ")
        if opcao == 'sim':
            continue
        break
    else:
        print("Não é um número.")
media = soma/n
print(f"A média é {media}")'''