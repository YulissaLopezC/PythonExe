# Leer un número entero de 4 dígitos y determinar si tiene mas dígitos pares o impares
def num_dig(num):

    num = abs(num)
    dig = 0
    while num != 0:
        dig += 1
        num = int(num / 10)
    return dig 

correcto = False
par = 0
impar = 0

while not(correcto):
    num = int(input("Ingrese un numero: "))
    if num_dig(num) == 4:
        correcto = True

num = abs(num)
while num != 0:
    ult_dig = num % 10
    if ult_dig % 2 == 0:
        par += 1
    else:
        impar += 1
    num = int(num / 10)

print(f"par {par} y impar {impar}")

if par > impar:
    print("El numero tiene mas digitos pares que impares")
elif impar > par:
    print("El numero tiene mas digitos impares que pares")
else:
    print("El numero tiene igual numero de digitos pares que impares")


