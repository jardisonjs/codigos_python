idades18 = 0

for contador in range(1,6):
    idadedd = int(input(f"informe sua idade {contador}: "))
    if idadedd >= 18:
        idades18 += 1
        
print(f"idades maiores de 18 anos {idades18}: ")