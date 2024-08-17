# Ejercicio 4 

peso = int(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Se encuentra en bajo peso")
elif imc < 25:
    print("Se encuentra en un peso saludable")
elif imc < 30:
    print("Se encuentra en sobrepeso")
elif imc < 35:
    print("Se encuentra en obesidad I")
elif imc < 40:
    print("Se encuentra en obesidad II")
else:
    print("Se encuentra en obesidad III")

print("Tu índice de masa corporal es:", imc)
