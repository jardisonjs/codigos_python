Num = []

while True:
    vl = int(input("Digite um número: "))

    if vl < 0:
        break
    else:
        Num.append(vl)
print(Num)

for contador in Num:
    if contador  % 2 == 0:
        Num.remove(contador)

print(Num)
 

   

  

