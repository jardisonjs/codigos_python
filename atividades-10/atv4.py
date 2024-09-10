salario = int(input("informe um número: "))


if salario >=0 and salario <=1900:
    print(f"você esta insento de impostos")
elif salario >=1901 and salario <=2800:
    print(f"Você pagara 7.5% de imposto")
elif salario >=2801 and salario <=3700:
    print(f"Você pagara 15% de imposto")
elif salario >=3701:
    print(f"Você pagara 22.5% de imposto")