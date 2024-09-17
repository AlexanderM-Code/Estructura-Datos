class Vehiculo:
    def __init__(self, marca: str, combustible: str, tipo: str, capacidad_tanque:float,nivel_combustible:float):
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo
        self.capacidad_tanque = capacidad_tanque
        self.nivel_combustible = nivel_combustible

    def encender(self):
        if self.nivel_combustible/self.capacidad_tanque < 0.10:
            print(f"Advertencia: {self.tipo} {self.marca} tiene poco combustible, necesita recargarse")
        else:
            print(f"{self.tipo} {self.marca} se ha encendido correctamente")
    def arrancar(self):
        pass
    print("-"*80)
    def __str__(self):
        return f"En {self.tipo} {self.marca} utilizamos {self.combustible}"

class Moto(Vehiculo):
    def __init__(self, marca: str, combustible: str, capacidad_tanque:float, nivel_combustible:float):
        super().__init__(marca, combustible, "Moto",capacidad_tanque,nivel_combustible)

class Carro(Vehiculo):
    def __init__(self, marca: str, combustible: str,capacidad_tanque:float, nivel_combustible:float):
        super().__init__(marca, combustible, "Carro",capacidad_tanque,nivel_combustible)

motocicleta = Moto("Honda", "Corriente", 3.0, 0.2)
mi_carro = Carro("Mazda", "Extra", 15.0, 2.0 )
print(motocicleta)
print(mi_carro)

print("-"*80)

motocicleta.encender()
mi_carro.encender()