#Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.
num = int(input("Ingrese un numero de 2 digitos: "))
num_pr= num
num_dig = 0
cont = 0
#si es de dos digitos
while num_pr != 0 and num_pr != -1:
    num_pr = int(num_pr / 10)
    num_dig += 1

if num_dig == 2:
    #determinar si es primo
    for i in range(1, num + 1):
        if num % i == 0:
            cont += 1
    
    if cont == 2:
        print("El numero es primo y no es negativo")
    else:
        print("El numero no es primo", end=" ")
        if num < 0:
            print("y es negativo")
else:
    print("Ingrese un numero valido de 2 digitos")

    

