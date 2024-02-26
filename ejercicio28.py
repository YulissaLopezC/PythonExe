#Leer un número entero menor que 50 y positivo y determinar si es un número primo.
correcto = False
div = 0
while not(correcto):
    num = int(input("Ingrese un numero positivo y menor que 50: "))
    if num >= 0 and num <= 50:
        correcto = True

for i in range(1, num + 1):
    if num % i == 0:
        div += 1

if div == 2:
    print(f"{num} es primo.")
else:
    print(f"{num} no es primo.")

    