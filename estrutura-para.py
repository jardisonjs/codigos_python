'''

Este codigo é uma representação que acontece na maioria das linguagens de progamação

for(contador=1; contador<=5; contador++){

}
'''

for contador in range(1,6):
    print(contador)

print("-"*40)
#2 forma de operação do for
for contador in range(10,0,-1):# o 3 parâmetro indica como os valores serão incrementados(alteração de valor)
    print(contador,end=" ")# a função end informa como os valores saerão exibidos ao final, por padrão é dados um enter(\n)