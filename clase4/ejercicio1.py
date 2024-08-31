def calculoFactorial (numero:int) -> str|int:
    resultado = 1 
    if numero < 0:
        return "No se pueden valores negativos"
    elif numero == 0:
        return 1 
    for n in range(1,numero+1):
        resultado = resultado*n
    return resultado

while True:   
    factorial = calculoFactorial(int(input("Ingrese un numero para calcular su factorial: ")))
    print("El resultado es: ", factorial, )



