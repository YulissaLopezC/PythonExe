#leer un numero entero y determinar si un es un numero terminado en 4
num = int(input("Ingrese un numero"))
if(num % 10 == 4):
    print("el numero termina en 4")
else:
    print("el numero no termina en 4")