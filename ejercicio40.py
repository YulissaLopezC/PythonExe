""". Leer dos números enteros y si la diferencia entre los dos es menor o igual a 10 entonces
mostrar en pantalla todos los enteros comprendidos entre el menor y el mayor de los 
números leídos."""

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
if diferencia <= 10 :
    for i in range(men, may + 1):
        print(i)

