""". Leer un número entero de 2 dígitos y si es par mostrar en pantalla la suma de sus 
dígitos, si es primo y menor que 10 mostrar en pantalla su último dígito y si es múltiplo 
de 5 y menor que 30 mostrar en pantalla el primer dígito"""

#funcion # digitos
def num_dig(num):
    dig = 0
    while num != 0:
        dig += 1
        num = int(num / 10)
    return dig

#funcion par
def sum_dig(num):
    sum = 0
    while num != 0:
        ult_dig = num % 10
        sum += ult_dig
        num = int(num / 10)
    print(sum)
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

#funcion es multiplo de 5 y menor que 30
def is_mult_cinco(num):
    if num % 5 == 0 and num < 30:
        return True
    else:
        return False

correcto = False
while not(correcto):
    num = int(input("Ingrese un numero "))
    if num_dig(num) == 2:
        correcto = True
num = abs(num)

if num % 2 == 0:
    print("la suma de sus digitos es: " , end="")
    sum_dig(num)

if is_primo(num) and num > 10:
    ult_dig = num % 10
    print(f"Su ultimo digito es {ult_dig}")

if is_mult_cinco(num):
    prim_dig = num // 10
    print(f"Su primer digito es {prim_dig}")
