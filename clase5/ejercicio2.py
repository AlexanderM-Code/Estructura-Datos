def multiplicacion_por_sumas(a:int,b:int)-> int :
    if a == 0:
        return 0
    return b + multiplicacion_por_sumas(a - 1 , b )

print (multiplicacion_por_sumas(4,5))