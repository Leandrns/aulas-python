from random import choice
import pandas as pd

'''dic = {
    "oi": ["olá", "eae", "salve"],
    "tchau": ["flw", "tmj", "noiss"]
}

resp = input("Diga oi ou tchau: ")
print(choice(dic[resp]))
'''

'''dic = {
    'chave': 'valor'
}
print(dic['chave'])

dic['nova chave'] = 'novo valor'
print(dic)

dic['chave'] = 1
print(dic)'''

'''dic = {
    'chave': 1
}

dic['chave'] = [dic['chave']]
dic['chave'].append(3)
print(dic['chave'])'''

'''numeros = {
    'pares': []
}
numeros['impares'] = []
for i in range(20):
    if i % 2 == 0:
        numeros['pares'].append(i)
    else:
        numeros['impares'].append(i)
print(pd.DataFrame(numeros))'''

'''numeros = {
    'um': '1',
    'dois': '2',
    'três': '3',
    'quatro': '4',
    'cinco': '5',
    'seis': '6',
    'sete': '7',
    'oito': '8',
    'nove': '9',
    'zero': '0'
}'''
'''numero_telefone = ''
for i in range(11):
    num = input(f"Digite o {i+1}° número do seu telefone por extenso: ")
    numero_telefone += numeros[num]
print(f"Seu número é {numero_telefone}")'''

'''tel = input("Diga seu número: ")
for key in numeros.keys():
    tel = tel.replace(key, numeros[key])
tel = tel.replace(' ', '')
print(tel)'''

formas = {
    '3': 'Triângulo',
    '4': 'Quadrado',
    '5': 'Pentagono',
    '6': 'Hexagono',
    '7': 'Heptagono',
    '8': 'Octogono'
}
lados = input("Digite uma quantidade de lados: ")
print(f"O polígono é um {formas[lados]}")
