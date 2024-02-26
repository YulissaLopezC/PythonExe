#Leer un número entero de cinco dígitos y determinar si es un número capicúo. Ej. 15651,
#59895.

def num_dig(num):
    dig = 0
    if num == 0:
        dig = 1
    while num != 0 and num != -1:
        dig += 1
        num = int(num / 10)
    return dig

correcto = False
while not(correcto):
    num = int(input("Ingrese un numero "))
    if num_dig(num) == 5:
        correcto = True

num = str(num)
long = len(num) - 1
dif = 0

for i in range(long):
    if num[i] != num[long - i]:
        dif = 1

if dif != 0:
     print("El numero no es capicuo")
else:
     print("El numero es capicuo")
    

        
