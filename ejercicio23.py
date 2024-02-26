#Leer un número entero de tres dígitos y determinar cuántos dígitos primos tiene

#funcion de digitos 
def num_dig(num):
    dig = 0
    if num == 0:
        dig = 1
    while num != 0 and num != -1:
        dig += 1
        num = int(num / 10)
    return dig

#funcion de primos
def is_primo(dig):
    div = 0
    for i in range(1, dig + 1):
        if dig % i == 0:
            div += 1
    
    if div == 2:
        return True

    return False


#ingresar el numero
correcto = False
prim = 0
while not(correcto):
    num = abs(int(input("Ingrese un numero ")))
    if num_dig(num) == 3:
        correcto = True

while num != 0:
    #sacar el ult dig
    ult_dig = num % 10
    if is_primo(ult_dig):
        prim += 1
    num = num // 10

print(f"el numero tiene {prim} digito(s) primos")
    




