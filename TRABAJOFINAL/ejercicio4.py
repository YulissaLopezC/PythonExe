#Leer 1 numero entero de dos digitos y determinar a cuanto es igual la suma de sus digitos
num1= int(input("Ingrese el primer numero: "))

#determinar si tienen dos digitos
if(len(str(num1))== 2):
    d1 = int(num1 / 10)
    d2 = int(num1 % 10) 
    sum = d1 + d2
    
    
print(f"la suma de los digitos es {sum}")
