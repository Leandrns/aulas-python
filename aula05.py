'''pares = 0
contador = 0

while contador < 5:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares = pares + 1
    contador = contador + 1
print(f"Você digitou {pares} números pares.")'''
 
#-----------------------------------------------------------------#
 
tentativas = 1
senha_certa = '12345' 
senha = input("Digite a senha: ") 
while senha != senha_certa and tentativas < 3: 
    print("Senha INCORRETA, tente novamente.") 
    print(f"Resta(m) {3 - tentativas} tentativa(s).") 
    senha = input("Digite a senha: ") 
    tentativas += 1 
if senha != senha_certa: 
    print("Senha INCORRETA. Limite de tentativas atingido!") 
else: 
    print("Senha CORRETA, acesso liberado!")
 
#-----------------------------------------------------------------#
#Soma dos números de 1 a 100 
 
'''soma = 0 
i = 1 
while i <= 100:
    soma +=  i 
    i += 1 
print(f"A soma dos números de 1 a 100 é {soma}")''' 
 
#-----------------------------------------------------------------#
#Soma dos quadrados perfeitos de 1 a 10 
 
'''soma = 0 
i = 1 
while i <= 10: 
    soma += i**2 
    i += 1 
print(f"A soma dos quadrados perfeitos de 1 a 10 é {soma}") '''
 
#-----------------------------------------------------------------#
