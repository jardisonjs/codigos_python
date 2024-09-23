FS = input("informe o atividade física que você praticou (caminhada(1), corrida(2) ou ciclismo(3)): ")
TP = float(input("informe quanto tempo você praticou o atividade física: "))


if FS == "1":
    caminhada = 5*TP
    print(f"Você queimou o total de {caminhada} calorias, praticando caminhada em {TP} minutos.")
elif FS == "2":
    corrida = 10*TP
    print(f"Você queimou o total de {corrida} calorias, praticando caminhada em {TP} minutos.")
elif FS == "3":
    ciclismo = 8*TP
    print(f"Você queimou o total de {ciclismo} calorias, praticando caminhada em {TP} minutos.")



