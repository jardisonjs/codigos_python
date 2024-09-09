n1 = int(input("informe um valor: "))
n2 = int(input("informe um valor: "))
soma = 0

for nn in range(n1, n2 + 1):
    soma = soma + nn

print(f"o valor final é: {soma}")