""". Leer dos números enteros y determinar si la diferencia entre los dos es un número 
divisor exacto de alguno de los dos números."""

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

if num % diferencia == 0 or num2 % diferencia == 0:
    print(f" la diferencia entre los dos es {diferencia} y es un número divisor exacto de alguno de los dos números")
else:
    print(f" la diferencia entre los dos es {diferencia} y no un número divisor exacto de alguno de los dos números")

