import time
def contador(segundos): 
    
    for jj in range (segundos,0,-1):
        print(jj)
        time.sleep(1)


segundos = int(input("INFORME A QUNATIDADE DE SEGUNDOS: "))

print(contador(segundos))