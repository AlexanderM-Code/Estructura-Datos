#Ejercicio 1

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

mayor = num1
if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print("El número mayor es:", mayor)
print("El número menor es:", menor)
