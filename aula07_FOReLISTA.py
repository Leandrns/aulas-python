# = FOR =
'''for char in 'leandro':
    print(char)'''

# No FOR, as mudanças realizadas durante um passo não são levadas para o próximo passo
# pois já existe um conjunto pré-determinado de coisas.

'''for i in range(2, 10, 2):   #(start, end, step)
    print(i, end=' ')

for i in range(10, 2, -2):
    print(i, end=' ')'''

#EXEMPLO 01
'''senha_cadastrada = '1234'
for i in range(3):
    senha = input("Digite a senha: ")
    if senha == senha_cadastrada:
        print("Acesso liberado!")
        break
    print(f"Senha incorreta! Você tem {2-i} tentativas restantes.")
    
if senha != senha_cadastrada:
    print("Acesso negado!")'''

# EXERCÍCIO 01 - Some todos os números de 1 a 100 usando FOR
'''soma = 0
for i in range(1, 101):
    soma += i
print(soma)'''

# EXERCÍCIO 02 - Peça 10 números e conte a quantidade de ímpares e pares
'''pares = 0
for i in range(1, 11):
    num = input(f"Digite o {i}° número: ")
    while not num.isnumeric():
        num = input(f"Digite o {i}° número: ")
    num = int(num)
    if num % 2 == 0:
        pares += 1
print(f"Pares: {pares}\n"
      f"Ímpares: {i - pares}")'''

# EXERCÍCIO 03 - Peça 10 números e faça a soma e a média
'''soma = 0
for i in range(1, 11):
    num = input(f"Digite o {i}° número: ")
    while not num.isnumeric():
        num = input(f"Digite o {i}° número: ")
    num = int(num)
    soma += num
media = soma / i
print(f"Média: {media}")'''

# EXERCÍCIO 04 - Faça a tabuada de todos os números de 1 a 10
'''for i in range(1, 11):
    print(f"\nTabuada do {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")'''

# EXERCÍCIO 05 - Encontre a quantidade de vogais numa string que o usuário digitou
'''palavra = input("Digite uma palavra: ")
vogais = 0
for char in palavra:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vogais += 1
print(f"A palavra '{palavra}' possui {vogais} vogais.")'''

# = LISTA =
'''lista = [1, True, 3.2, 'leandro', ['anne', False]]
print(type(lista))
print(lista[0])
print(lista[1])

lista[4] = 3    #sobreescreve um valor da lista

for i in range(5):
    print(lista[i])

for j in range(len(lista)):
    print(lista[j])

for elem in lista:
    print(elem)'''

'''profs = ['André', 'Lucas Silva', 'Yan', 'Danilo', 'Allen', 'Fábio', 'Celso']
for i in range(len(profs)):
    if profs[i] == 'Danilo':
        print(f"{profs[i]} está na posição {i} da lista")
        break'''

'''profs = ['André', 'Lucas Silva', 'Yan', 'Danilo', 'Allen', 'Fábio', 'Celso']
materias = ['Storytelling', 'Front End', 'Edge', 'Python', 'Software TX Design', 'Web', 'Cálculo']
for i in range(len(profs)):
    print(f"{profs[i]} - {materias[i]}")'''

profs = ['André', 'Lucas Silva', 'Yan', 'Danilo', 'Allen', 'Fábio', 'Celso']
profs2 = ['Lucas Silva', 'João', 'Allen', 'Gilberto', 'Tamires']
for prof1 in profs:
    for prof2 in profs2:
        if prof1 == prof2:
            print(f"O(A) {prof1} dá aulas nas duas turmas")
