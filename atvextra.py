itens = []
# preenchendo a lista
while True:
    valor = int(input("informe um valor numérico: "))
    if valor == 0:
        break
    else:
        itens.append(valor)
print(itens)

#pecorrer minha lista
for contador in itens:
    if contador == 3:
        itens.remove(contador)
print(itens)
