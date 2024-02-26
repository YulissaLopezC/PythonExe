#Leer dos números enteros y determinar si la diferencia entre los dos es un número par.
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

if diferencia % 2 == 0:
    print(f"La diferencia entre {may} y {men} es {diferencia} y es par")
else:
    print(f"La diferencia entre {may} y {men} es {diferencia} y no es par")