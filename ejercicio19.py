#Leer tres números enteros y determinar cuál es el mayor. Usar solamente dos variables.
may = 0

for i in range(3):
    num = int(input("Ingrese un numero "))
    if num > may:
        may = num
    # num = int(input("Ingrese un numero "))
print(f'el numero mayor de los 3 ingresados es {may}')
