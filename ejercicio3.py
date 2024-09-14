class Vehiculo:
    def __init__ ( self, marca:str,combustible:str):
        self.marca = marca
        self.combustible = combustible
    def encender (self):
        pass
    def arrancar (self):
        pass
    def __str__(self):
        return f"En el vehiculo {self.marca} utilizamos {self.combustible}"
carro = Vehiculo("Toyota", "Corriente")
print(carro)

class Moto ( Vehiculo):
    def __init__(self, marca: str, combustible: str):
        super().__init__(marca, combustible)
class Carro ( Vehiculo):
    def __init__(self, marca: str, combustible: str):
        super().__init__(marca, combustible)
motocicleta = Moto ("Honda", "Corriente")
mi_carro = Carro ("Mazda", "Extra")

print(motocicleta)
print(mi_carro)