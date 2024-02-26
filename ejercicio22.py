#Leer un número entero de tres dígitos y determinar si el primer dígito es igual al último

def num_dig(num):
    dig = 0
    while num != 0 and num != -1:
        dig += 1
        num = int(num / 10)
    return dig

num = 0
while num_dig(num) != 3:
    num = int(input("Ingrese un numero de 3 cifras: "))

#separar el 1er y el ultimo digito
prm_dig = num // 100
ult_dig = num % 10

if prm_dig == ult_dig:
    print("el primer dígito es igual al último ")
else:
    print("el primer dígito no es igual al último")
