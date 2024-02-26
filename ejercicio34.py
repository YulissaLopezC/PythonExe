#Leer un número entero menor que mil y determinar cuántos dígitos tiene

num = int(input("Ingrese un numero menor que 1000: "))
dig = 0
while num >= 1000:
    print("Oopss intenta otra vez")
    num = int(input("Ingrese un numero menor que 1000: "))

while num != 0:
    dig += 1
    num = int(num / 10)

print(f"el numero tiene {dig} digito(s)")

