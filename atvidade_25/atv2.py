def exibir_moedas(cotacoes):
    print("Moedas disponíveis:")
    for moeda, preco in cotacoes.items():
        print(f"{moeda}: R$ {preco:.2f}")

def converter_moeda(cotacoes):
    while True:
        exibir_moedas(cotacoes)
        moeda = input("Digite a moeda para conversão (ou 'sair' para encerrar): ").strip().lower()
        
        if moeda == 'sair':
            break
        elif moeda in cotacoes:
            valor_reais = float(input("Digite o valor em reais: "))
            valor_convertido = valor_reais / cotacoes[moeda]
            print(f"Valor convertido: {valor_convertido:.2f} {moeda.upper()}")
        else:
            print("Moeda não encontrada.")

def menu_moedas():
    cotacoes = {
        'dólar': 5.25,
        'euro': 5.73,
        'libra': 6.68,
        'iene': 0.036,
        'franco suíço': 5.74
    }
    converter_moeda(cotacoes)

menu_moedas()
