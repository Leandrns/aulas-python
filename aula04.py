'''vel = float(input("Digite a velocidade: "))
if vel <= 100:
    print("Isento.")
else:
    if vel <= 120:
        multa = 0.2 * vel
    elif vel <= 150:
        multa = 0.2 * 120 + 0.3 * vel
    else:
        multa = 0.2 * 120 + 0.3 * 150 + 0.4 * vel
    print(f"Valor da multa: R${multa:.2f}")'''

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
d = int(input("Digite o quarto número: "))
e = int(input("Digite o quinto número: "))

if a%2 == 0:
    print(f"O número {a} é par")
else:
    print(f"O número {a} é ímpar")
    
if b%2 == 0:
    print(f"O número {b} é par")
else:
    print(f"O número {b} é ímpar")
    
if c%2 == 0:
    print(f"O número {c} é par")
else:
    print(f"O número {c} é ímpar")
    
if d%2 == 0:
    print(f"O número {d} é par")
else:
    print(f"O número {d} é ímpar")
    
if e%2 == 0:
    print(f"O número {e} é par")
else:
    print(f"O número {e} é ímpar")
