print("1 hora = 50 reais, e droba a cada hora.")
TB = int(input("informe suas horas trabalhadas: "))

if TB >= 40:
    CL = TB*50
    BS = CL/100 * 50
    TL = CL+BS
    print(f"você vai receber {TL} reais de horas trabalhadas")
else:
    CL = TB*50
    print(f"você vai receber {CL} reais de horas trabalhadas")