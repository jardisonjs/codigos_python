ano = int(input("diga um ano: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f"o ano {ano} é bissexto.")
else:
    print(f"o ano {ano} não é bissexto.")