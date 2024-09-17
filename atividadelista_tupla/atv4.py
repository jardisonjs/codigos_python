lista = [1, 2, 3, 4, 5, 3, 6, 7, 8, 3]

contador = 0
indices_3 = []
for cu in lista:  
    if lista[contador] == 3:
        indices_3.append(contador)
    contador += 1

if indices_3:
    print("Elementos iguais a 3 encontrados nas posições:", indices_3)
else:
    print("Nenhum elemento igual a 3 encontrado na lista.")