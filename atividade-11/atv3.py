
med = 33.5


acima_ou_igual_med = 0
abx_med = 0

for i in range(0,7):
    temp = float(input(f"Digite a {i+1} temperatura: "))


    if temp >= med:
        acima_ou_igual_med += 1
    else:
        abx_med += 1


print(f"Quantidade de temperaturas iguais ou acima da média ({med}): {acima_ou_igual_med}")
print(f"Quantidade de temperaturas abaixo da média ({med}): {abx_med}")