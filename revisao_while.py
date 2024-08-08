'''senha_certa = '1234'
senha = input("Digite sua senha: ")
tentativas = 1
while senha != senha_certa and tentativas < 3:
    print("Senha incorreta!")
    senha = input("Digite sua senha: ")
    tentativas += 1
print("Acesso liberado!")'''

vinho1 = "Chapinha"
vinho2 = "Pérgola"

opcao = input(f"Escolha um vinho [{vinho1}][{vinho2}]: ")
while opcao != vinho1 and opcao != vinho2:
    opcao = input(f"Escolha um vinho [{vinho1}][{vinho2}]: ")

if opcao == vinho1:
    print("R$50")
else:
    print("R$60")