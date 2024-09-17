TP = []
mes = ["Janeiro: ", "Fevereiro: ", "Março: ", "Abril: ", "Maio: ", "Junho: ", "Julho: ", "Agosto: ", "Setembro: ", "Outubro: ", "Novembro: ", "Dezembro: "]

for contador in range(12):
    Temperatura = float(input(f"Informe a temperatura média de {mes[contador]}"))
    TP.append(Temperatura)

    soma_da_tp = 0
    CT = 0

    for temperatura in TP:
        soma_da_tp += temperatura
        CT +=1  

        media_ano = soma_da_tp/CT

print(f"A média anual das temperatueas: {media_ano:.2f}")

print("As temperaturas acima da média anual são:")
for contador in range(12):
    if TP[contador] > media_ano:
        print(f"{mes[contador]}: {TP[contador]:.2f}")
