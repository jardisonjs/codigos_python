
ni = int(input("Digite um número inteiro: "))


somDiv = 0


for i in range(1, ni):
    if ni % i == 0:  
        somDiv += i


if somDiv == ni:
    print(f"{ni} é um número perfeito.")
else:
    print(f"{ni} não é um número perfeito.")