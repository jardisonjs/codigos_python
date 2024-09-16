import datetime

ano_da_inscri = datetime.date.today().year

while True:
    data_de_nascimento = int(input("informe sua data de nascimento: "))
    
    idade = ano_da_inscri - data_de_nascimento

    if idade >= 18:
        print("Você esta apto a se inscrever no concurso.")
        break
    else:
        print("Você não tem idade suficiente para se inscrever no concurso")