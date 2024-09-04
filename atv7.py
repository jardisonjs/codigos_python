produto = int(input("informe o valor do produto:"))
ops = input("escolha uma opção: pix \n dinheiro \n debito \n cartão de credito \n duas vezes sem juros \n três vezes com juros \n Sua escolha é:")

if ops == 'pix':
    VF = produto*15/100
    TL = produto-VF
    print(f"Você recebeu {VF} reais de desconto, o valor final do produto é: {TL}")
elif ops == 'dinheiro':
    VF = produto*15/100
    TL = produto-VF
    print(f"Você recebeu {VF} reais de desconto, o valor final do produto é: {TL}")
elif ops == 'debito':
    VF = produto*15/100
    TL = produto-VF
    print(f"Você recebeu {VF} reais de desconto, o valor final do produto é: {TL}")
elif ops == 'cartão de credito':
    VF = produto*10/100
    TL = produto-VF
    print(f"Você recebeu {VF} reais de desconto, o valor final do produto é: {TL}")
elif ops == 'duas vezes':
    VF = produto/2
    print(f"O valor a pagar é: {VF}")
elif ops == 'três vezes':
    VF = produto*10/100
    TL = (produto+VF)/3
    print(f"O valor a pagar é: {TL} por parcela")





