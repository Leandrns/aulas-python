#QUESTÃO 01
'''num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
if num1 > num2:
    print(f"O maior é o valor {num1}")
else:
    print(f"O maior é o valor {num2}")'''

#QUESTÃO 02
'''ano = int(input("Digite o seu ano de nascimento: ")) 
idade = 2024 - ano 
if idade < 16: 
   print("Você não pode votar esse ano.") 
elif idade < 18: 
   print("Seu voto é opcional esse ano.") 
else: 
   print("Você é obrigado a votar esse ano.")'''

#QUESTÃO 03
'''senha = int(input("Digite a senha: ")) 
if senha == 1234: 
   print("ACESSO PERMITIDO") 
else: 
   print("ACESSO NEGADO")'''

#QUESTÃO 04
'''qntd = int(input("Quantas maçãs foram compradas? ")) 
if qntd < 12: 
   valor_un = 0.30 
else: 
   valor_un = 0.25 

valor_final = qntd * valor_un 
print(f"Valor total da compra: R${valor_final}")'''

#QUESTÃO 05 -- C O R R I G I D O
## Primeira forma
'''a = int(input("Digite o primeiro valor: ")) 
b = int(input("Digite o segundo valor: ")) 
c = int(input("Digite o terceiro valor: ")) 
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

menor = a
if b < menor:
    menor = b
if c < maior:
    menor = c
meio = a + b + c - menor - maior
print(menor, meio, maior)'''

## Segunda forma
'''a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a > b and a > c:
    aux = a
    a = c
    c = aux
elif b > c:
    aux = b
    b = c
    c = aux
if a > b:
    aux = a
    a = b
    b = aux
print(a , b , c)'''

#QUESTÃO 06
'''altura = float(input("Digite a sua altura: ")) 
sexo = int(input("Digite o número correspondente ao seu sexo (1: Feminino   2: Masculino): ")) 
if sexo == 1: 
   peso_ideal = (62.1 * altura) - 44.7 
else: 
   peso_ideal = (72.7 * altura) - 58 

print(f"Seu peso ideal é: {peso_ideal:.2f}")'''

#QUESTÃO 07
'''qntd_lado = int(input("Digite quantos lados possui o polígono: ")) 
medida = int(input("Digite a medida do lado do polígono (em CM): ")) 

if qntd_lado == 3: 
   print("TRIÂNGULO") 

elif qntd_lado == 4: 
   print("QUADRADO") 

elif qntd_lado == 5: 
   print("PENTÁGONO") 
   
per = medida*qntd_lado
print(f"O perímetro vale {per}cm") '''

#QUESTÃO 08 -- C O R R I G I D O
'''qntd_lado = int(input("Digite quantos lados possui o polígono: "))
if qntd_lado > 5:
    print("Polígono não identificado.")
elif qntd_lado < 3:
    print("Não é um polígono.")
else:
    medida = int(input("Digite a medida do lado do polígono (em CM): "))
    if qntd_lado == 3:
        print("TRIÂNGULO")
    elif qntd_lado == 4:
        print("QUADRADO")
    else:
        print("PENTÁGONO")
    per = medida*qntd_lado
    print(f"O perímetro vale {per}cm")'''

#QUESTÃO 09 -- C O R R I G I D O
'''a = int(input("Digite o primeiro valor:")) 
b = int(input("Digite o segundo valor:")) 
c = int(input("Digite o terceiro valor:")) 

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print(maior)'''

#QUESTÃO 10 -- C O R R I G I D O
'''lado1 = int(input("Digite o valor do lado 1: ")) 
lado2 = int(input("Digite o valor do lado 2: ")) 
lado3 = int(input("Digite o valor do lado 3: ")) 

if lado1 == lado2 and lado2 == lado3:
    print("O triângulo é EQUILÁTERO")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("O triângulo é ISÓSCELES")
else:
    print("O triângulo é ESCALENO")'''

#QUESTÃO 11 -- C O R R I G I D O
'''ang1 = int(input("Digite o valor do primeiro ângulo: ")) 
ang2 = int(input("Digite o valor do segundo ângulo: ")) 
ang3 = int(input("Digite o valor do terceiro ângulo: ")) 
if ang1 == 90 or ang2 == 90 or ang3 == 90: 
   print("O triângulo é RETÂNGULO") 
elif ang1 > 90 or ang2 > 90 or ang3 > 90: 
   print("O triângulo é OBTUSÂNGULO") 
elif ang1 < 90 and ang2 < 90 and ang3 < 90: 
   print("O triângulo é ACUTÂNGULO")'''
