import random
import string

def generar_contraseña(longitud):
    caracteres=string.ascii_letters + string.digits + string.punctuation
    contraseña =''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

while True:
    longitud = int(input("Introduce la longitud de la contraseña que deseas generar: "))
    contraseña_generada = generar_contraseña(longitud)
    print("La contraseña generada es: ", contraseña_generada)
