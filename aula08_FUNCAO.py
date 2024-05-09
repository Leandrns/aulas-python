'''def expo(x,y):
    return (x**y)

print(expo(9,2))
print(expo(8,4))'''

'''def voto(nome,idade):
    if idade < 16:
        return (False)
    else:
        return (True)

eleitor = input("Nome: ")
idade = int(input("Idade: "))

if voto(eleitor,idade):
    print("Pode votar")
else:
    print("Não pode votar")'''

# Função que retorna o maior valor de uma lista
def maior(x):
    z = x[0] # z, que representa o número maior, recebe o primeiro elemento da lista para iniciar as comparações
    for i in x:
        if i > z:
            z = i
    return (z)

y = [2, -5, 8, -1]
print(maior(y))

t = [8, 100, -9, 101]
print(maior(t))
