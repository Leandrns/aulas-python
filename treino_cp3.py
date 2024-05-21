def verifica_numero(msg, msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    return int(num)

def obriga_opcao(msg, msg_erro, lista):
    opcao = input(msg)
    while opcao not in lista:
        print(msg_erro)
        opcao = input(msg)
    return opcao

def busca_indice(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i

print("====== Seja bem-vindo(a) a Vinheria Agnello! ======")
ano_nascimento = verifica_numero("Digite seu ano de nascimento\n-> ",
                                 "O ano digitado não é composto somente por números!")
if 2024 - ano_nascimento < 18:
    print("Você possui menos de 18 anos, não pode comprar bebidas alcoólicas!")
else:
    endereco = input("Digite seu endereço:\n-> ")
    vinhos = ["Vinho Tinto", "Vinho Branco", "Vinho Rose"]
    vinhos_num = ['1', '2', '3']
    precos = [30, 40, 60]
    quantidades_vinhos = [0, 0, 0]
    catalogo = ''
    total = 0
    frete = 15
    opcoes_continuar = ['sim', 'não']
    for i in range(len(vinhos)):
        catalogo += f"{vinhos_num[i]} - {vinhos[i]} - R${precos[i]}\n"
    while True:
        print("====== CATÁLOGO ======")
        print(catalogo)
        escolha = obriga_opcao("Digite o número que corresponde ao vinho que deseja comprar:\n-> ",
                               f"Digite apenas uma das opções disponíveis!\n{catalogo}", vinhos_num)

        quantidade = verifica_numero(f"Digite a quantidade de garrafas de {vinhos[int(escolha)-1]}\n-> ",
                                     "A quantidade deve ser um valor numérico!")
        i = busca_indice(vinhos_num, escolha)
        preco = precos[i]
        quantidades_vinhos[i] += quantidade

        total += quantidade*preco

        continuar = obriga_opcao(f"Você deseja continuar comprando? {'|'.join(opcoes_continuar)}\n-> ",
                                 f"Digite apenas uma das opções!",
                                 opcoes_continuar)
        if continuar == 'não':
            break

    if total > 500:
        print("Frete grátis!!")
    else:
        total += frete
        print(f"Frete: R${frete:.2f}")
    print(f"Valor total da compra: R${total:.2f}\n"
          f"Endereço de entrega: {endereco}")
    for j in range(len(vinhos)):
        print(f"{vinhos[j]}: {quantidades_vinhos[j]} unidades")
    print("\nObrigado pela sua compra! Aproveite seu vinho e volte sempre!\n"
          "Atenciosamente, Equipe Agnello :)")