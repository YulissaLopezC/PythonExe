# Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.
has_two_dig = False
num = 0

#comprobar si tiene dos digitos
while has_two_dig == False:
    num = int(input("ingrese un numero de dos digitos: "))

    num_cop = num
    dig = 0

    while num_cop != 0:
        dig += 1
        num_cop = int(num_cop / 10)

    if dig == 2:
        has_two_dig = True

#separar los digitos
dig_1 = int(num / 10)
dig_2 = int(num % 10)

if(dig_1 == dig_2):
    print("Ambos digitos son iguales")
else:
    print("Los digitos no son iguales")
"""
num = str(num)
if(num[0] == num[1]):
    print("Ambos digitos son iguales")
else:
    print("Los digitos no son iguales")

"""