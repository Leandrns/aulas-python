print("Seja bem-vindo à Vinheria Agnello!")
ano_nasc = input("Diga seu ano de nascimento: \n-> ")
while not ano_nasc.isnumeric():
    print("Digite apenas números!")
    ano_nasc = input("Diga seu ano de nascimento: \n-> ")

ano_nasc = int(ano_nasc)
if 2024 - ano_nasc < 18:
    print("Você possui menos de 18 anos, não pode consumir bebidas alcoólicas!!")
else:
    endereco = input("Diga seu endereço: \n-> ")
    vinho1 = "Vinho Tinto"
    vinho2 = "Vinho Seco"
    vinho3 = "Vinho Rose"
    preco1 = 20
    preco2 = 30
    preco3 = 40
    frete = 10
    valor_total = 0
    while True:
        print(f"""
        ===== NOSSOS VINHOS ===== 
        1 - {vinho1} - R${preco1}
        2 - {vinho2} - R${preco2}
        3 - {vinho3} - R${preco3}
        4 - Sair
        """)
        opcao = input("Escolha uma das opções digitando o número correspondente: \n-> ")
        
        if opcao == '1':
            preco = preco1
        elif opcao == '2':
            preco = preco2
        elif opcao == '3':
            preco = preco3
        elif opcao == '4':
            break
        else:
            print("Digite uma das opções apresentadas!!!")
            continue
        
        quantidade = input("Digite a quantidade de garrafas: \n-> ")
        while not quantidade.isnumeric():
            print("Digite apenas números!")
            qtd = input("Digite a quantidade de garrafas: \n-> ")
        quantidade = int(quantidade)
        valor_total += preco * quantidade
        print("Retornando ao catálogo...")
    if valor_total < 100:
        valor_total += frete
    else:
        print("Frete grátis!")
    print(f"""
Valor da compra: R${valor_total}
Endereço de entrega: {endereco}
    """)