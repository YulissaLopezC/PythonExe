#Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.
def num_digitos(num):
    dig = 0
    
    while num != 0 and num != -1:
        dig += 1
        num = int(num / 10)
    return dig

len = 3
num = abs(int(input("Ingrese un numero de 3 cifras ")))
dig = num_digitos(num)

while dig != len:
    print("Oopss Ingresa numero de dos cifras BB")
    num = int(input("Ingrese un numero de 3 cifras "))
    dig = num_digitos(num)

num= str(num)
may = int(num[0])
pos = 0

for i in range(1, len):
    if int(num[i]) > may:
        pos = i
        may = int(num[i])

print(f'el numero mayor es {may} se encuentra en la posicion {pos + 1}')

