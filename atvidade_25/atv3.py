def converter_temperatura(celsius, escala):
    if escala == 'f':
        return (9/5) * celsius + 32
    elif escala == 'k':
        return celsius + 273.15

def menu_temperatura():
    while True:
        celsius = float(input("Digite a temperatura em Celsius (ou um número negativo para sair): "))
        if celsius < 0:
            break
        escala = input("Para qual escala você deseja converter? (f - Fahrenheit / k - Kelvin): ").strip().lower()
        temperatura_convertida = converter_temperatura(celsius, escala)
        if escala == 'f':
            print(f"{celsius:.2f} °C é igual a {temperatura_convertida:.2f} °F")
        elif escala == 'k':
            print(f"{celsius:.2f} °C é igual a {temperatura_convertida:.2f} K")
        else:
            print("Escala inválida.")

menu_temperatura()