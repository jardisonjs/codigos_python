# Contadores
neg = 0
sm_pstv = 0

# Receber 8 números do usuário
for i in range(8):
    nm= int(input(f"Digite o {i+1} número: "))
    
    if nm< 0:
        neg += 1
    else:
        sm_pstv += nm

# Exibir os resultados
print(f"Quantidade de números negativos: {neg}")
print(f"Soma dos números positivos: {sm_pstv}")