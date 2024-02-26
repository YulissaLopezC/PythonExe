def is_primo(num):
    div = 0
    for i in range(1, num + 1):
        if num % i == 0:
            div += 1

    if div == 2:
        return True
    else:
        return False
    
num = int(input("Ingrese un numero: "))
if num < 100 :
    if is_primo(num):
        print("El numero es primo")
    else:
        print("El numero no es primo")