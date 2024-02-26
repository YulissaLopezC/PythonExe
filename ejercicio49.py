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

ult_dig = num % 10
if num % 4 == 0:
    if is_primo(ult_dig):
        print("El ultimo digito es primo")
    else:
        print("ultimo digito no es primo")