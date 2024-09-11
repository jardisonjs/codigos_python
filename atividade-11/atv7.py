
n1 = int(input("Digite o primeiro número inteiro positivo: "))
n2 = int(input("Digite o segundo número inteiro positivo: "))


totMulti = 0


for i in range(n1, n2 + 1):
    if i % 7 == 0 and i % 11 == 0:
        totMulti += 1


print(f"O total de números entre {n1} e {n2} que são múltiplos de 7 e 11 é: {totMulti}")
