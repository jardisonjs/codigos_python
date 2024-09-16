#1 formar de utilizar white - semelhante ao For

contador = 1

while contador <= 5:
    print(contador)
    contador = contador+1 # é o mesmo que conatador +=1

print("="*40)
#2 forma de utilizar enquanto - loop condicional normal

valor  = 0 

while valor >=0:
    valor = int(input("informe um valor qualquer digite um valor negativo para terminar: "))

    print(f"Vocé digitou {valor}")

print("="*40)

# 3 forma de utilizar o enquanto - semelhante a estrutura faça..enquanto
while True:
    senha = input("informe sua senha: ")
    if senha == "123":
        print("Parabéns, senha correta")
        break # forma de encerrar o loop
    else:
        print("Senha não conferem, tente novamente")