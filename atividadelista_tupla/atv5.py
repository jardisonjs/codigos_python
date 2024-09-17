numeros = []

for NU in range(5):
    numero = int(input("Informe um número: "))
    numeros.append(numero)

print("Lista completa dos números: ", numeros)

print("Os números divisíveis por 3 são:")
for NU in numeros:
    if NU %3 == 0:
        print(NU)