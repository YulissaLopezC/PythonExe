#Leer un número entero de dos dígitos y determinar si sus dos dígitos son primos

#ingresar el numero entero de dos digitos
num = int(input("Ingrese un numero de dos digitos: "))
num_dig_primos = 0
has_two_dig = False

while has_two_dig == False:
    #contar el numero de digitos
    num_cop = num
    dig = 0
    #contar el numero de digitos
    while num_cop != 0 and num_cop != -1:
        dig += 1
        num_cop = int(num_cop / 10)
    
    if dig == 2:
        has_two_dig = True
    else:
        num = int(input("Ingrese un numero de dos digitos: "))


#separa y revisa si son primos
while num != 0:
    #saco el ultimo digito
    ult_dig= int(abs(num) % 10) #5
    #probar si es primo
    cont = 0
    for i in range(1, ult_dig + 1):
        if(ult_dig % i == 0):
            cont += 1
    
    if cont == 2:
        num_dig_primos += 1

    num = int(num / 10) #2


if num_dig_primos == 2:
    print("Ambos digitos son primos")
else:
    print("uno o ningun digito son primos")


    



