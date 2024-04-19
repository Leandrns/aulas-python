##REVISÃO - AULA 1

#Operações
'''
nome = input("Diga seu nome: ")
primeiro_numero = int(input(f"{nome}, diga um número: "))
segundo_numero = int(input(f"{nome}, diga outro número: "))

soma = primeiro_numero + segundo_numero
print(f"A soma entre {primeiro_numero} e {segundo_numero} dá {soma}")

subt = primeiro_numero - segundo_numero
print(f"A subtração entre {primeiro_numero} e {segundo_numero} dá {subt}")

mult = primeiro_numero * segundo_numero
print(f"A multiplicação entre {primeiro_numero} e {segundo_numero} dá {mult}")

div = primeiro_numero / segundo_numero
print(f"A divisão entre {primeiro_numero} e {segundo_numero} dá {div}")
'''

#Variável acumulativa
'''
frase = "Eu "
print(frase)
frase = frase + "sou "
print(frase)
frase = frase + "o "
print(frase)
frase = frase + "Leandro"
print(frase)
'''

##AULA 2

#Operadores booleanos: >, <, >=, <=, ==, !=, or, and, not, is, in
'''
primeiro = 6
segundo = 5
a = primeiro>segundo
print(f"A comparação {primeiro} > {segundo} é {a}")
a = primeiro!=segundo
print(f"A comparação {primeiro} != {segundo} é {a}")
a = primeiro==segundo
print(f"A comparação {primeiro} == {segundo} é {a}")
a = primeiro<segundo
print(f"A comparação {primeiro} < {segundo} é {a}")
a = primeiro>=segundo
print(f"A comparação {primeiro} >= {segundo} é {a}")
'''
'''
a = 2
b = 3
c = 4
d = 5
#com OR

print(f"A comparação {a}>{b} or {c}>{d}, ou seja, {a>b} or {c>d}, é {a>b or c>d}")
print(f"A comparação {a}<{b} or {c}>{d}, ou seja, {a<b} or {c>d}, é {a<b or c>d}")
print(f"A comparação {a}>{b} or {c}!={d}, ou seja, {a>b} or {c!=d}, é {a>b or c!=d}")
print(f"A comparação {a}<={b} or {c}<{d}, ou seja, {a<=b} or {c<d}, é {a<=b or c<d}")
'''
#com AND
'''
print(f"A comparação {a}>{b} and {c}>{d}, ou seja, {a>b} and {c>d}, é {a>b and c>d}")
print(f"A comparação {a}<{b} and {c}>{d}, ou seja, {a<b} and {c>d}, é {a<b and c>d}")
print(f"A comparação {a}>{b} and {c}!={d}, ou seja, {a>b} and {c!=d}, é {a>b and c!=d}")
print(f"A comparação {a}<={b} and {c}<{d}, ou seja, {a<=b} and {c<d}, é {a<=b and c<d}")
'''
#usando if e else
'''
idade = int(input("Diga sua idade: "))
if idade < 18:
    print("Você não pode beber cerveja.")
else:
    print("Você pode beber cerveja.")
'''
'''
idoso = input("Você é idoso? ")
cadeirante = input("Você é cadeirante? ")
estacionar = False
if idoso == 'sim' or cadeirante == 'sim':
    print("Você pode estacionar!")
    estacionar = True
if estacionar == False:
    print("Você não pode estacionar.")
'''
#Identificar se a letra é uma vogal ou uma consoante

#com OR
'''
letra = str(input("Digite uma letra: "))
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"A letra '{letra}' é uma vogal.")
else:
    print(f"A letra '{letra}' é uma consoante.")
'''
#com ELIF
'''
vogal = False
letra = input("Digite uma letra: ")
if letra == 'a':
    vogal = True
elif letra == 'e':
    vogal = True
elif letra == 'i':
    vogal = True
elif letra == 'o':
    vogal = True
elif letra == 'u':
    vogal = True
else:
    print(f"A letra '{letra}' é uma consoante.")
if vogal == True:
    print(f"A letra '{letra}' é uma vogal.")
'''
'''
nota = int(input("Digite sua nota: "))
if nota >= 6:
    print("Aprovado!")
elif nota < 6 and nota >= 4:
    print("Exame.")
else:
    print("Reprovado :(")
'''
#ATIVIDADE - Cálculo Imposto de Renda
salario = float(input("Digite o seu salário: "))
if salario <= 1903.98:
    print(f"O desconto é: isento.")
    sal_final = salario
    print(f"Seu salário final é: R${sal_final}")

elif salario > 1903.98 and salario <= 2826.65:
    desconto = salario * 0.075
    print(f"O desconto é de R${desconto}.")
    sal_final = salario - desconto
    print(f"Seu salário final é: R${sal_final}")

elif salario > 2826.65 and salario <= 3751.05:
    desconto = salario * 0.15
    print(f"O desconto é de R${desconto}.")
    sal_final = salario - desconto
    print(f"Seu salário final é: R${sal_final}")

elif salario > 3751.05 and salario <= 4664.68:
    desconto = salario * 0.225
    print(f"O desconto é de R${desconto}.")
    sal_final = salario - desconto
    print(f"Seu salário final é: R${sal_final}")

else:
    desconto = salario * 0.275
    print(f"O desconto é de R${desconto}.")
    sal_final = salario - desconto
    print(f"Seu salário final é: R${sal_final}")
