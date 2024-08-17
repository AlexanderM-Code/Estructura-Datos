# Ejercicio 3 

# Solicitar los números al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Solicitar la operación al usuario
operacion = input("Ingrese la operación a realizar (+, -, x, /): ")

# Realizar la operación y mostrar el resultado
if operacion == "+":
    resultado = numero1 + numero2
    print(f"{numero1} + {numero2} = {resultado}")
elif operacion == "-":
    resultado = numero1 - numero2
    print(f"{numero1} - {numero2} = {resultado}")
elif operacion == "x":
    resultado = numero1 * numero2
    print(f"{numero1} x {numero2} = {resultado}")
elif operacion == "/":
    if numero2 == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        resultado = numero1 / numero2
        print(f"{numero1} / {numero2} = {resultado}")
else:
    print("Operación inválida.")
