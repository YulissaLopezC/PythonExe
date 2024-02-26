#Leer dos números enteros de dos dígitos y determinar si tienen dígitos comunes
def two_digits(num):
    dig = 0
    while num != 0 and num != -1:
        dig += 1
        num = int(num / 10)
    
    if dig == 2:
        return True
    else:
        return False


print("Ingrese dos numeros de dos digitos cada uno")
num_1 = input("Ingrese el numero:  ")
num_2 = input("Ingrese el numero:  ")
dig_comun= 0

#comprueba que tiene dos digitos
while not(two_digits(int(num_1))) or not(two_digits(int(num_2))):
    print("Ingrese dos numeros de dos digitos cada uno")
    num_1 = input("Ingrese el numero:  ")
    num_2 = input("Ingrese el numero:  ")



for i in range(2):
    for j in range(2):
        if num_1[i] == num_2[j]:
           dig_comun += 1

print(f'Los numeros tiene {dig_comun} digito(s) en comun')



