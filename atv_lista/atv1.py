lista1 = []
while True:
    elemento = input("Digite um elemento para a lista 1 (ou 'fim' para terminar): ")
    if elemento == 'fim':
        break
    lista1.append(int(elemento))

lista2 = []
while True:
    elemento = input("Digite um elemento para a lista 2 (ou 'fim' para terminar): ")
    if elemento == 'fim':
        break
    lista2.append(int(elemento))

intersecao = [elemento for elemento in lista1 if elemento in lista2]
print("Números comuns:", intersecao)