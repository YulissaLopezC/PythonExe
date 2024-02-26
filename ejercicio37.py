#Leer dos números enteros y determinar cuál es múltiplo de cuál
num = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))

if num % num2 == 0:
    print(f"El numero {num} es multiplo de {num2}")
elif num2 % num == 0:
    print(f"El numero {num2} es multiplo de {num}")
else:
    print("Los numeros no son multiplos")





