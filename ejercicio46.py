#funcion # digitos
def num_dig(num):
    dig = 0
    while num != 0:
        dig += 1
        num = int(num / 10)
    return dig

def sum_dig(num):
    sum = 0
    while num != 0:
        ult_dig = num % 10
        sum += ult_dig
        num //=10
    return sum

correcto = False
while not(correcto):
    num = int(input("Ingrese un numero "))
    if num_dig(num) == 2:
        correcto = True
num = abs(num)

ult_dig = int(num) % 10

if ult_dig == 1:
    print("Su primer digito es: ", int(num / 10))

if ult_dig == 2:
    suma = sum_dig(num)
    print("La suma de sus digitos  ", suma)

if ult_dig == 3:
     print("Su primer digito es: ", int(num / 10), "y su ultimo digito", int(num % 10) )