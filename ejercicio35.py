#Leer un número entero de dos dígitos, guardar cada dígito en una variable diferente y 
#luego mostrarlas en pantalla
def num_dig(num):

    num = abs(num)
    dig = 0
    while num != 0:
        dig += 1
        num = int(num / 10)
    return dig 


correcto = False
dig = 0

while not(correcto):
    num = int(input("Ingrese un numero: "))
    if num_dig(num) == 2:
        correcto = True


dig1 = int(num / 10);
dig2 = abs(num) % 10;

print(f"El primer digito es {dig1}")
print(f"El segundo digito es {dig2}")
