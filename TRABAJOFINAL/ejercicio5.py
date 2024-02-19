#Leer un numero entero de dos digitoa y determinar si sus digitos son pares
num = int(input("Ingrese un numero: "))

dig2= num % 10
dig1 = int(num / 10)

if(dig2 % 2 == 0 and dig1 % 2 == 0):
    print("Ambos digitos son pares")
else:
    print("uno o ambos digitos son impares")
    
    