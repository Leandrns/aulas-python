'''lista = [1,2,4,5,6]
while True:
    try:
        i = int(input("Diga um número: "))
        elemento = lista[i]
    except ValueError:
        print("Era pra ser um número!")

    except IndexError:
        print("Esse indice não existe")

    except Exception as e:
        print(e)

    else:
        print(elemento)
        break'''

'''opcoes = ['a', 'b', 'c']
while True:
    try:
        opcao = input(f"Diga uma dessas opções: {opcoes}\n-> ")
        if opcao not in opcoes:
            raise
    except:
        print("Opção inválida")'''

'''dic = {
    "chave1": [1,2,3,4],
    "chave2": [5,6,7,8]
}
while True:
    try:
        chave = input(f"Diga uma chave: {dic.keys()}\n-> ")
        key = dic[chave]
        i = int(input("Diga um índice: "))
        index = dic[chave][i]
    except KeyError:
        print("Essa chave não existe!")
    except ValueError:
        print("Precisa ser um número!")
    except IndexError:
        print(f"Esse índice não existe! Somente de 0 a {len(dic[chave])-1}")
    else:
        print(dic[chave][i])'''

'''while True:
    try:
        flag1 = "primeiro"
        flag2 = "inteiro"
        a = int(input("Diga um número: "))
        flag1 = "segundo"
        flag2 = "float"
        b = float(input("Diga um número: "))
        print(a/b)
    except ValueError:
        print(f"O {flag1} número tem que ser {flag2}")
    except ZeroDivisionError:
        print("O segundo número não pode ser zero")'''