#leer un numero entero de dos digitos y determinar si es primo
num = int(input("ingrese numero: "))
cont = 0

if(len(str(num))==2):
    for i in range(1, num + 1):
        if(num % i == 0):
            cont += 1

if(cont == 2):
    print("El numero es primo")
else:
    print(f"el numero no es primo tiene {cont} divisores")