import random


cont = [0] * 6


for _ in range(10):
    lanc = random.randint(1, 6)
    cont[lanc- 1] += 1


for i in range(6):
    print(f"Valor {i + 1}: {cont[i]} vezes")