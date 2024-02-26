#. Leer tres números enteros y determinar si el último dígito de los tres números es igual
num = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
num3 = int(input("Ingrese un numero: "))

ult_dig_num = abs(num) % 10
ult_dig_num2 = abs(num2) % 10
ult_dig_num3 = abs(num3) % 10

print(ult_dig_num, " ", ult_dig_num2, " ", ult_dig_num3)
if ult_dig_num == ult_dig_num2 and ult_dig_num == ult_dig_num3:
    print("Los tres ultimos digitos son iguales")
else:
    print("Los tres ultimos digitos no son iguales")