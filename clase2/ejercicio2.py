#Ejercicio 2

# Solicitar números al usuario - inicio del bucle 
while True:
    numero = int(input("Ingrese un número (o 0 para salir): "))
    
    if numero == 0:
        break  # Salir del bucle si el usuario ingresa 0
    
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
