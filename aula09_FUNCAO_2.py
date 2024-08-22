def forca_opcao(msg, lista_opcoes):
    possibilidades = '\n'.join(lista_opcoes)
    possibilidades =  '\n'+possibilidades+'\n'
    msg += "\n-> "
    opcao = input(possibilidades+msg)
    while opcao not in lista_opcoes:
        print(f"Opção inválida! Somenta essas:{possibilidades}")
        opcao = input(msg)
    return opcao

'''carros = ['Celta', 'Virtus', 'Camaro', 'Audi R8']
escolha_carro = forca_opcao("Escolha um carro: ", carros)
print(f"Você escolheu o {escolha_carro}")'''
