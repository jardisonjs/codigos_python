n = int(input("informe um número: "))


for nn in range(1, n + 1):
    if n % nn == 0:
        print(nn)