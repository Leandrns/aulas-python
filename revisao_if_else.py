# Exercício do salário
'''salario = float(input("Salário: "))

if salario <= 1903.98:
    aliquota = 0

elif salario <= 2826.65:
    aliquota = 0.075

elif salario <= 3751.05:
    aliquota = 0.15

elif salario <= 4664.68:
    aliquota = 0.225

else:
    aliquota = 0.275

desconto = aliquota * salario
salario -= desconto
print(f"O desconto é de {desconto:.2f}. Seu salário é {salario:.2f}")'''

# Refazendo a lista de if e else
## 01
'''num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
if num1 > num2:
    print(f"O maior é o {num1}")
else:
    print(f"O maior é o {num2}")'''

## 02
'''ano_nasc = int(input("Digite seu ano de nascimento: "))
if 2024 - ano_nasc < 16:
    print("Você não pode votar esse ano.")
else:
    print("Você deve votar esse ano.")'''

## 03
'''senha_certa = "1234"
senha = input("Digite a senha: ")
if senha == senha_certa:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")'''

## 04
'''qntd_macas = int(input("Quantas maçãs você quer: "))
if qntd_macas < 12:
    preco_un = 0.30
else:
    preco_un = 0.25
total = qntd_macas * preco_un
print(f"O valor da sua compra é R${total:.2f}")'''

## 05
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))

# Primeira forma
'''maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

meio = num1 + num2 + num3 - maior - menor
print(menor, meio, maior)'''

# Segunda forma
if num1 > num2 and num1 > num3:
    aux = num1
    num1 = num3
    num3 = aux
elif num2 > num3:
    aux = num2
    num2 = num3
    num3 = aux
if num1 > num2:
    aux = num1
    num1 = num2
    num2 = aux
print(num1, num2, num3)


## 06
'''altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo [1]Feminino [2]Masculino:")
if sexo == '1':
    peso_ideal = 72.7 * altura - 58
else:
    peso_ideal = 62.1 * altura - 44.7
print(f"Seu peso ideal é {peso_ideal}kg.")'''

## 07 e 08
'''qntd_lados = int(input("Digite a quantidade de lados do polígono: "))

if qntd_lados < 3:
    print("Não é um polígono.")
elif qntd_lados > 5:
    print("Polígono não identificado.")
else:
    medida = int(input("Digite a medida do lado em cm: "))
    if qntd_lados == 3:
        poligono = "Triângulo"
    elif qntd_lados == 4:
        poligono = "Quadrado"
    elif qntd_lados == 5:
        poligono = "Pentágono"
    print(f"O polígono é um {poligono} e tem perímetro de {qntd_lados*medida}cm")'''

## 09
'''a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print(maior)'''

## 10
'''a = input("Medida do lado 1: ")
b = input("Medida do lado 2: ")
c = input("Medida do lado 3: ")
if a == b and b == c:
    print("Equilátero")
elif a == b or a == c or b == c:
    print("Isósceles")
else:
    print("Escaleno")'''

## 11
'''a = input("Ângulo 1: ")
b = input("Ângulo 2: ")
c = input("Ângulo 3: ")
if a == '90' or b == '90' or c == '90':
    print("Triângulo Retângulo")
elif a > '90' or b > '90' or c > '90':
    print("Triângulo Obtusângulo")
elif a < '90' and b < '90' and c < '90':
    print("Triângulo Acutângulo")'''
