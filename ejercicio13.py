#. Leer dos números enteros de dos dígitos y determinar si la suma de los dos números 
#origina un número par

#funcion que dice si un numero tiene 2 digitos
def two_digits(num):
    dig = 0
    while num != 0:
        dig += 1
        num = int(num / 10)
    
    if dig == 2:
        return True
    else:
        return False

correct = False
num_1 = 0
num_2 = 0

while not(correct):
    num_1 = int(input("Ingrese en primer numero "))
    num_2= int(input("Ingrese en segundo numero "))

    if two_digits(num_1) and two_digits(num_2):
        correct = True

sum = num_1 + num_2
if sum % 2 == 0 :
    print(f'la suma de {num_1} + {num_2} = {sum} es par')
else:
    print(f'la suma de {num_1} + {num_2} = {sum} No es par')