for numero in range(1,51):
    if  (numero % 5 == 0) and (numero % 3 == 0):
        print(f"{numero} FizzBuzz")
    elif (numero % 5 == 0):
        print(f"{numero} Fizz")
    elif (numero % 3 == 0):
        print(f"{numero} Buzz")
    else:
        print(numero)