#Leer un número entero de cuatro dígitos y determinar cuántos dígitos pares tiene
def num_dig(num):
    dig = 0
    if num == 0:
        dig = 1
    while num != 0:
        dig += 1
        num = num // 10
    return dig

correcto = False
par = 0


while not(correcto):
    num = int(input("Ingrese un numero "))
    if num_dig(num) == 4:
        correcto = True

while num != 0:
    ult_dig = num % 10
    if ult_dig % 2 == 0:
        par += 1
    num = num // 10

print(f"el numero tiene {par} digitos pares")