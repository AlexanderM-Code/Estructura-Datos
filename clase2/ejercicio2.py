#Ejercicio 2

while True:
    numero = int(input("Ingrese un número (o 0 para salir): "))
    
    if numero == 0:
        break  
    
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
