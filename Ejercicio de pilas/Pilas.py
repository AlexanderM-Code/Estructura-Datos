class Pila:
    def __init__(self):
        self.pila = []

    def agregar_a_la_pila(self, elemento):
        self.pila.append(elemento)

    def eliminar_de_la_pila(self):
        if not self.es_vacia():
            return self.pila.pop()
        else:
            print("Error: La pila está vacía.")
            return None

    def es_vacia(self):
        return len(self.pila) == 0

    def cima_de_la_pila(self):
        if not self.es_vacia():
            return self.pila[-1]
        else:
            print("Error: La pila está vacía.")
            return None

pila = Pila()
pila.agregar_a_la_pila("libro 1")
pila.agregar_a_la_pila("libro 2")
pila.agregar_a_la_pila("libro 3")

print(pila.cima_de_la_pila())      
print(pila.eliminar_de_la_pila())  
print(pila.cima_de_la_pila())      
print(pila.es_vacia()) 



