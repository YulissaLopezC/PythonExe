#Leer un número entero de cuatro dígitos y determinar a cuanto es igual la suma de sus 
#dígitos

def num_dig(num):
    dig = 0
    if num == 0:
        dig = 1
    while num != 0:
        dig += 1
        num = num // 10
    return dig

correcto = False
sum = 0

while not(correcto):
    num = int(input("Ingrese un numero "))
    if num_dig(num) == 4:
        correcto = True


while num != 0:
    ult_dig = num % 10
    sum += ult_dig
    num = num // 10

print(f"La suma de los digitos del numero es igual a {sum}")