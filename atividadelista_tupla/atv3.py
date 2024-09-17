numeros = []
for contador in range(6):
    numeros.append(float(input("Digite um número: ")))

print("Lista de números:", numeros)

pos1, pos2 = int(input("Digite a primeira posição: ")), int(input("Digite a segunda posição: "))

num1, num2 = numeros[pos1], numeros[pos2]

operacoes = (num1 * num2, num1 + num2, num1 - num2, num1 / num2, num1 ** num2)

print("Operações:")
print(f"Produto: {operacoes[0]}")
print(f"Soma: {operacoes[1]}")
print(f"Diferença: {operacoes[2]}")
print(f"Divisão: {operacoes[3]}")
print(f"Exponenciação: {operacoes[4]}")