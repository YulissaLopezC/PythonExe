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

#funcion primo
def is_primo(num):
    div = 0
    for i in range(1, num + 1):
        if num % i == 0:
            div += 1

    if div == 2:
        return True
    else:
        return False

correcto = False
while not(correcto):
    num = int(input("Ingrese un numero "))
    num2 = int(input("Ingrese un numero "))
    if num_dig(num) == 2 and num_dig(num2):
        correcto = True
num = abs(num)

may = 0
men = 0
diferencia = 0
if num > num2:
    may , men = num , num2
else:
     may , men = num2 , num

diferencia = may - men

if diferencia % 2 == 0:
    sum = sum_dig(num) + sum_dig(num2)
    print(sum)

if is_primo(diferencia) and diferencia < 10:
    producto = num * num2
    print("producto ", producto)

if diferencia % 10 == 4:
    num = str(num)
    num2 = str(num2)

    for i in range(len(num)):
        print(num[i], " ", num2[i])
    





