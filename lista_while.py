# ---- LISTA WHILE ---- #

# QUESTÃO 01 - C O R R I G I D O
'''nota = input("Digite a nota (de 0 a 10): ")
while True:
    if nota.isnumeric():
        if int(nota) >= 0 and int(nota) <= 10:
            nota = int(nota)
            break
        else:
            print("Valor inválido, tente novamente.")
            nota = input("Digite a nota (de 0 a 10): ")
    else:
        print("Você não digitou um número!")
        nota = input("Digite a nota (de 0 a 10): ")
print(f"A nota é {nota}.")'''

#QUESTÃO 02 - C O R R I G I D O
'''nome = input("Digite seu nome: ")
while len(nome) < 3:
    print("Digite mais que 3 caracteres!")
    nome = input("Digite seu nome: ")

while True:
    idade = input("Digite sua idade: ")
    if idade.isnumeric():
        idade = int(idade)
        if idade >= 0 and idade <= 150:
            print(f"Nota registrada: {idade}")
            break
        else:
            print("O número não está entre 0 e 150.")
    else:
        print("Deve ser um número.")

while True:
    salario = input("Digite seu salário: ")
    if salario.isnumeric():
        salario = int(salario)
        if salario > 0:
            break
        else:
            print("Deve ser um valor positivo.")
    else:
        print("Deve ser um número.")
            
sexo = input("Digite seu sexo (F ou M): ")
while not (sexo == 'F' or sexo == 'M'):
    print("Valor inválido.")
    sexo = input("Digite seu sexo (F ou M): ")

estado_civil = input("Digite seu estado civil (S, C, V ou D): ")
while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
    print("Valor inválido.")
    estado_civil = input("Digite seu estado civil (S, C, V ou D): ")

print(f"Nome: {nome}\n"
      f"Idade: {idade}\n"
      f"Salário: R${salario}\n"
      f"Sexo: {sexo}\n"
      f"Estado civil: {estado_civil}")'''

#QUESTÃO 03 - C O R R I G I D O
'''pais_a = 80000
pais_b = 200000
taxa_crescimento_a = 1.03
taxa_crescimento_b = 1.015
anos = 0
while pais_a < pais_b:
    pais_a *= taxa_crescimento_a
    pais_b *= taxa_crescimento_b
    anos += 1

print(f"O país A se igualou ou ultrapassou o país B em {anos} anos.\n"
      f"País A: {pais_a:.0f} habitantes\n"
      f"País B: {pais_b:.0f} habitantes")'''

#QUESTÃO 04 - C O R R I G I D O
'''i = 0
soma = 0
while i < 5:
    num = input(f"Digite o {i+1}° número: ")
    while not num.isnumeric():
        print("Não é um número!")
        num = input(f"Digite o {i+1}° número: ")
    num = int(num)
    soma += num
    i += 1
media = soma/5
print(f"Soma dos números: {soma}\n"
      f"Média: {media:.2f}")'''

#QUESTÃO 05 - C O R R I G I D O
'''a = input("Digite um número: ")
while not a.isnumeric():
    print("Não é um número!")
    inicio = input("Digite um número: ")
a = int(a)

b = input("Digite outro número: ")
while not b.isnumeric():
    print("Não é um número!")
    fim = input("Digite outro número: ")
b = int(b)

if b < a:
    aux = a
    a = b
    b = aux

while a <= b:
    print(a)
    a += 1'''

#QUESTÃO 06 - C O R R I G I D O
'''nome_usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
while nome_usuario == senha:
    print("ERRO! Nome de usuário igual à senha.")
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
print("Sucesso! Entrando...")'''

#QUESTÃO 07 - C O R R I G I D O
'''num = input("Digite um número que deseja saber a tabuada: ")
while not num.isnumeric():
    print("Não é um número!")
    num = input("Digite um número que deseja saber a tabuada: ")
num = int(num)
i = 1
multiplicacao = 0
while i <= 10:
    multiplicacao = num * i
    print(f"{num} x {i} = {multiplicacao}")
    i += 1'''

#QUESTÃO 07.1 - Todas as tabuadas do 1 ao 10
'''num = 1
i = 1
while num <= 10:
    print(f"----- TABUADA DO {num} -----")
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num*i}")
        i += 1
    num += 1'''

#QUESTÃO 08 - C O R R I G I D O
'''a = 1
b = 1
n = int(input("Digite até qual termo da Sequência de Fibonacci você quer saber: "))
print(a, end=' ')
print(b, end=' ')
i = 2
while i < n:
    c = a + b
    a = b
    b = c
    print(c, end=' ')
    i += 1'''

#QUESTÃO 09 - C O R R I G I D O
'''i = 1
pares = 0
while i <= 10:
    num = input(f"Digite o {i}° número: ")
    if not num.isnumeric():
        print("Não é um número!")
        continue    #manda para a próxima repetição (foda-se oq ta em baixo)
    num = int(num)
    if num % 2 == 0:
        pares += 1
    i += 1
print(f"Quantidade de pares: {pares}\n"
      f"Quantidade de ímpares: {i - pares}")'''

#QUESTÃO 10 - C O R R I G I D O
'''num = input("Digite um número (> 0) que deseja saber seu fatorial: ")
while not num.isnumeric():
    print("Não é um número")
    num = input("Digite um número (> 0) que deseja saber seu fatorial: ")
num = int(num)
fatorial = num
fatorial_string = f"{num}!"
while num > 1:
    num -= 1
    fatorial *= num
print(f"{fatorial_string} = {fatorial}")'''

#QUESTÃO 11 - C O R R I G I D O
'''num = input("Digite um número: ")
while not num.isnumeric():
    print("Não é um número!")
    num = input("Digite um número: ")
num = int(num)

i = 2
while i < num**0.5:
    if num % i == 0:
        print(f"O número {num} não é primo.")
        break
    i += 1
if i >= num**0.5:
    print(f"O número {num} é primo!")'''

#QUESTÃO 12
'''qntd_notas = input("De quantas notas deseja saber a média aritmética?:  ")
while not qntd_notas.isnumeric():
    print("Não é um número!")
    qntd_notas = input("De quantas notas deseja saber a média aritmética?:  ")
qntd_notas = int(qntd_notas)

i = 1
soma_notas = 0
while i <= qntd_notas:
    nota = input(f"Digite a {i}° nota: ")
    while not nota.isnumeric():
        print("Não é um número!")
        nota = input(f"Digite a {i}° nota: ")
    soma_notas += nota
    i += 1
media = soma_notas/qntd_notas
print(f"A média aritmética das notas é: {media:.2f}")'''

#QUESTÃO 13
'''ano_inicial = 1996
salario = 1000
aumento = 0.015
while ano_inicial <= 2004:
    salario *= (1 + aumento)
    aumento *= 2
    ano_inicial += 1 
print(int(salario))'''

#QUESTÃO 14