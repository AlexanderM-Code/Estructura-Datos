def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

while True:
    celsius = float(input("Introduce la temperatura en Celsius: "))
    resultado = celsius_a_fahrenheit(celsius)
    print ("Los grados" ,celsius, "equivalen a ", resultado, "grados fahrenheit")