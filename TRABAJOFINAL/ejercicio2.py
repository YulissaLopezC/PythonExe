#Leer un numero entero y determinar si tiene tres digitos
num = int(input("Ingrese un numero: "))

if(num > 99 and num < 1000):
    print("el numero tiene 3 digitos")
else:
    print("el numero tiene no 3 digitos")