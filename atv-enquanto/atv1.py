
while True :
    vl1 = int(input("Informe um valor: "))

    if vl1 <0:
        print("Não foi possivel calcular")
        break
    elif vl1 >100:
        print("O limite foi excedido")
    elif vl1 >10:
        RS = vl1*vl1
        print(f"O quadrado de {vl1} é: {RS}")
    elif vl1 >5:
        RS = vl1*vl1*vl1
        print(f"O cubo de {vl1} é: {RS}")
    else:
        print(vl1)