# Leer tres números enteros y determina si el penúltimo dígito de los tres números es 
#igual.

def pen_dig(num):
    ult_digs = abs(num) % 100
    pen_dig = int(ult_digs / 10)
    return pen_dig

num = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
num3 = int(input("Ingrese un numero: "))

if pen_dig(num) == pen_dig(num2) == pen_dig(num3):
    print("Los tres penultimos digitos son iguales")
else:
    print("Los tres penultimos digitos no son iguales")

