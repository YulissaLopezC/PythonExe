#Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al 
#penúltimo

def num_dig(num):
    dig = 0
    if num == 0:
        dig = 1
    while num != 0:
        dig += 1
        num = num // 10
    return dig

correcto = False
while not(correcto):
    num = int(input("Ingrese un numero "))
    if num_dig(num) == 4:
        correcto = True

pen_dig = (num % 100) // 10
sec_dig = (num // 100) % 10

if sec_dig == pen_dig:
    print("el segundo dígito es igual al penúltimo")
else:
    print("el segundo dígito no es igual al penúltimo")
    
