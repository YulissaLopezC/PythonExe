#Leer un número entero de tres dígitos y determinar a cuánto es igual la suma de sus 
#dígitos.

def two_dig(num):
    dig = 0
    while num != 0 and num != -1:
        dig += 1
        num = int(num / 10)
    return dig
    
    if dig == 2:
        return True
    else:
        return False

num = int(input("Ingrese un numero: "))

while not(two_dig(num)):
    print("Oopss Ingresa numero de dos cifras BB")
    num = int(input("Ingrese un numero: "))

sum = 0

while num != 0:
    ult_dig = int(abs(num) % 10)
    sum += ult_dig
    num = int(num / 10)

print(f'la suma de los digitos es igual a {sum}')
        

