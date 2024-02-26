#. Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los 
#otros.

def num_digitos(num):
    dig = 0
    while num != 0:
        dig += 1
        num = int(num / 10)
    
    return dig

len = 3
num = int(input("Ingrese un numero de 3 cifras "))
dig = num_digitos(num)

while dig != len:
    print("Oopss Ingresa numero de dos cifras BB")
    num = int(input("Ingrese un numero de 3 cifras "))
    dig = num_digitos(num)

#convierto los numeros en una lista(array)
digitos = [int(d) for d in str(num)]

for i in range(len):
    #saco el numero a dividir actual
    dividendo = digitos[i]
    #saco una lista con los otros numero menos el dividendo
    divisores = digitos[:i] + digitos[i+1:]
    if dividendo % divisores[0] == 0 and dividendo % divisores[1] == 0:
        print(f"El dígito {dividendo} es múltiplo de los otros dos.")



