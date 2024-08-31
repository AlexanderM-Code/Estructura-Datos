def palindromo(palabra):
    palabra=palabra.replace("","").lower()
    return palabra == palabra [::-1]

while True:
    palabra = input("Introduce una palabra para verificar si es un palindromo: ")

    if palindromo(palabra):
        print("La palabra ", palabra, "es un palindromo")
    else:
        print("La palabra ", palabra, " no es un palindromo")