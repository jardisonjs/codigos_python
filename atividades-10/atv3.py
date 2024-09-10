idade = int(input("informe um número: "))

if idade <=12:
    print(f" você é criança")
elif idade >=12 and idade <=18:
    print(f"você é adolecente")
elif idade >=18 and idade <=60:
    print(f"você é adulto")
elif idade >=60:
    print(f"você é idoso")