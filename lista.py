animais = ["Cachorro","Gato","Ovelha"]
print(type(animais)) #exibindo o tipo da variavel

print(animais)

#Exibindo todos os itens da lista
print("+"*50)
for itens in animais:
    print(itens)

#1 etapa: atualizar dados
print("-"*50)
animais[0] = "Coelho"
print(animais)

#2 etapa: inserir dados
print("-"*50)
#forma1 - usando append
animais.append("Cavalo") #irá inserir um novo item no final da lista
print(animais)

#2 forma - usando insert
animais.insert(1, "Coral-verdadeira") # o insert precisa de 2 valors, o 1 será o indice que desejo inserir o valor. 0 2 é 0 conteudo que quero inserir na lista
print(animais)

#3 etapa: excluir dados
print("-"*50)
#1 forma - usando pop()
animais.pop() #remove o últiomo item da lista
print(animais)

#2 forma 2 usando pop() com indice
animais.pop(0) #aqui iremos escolher qual indice da lista será excluido
print(animais)

#3 forma - usando remove
animais.remove("Ovelha")# Irá remover o item pelo seu conteúdo
print(animais)