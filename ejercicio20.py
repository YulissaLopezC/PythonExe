#Leer tres números enteros y mostrarlos ascendentemente
#ingreso los numero
num1 = int(input("Ingrese un numero"))
num2 = int(input("Ingrese un numero"))
num3 = int(input("Ingrese un numero"))

if num1 > num2:
    num2 , num1 = num1, num2
if num2 > num3:
    num3, num2 = num2, num3
if num1 > num3:
    num3, num1 = num1, num2

print(num1, " ", num2, " ", num3)


