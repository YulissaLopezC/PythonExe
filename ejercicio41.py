"""Leer dos números enteros y determinar si la diferencia entre los dos es un número 
primo"""

num = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))

may = 0
men = 0
diferencia = 0
if num > num2:
    may , men = num , num2
else:
     may , men = num2 , num

diferencia = may - men
div = 0
for i in range (1, diferencia + 1):
    if diferencia % i == 0:
        div += 1

if div == 2:
    print(f"La diferencia entre {may} y {men} es {diferencia} y es un numero primo")
else:
    print(f"La diferencia entre {may} y {men} es {diferencia} y no es un numero primo")
