import random

Nsecreto = random.randint(1,100)
tentativas = 5

print("Você deve adivinhar o número secreto entre 1 e 100, e você so tem 5 tentativas.")

while tentativas > 0:
    adivinha = int(input("qual é o número secreto: "))

    if adivinha < Nsecreto:
        print("O número secreto é maior.")
    elif adivinha > Nsecreto:
        print("O número secreto é menor")
    else:
        print("Parabéns! Você adivinhou o número secreto!")
        break

    tentativas -= 1
    print(f"tentativas restantes: {tentativas}")

    if tentativas == 0:
        print(f"Você perdeu o jogo de adivinhar. O número secreto era {Nsecreto}")