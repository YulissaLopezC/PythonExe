#Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se 
#encuentra el mayor dígito.

def num_dig(num):
    dig = 0
    while num != 0:
        dig += 1
        num = num // 10
    return dig

num1 = int(input("Ingrese un numero "))
num2 = int(input("Ingrese un numero "))
num3 = int(input("Ingrese un numero "))
may = 0
pos = 0


while num_dig(num1) != 2 or num_dig(num2) != 2 or num_dig(num3) != 2:
    print("Oops Intenta nuevamente, todos los numeros deben ser de dos digitos")
    num1 = int(input("Ingrese un numero "))
    num2 = int(input("Ingrese un numero "))
    num3 = int(input("Ingrese un numero "))

conv = str(num1) + str(num2) + str(num3)

#agregarlos un arreglo
digitos = [int(num) for num in conv]
for i in range(len(digitos)):
    if digitos[i] > may:
        may = digitos[i]
        pos = i

if pos == 0 or pos == 1:
    pos = num1
elif pos == 2 or pos == 3:
    pos = num2
elif pos == 4 or pos == 5:
    pos = num3


print(f"el mayor de los digitos esta en el numero {pos}")




