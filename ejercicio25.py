#Leer un número entero de tres dígitos y determinar si alguno de sus dígitos es igual a la 
#suma de los otros dos
def num_dig(num):
    dig = 0
    if num == 0:
        dig = 1
    while num != 0 and num != -1:
        dig += 1
        num = int(num / 10)
    return dig

correcto = False
par = 0

while not(correcto):
    num = int(input("Ingrese un numero "))
    if num_dig(num) == 3:
        correcto = True

#lista de los digitos del numero
digitos = [int(d) for d in str(num)]

for i in range(3):
    res = digitos[i]
    sumad = digitos[:i] + digitos[i + 1:]
    if sumad[0] + sumad[1] == res:
        print(f"la suma de {sumad[0]} y {sumad[1]} es igual al digito en la {i + 1} posicion")