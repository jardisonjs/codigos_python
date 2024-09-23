VL = int(input("Informe o valor da conta: "))
PR = float(input("Informe o valor da gorjeta que irá dar ao garçom: "))

GO = VL * PR/100
VT = VL + GO

print(f"Gorjeta: {GO} \n Total: {VT} ")
