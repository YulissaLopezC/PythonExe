#Leer un número entero y determinar si termina en 7
num = int(input("Ingrese un numero "))
ult_dig = num % 10
print(ult_dig)
if ult_dig == 7 :
    print("El numero termina en 7")
else:
    print("El numero no termina en 7")