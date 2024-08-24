print("-"*50)
print("Bienvenido a la fiesta")

cupo_maximo = 10
cupo_actual = 0 
boletos_validos = ["boleto1" , "boleto2" , "boleto3" , "boleto4" , "boleto5" , "boleto6" , "boleto7" , "boleto8" , "boleto9" , "boleto10"] 

while cupo_actual < cupo_maximo:
    nombre = input("Cual es tu nombre: ")
    boleto = input("Ingrese el numero de boleto: ")
    if boleto in boletos_validos:
        cupo_actual += 1 
        print("Ingreso permitido" , nombre ) 
        print("Cupos restantes: {}".format(len(boletos_validos)-cupo_actual))
    else:
        print("Ingreso no permitido" , nombre)
    print("-"*50)

print("No se permite mas ingresos el cupo esta lleno")