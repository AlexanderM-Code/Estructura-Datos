def operacionesBasicas(a,b,operacion):
    if operacion == '+':
        return a + b 
    elif operacion == '-':
        return a - b 
    elif operacion == '*':
        return a * b 
    elif operacion == '/':
        if b == 0:
            return "Error: Division por cero no es posible"
        else:
            return a / b
    else:
        return "Operacion no reconocida"

while True:
    print("-"*100)
    a = float(input("Digite el primer numero: "))
    b = float(input("Digite el segundo numero: "))
    operacion = input("Introduce la operacion (suma, resta, multiplicacion, division): ")

    resultado = operacionesBasicas(a,b, operacion)
    print("El resultado de la" , operacion, " es: ", resultado)