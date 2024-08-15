'''media = 0
for i in range(7):
    nota = input(f"Diga a {i+1}ª nota: ")
    while not nota.isnumeric():
        print("")
        nota = input(f"Diga a {i + 1}ª nota: ")
    nota = int(nota)
    media += nota
media /= 7
print(media)'''

'''lista = [2, 125, 454, 12, 84, 96, 87]
for i in range(len(lista)):
    lista[i] = 1
print(lista)
'''

'''lista = []
for i in range(10):
    num = input(f"Digite o {i+1}º número: ")
    while not num.isnumeric():
        print("Não é um número")
        num = input(f"Digite o {i + 1}º número: ")
    lista.append(int(num))
print(lista)
pares = 0
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        pares += 1
print(f"Quantidade de pares: {pares}")'''
