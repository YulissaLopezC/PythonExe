#. Leer un número entero de tres dígitos y determinar si al menos dos de sus tres dígitos 
# son iguales.

def num_digitos(num):
    dig = 0
    while num != 0 and num != -1:
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

# ult_dig = int(num % 10)
# print(ult_dig)
# temp = int(num / 10)
# print(temp)
# sec_dig = int(temp % 10)
# print(sec_dig)
# prm_dig = int(temp / 10)
# print(prm_dig)

num = str(num)
par = 0
for i in range(len):
    for j in range (i + 1, len):
        #print(num[i], " ", num[j])
        if num[i] == num[j]:
            par += 1
if par != 0:
    print("El numero tiene al menos dos digitos iguales")
else:
    print("El numero no tiene al digitos iguales")
         