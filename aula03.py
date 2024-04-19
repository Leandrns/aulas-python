'''
#ATIVIDADE - Cálculo Imposto de Renda
salario = float(input("Digite o seu salário: "))
if salario <= 1903.98:
    print(f"Você é isento de desconto.")
    sal_final = salario
    print(f"Seu salário final é: R${sal_final}")

elif salario <= 2826.65:
    desconto = salario * 0.075
    print(f"O desconto é de R${desconto:.2f}.")
    sal_final = salario - desconto
    print(f"Seu salário final é: R${sal_final:.2f}")

elif salario <= 3751.05:
    desconto = salario * 0.15
    print(f"O desconto é de R${desconto:.2f}.")
    sal_final = salario - desconto
    print(f"Seu salário final é: R${sal_final:.2f}")

elif salario <= 4664.68:
    desconto = salario * 0.225
    print(f"O desconto é de R${desconto:.2f}.")
    sal_final = salario - desconto
    print(f"Seu salário final é: R${sal_final:.2f}")

else:
    desconto = salario * 0.275
    print(f"O desconto é de R${desconto:.2f}.")
    sal_final = salario - desconto
    print(f"Seu salário final é: R${sal_final:.2f}")
'''

#ATIVIDADE - Cálculo Imposto de Renda - C O R R I G I D O
salario = float(input("Digite o seu salário: "))
if salario <= 1903.98:
    aliquota = 0
elif salario <= 2826.65:
    aliquota = 0.075
elif salario <= 3751.05:
    aliquota = 0.15
elif salario <= 4664.68:
    aliquota = 0.225
else:
    aliquota = 0.275

desconto = salario * aliquota
print(f"O desconto é de R${desconto:.2f}.")
sal_final = salario - desconto
print(f"Seu salário final é: R${sal_final:.2f}")
