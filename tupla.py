objetos = ('Lapis','Borracha','Caderno')
print(objetos[1]) #irei exibir o item na posição 1, ou seja segunda posição, uma vez que toda coleção começa na posição zero.

print(type(objetos)) #irá mostra o tipo da variável

print(objetos) #exibir todos os itens de uma só vez

print("-"*50)

for item in range(0,3):
    print(objetos[item],end=", ") # exibindo todos os itens da tlupa

# exibindo todos os itens da tupla sem a função range
print("")
print("-"*50)
for elementos in objetos:
    print(elementos)

# iremos tentar alterar o conteúdo da tupla
objetos[0] = "caneta"