"""Leer un número entero de 4 dígitos y determinar si el primer dígito es múltiplo de alguno 
de los otros dígitos."""

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
    if num_dig(num) == 4:
        correcto = True
num = abs(num)

prim_dig = num // 1000
while num != prim_dig:
    #sacar el ult dig
    ult_dig = num % 10
    if prim_dig % ult_dig == 0:
        print(f"{prim_dig} es multiplo de {ult_dig}") 
    num = num // 10
    