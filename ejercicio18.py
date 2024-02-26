#. Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los 
#otros.

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

#separo los digitos
dig1 = num // 100;
print(dig1)
dig2 = (num // 10) % 10
print(dig2)
dig3 = num % 10
print(dig3)

if dig1 % dig2 == 0 and dig1 % dig3 == 0:
    print(f"El dígito {dig1} es múltiplo de los otros dos.")
elif dig2 % dig1 == 0 and dig2 % dig3 == 0:
    print(f"El dígito {dig2} es múltiplo de los otros dos.")
elif dig3 % dig1 == 0 and dig3 % dig2 == 0:
    print(f"El dígito {dig3} es múltiplo de los otros dos.")
else:
    print("Ningún dígito es múltiplo de los otros dos.")






    



