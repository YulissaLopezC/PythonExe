#Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de 
#todos los dígitos.

#funcion que determina se son de dos digitos 
def two_digits(num):
    dig = 0
    while num != 0 and num != -1:
        dig += 1
        num = int(num / 10)
    
    if dig == 2:
        return True
    else:
        return False

#funcion que determina la suma de los digitos
def sum_dig(num):
    sum = 0
    while num != 0 and num != -1:
        ult_dig = int(abs(num) % 10) #el ultimo digito 3
        sum += ult_dig
        num = int(num / 10)# 2
    return(sum)


num_1 = 0
num_2 = 0

correct = False
while not(correct):
    num_1 = int(input("Ingrese un numero de dos cifras: "))
    num_2 = int(input("Ingrese un numero de dos cifras: "))

    if two_digits(num_1) and two_digits(num_2):
        correct = True
    else:
        print("Oopss Ingresa numeros de dos digitos BB")

suma = sum_dig(num_1) + sum_dig(num_2)
print(f'la suma de los digitos de {num_1} y los digitos de {num_2} es igual a {suma}')



        

