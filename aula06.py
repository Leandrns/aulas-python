#-----------------------------------------------------------------#
#Obrigando o usuário a digitar umas das opções
'''idoso  = input("Você é idoso? (sim/não): ")
#while idoso != "sim" and idoso != "não":       #enquanto for diferente
while not (idoso == "sim" or idoso == "não"):   #enquanto não for igual
    idoso = input("Você é idoso? (sim/não): ")
if idoso == "sim":
    print("top")
else:
    print("bb")'''

#-----------------------------------------------------------------#

'''num = input("Diga um número: ")
while not num.isnumeric():      #enquanto 'num' não for um número
    num = input("Diga um número: ")
num = int(num)      #converte a string para inteiro
print(type(num), num)'''

#-----------------------------------------------------------------#
#Usando o break para sair do while

'''pares = 0
contador = 0

while True:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares += 1
    contador = contador + 1
    if contador >= 5:
        break
print(f"Você digitou {pares} números pares e {contador - pares} números ímpares.")'''
