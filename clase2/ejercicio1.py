#Ejercicio 1

# Solicitar los tres números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Encontrar el número mayor
mayor = num1
if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3

# Encontrar el número menor
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

# Mostrar los resultados
print("El número mayor es:", mayor)
print("El número menor es:", menor)
