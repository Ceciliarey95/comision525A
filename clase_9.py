## POO

class Coche:

    ruedas = 4

    # Método constructor
    
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f"Marca {self.marca}, modelo: {self.modelo}, color: {self.color}\n Cantidad de ruedas : {self.ruedas}"
        
    # Método de instancia
    def acelerar(self):
        print(f"El {self.marca} está acelerando")

    # Método de CLASE
    @classmethod
    def incrementar_ruedas(cls):
        cls.ruedas += 1

    # Método Estático
    @staticmethod
    def calcular_distancia(velocidad, tiempo):
        return velocidad * tiempo

coche_1 = Coche("Toyota", "Corolla", "Rojo")
coche_2 = Coche("Ford", "Focus", "Blanco")

print("Coche 1:")
print(coche_1)
print("Coche 2:")
print(coche_2)
coche_1.color = "Gris"
print("Coche 1:")
print(coche_1)

# Coche.incrementar_ruedas()

# print("Coche 1:")
# print(f"Marca {coche_1.marca}, modelo: {coche_1.modelo}, color: {coche_1.color}\n Cantidad de ruedas : {coche_1.ruedas}")

# print("Coche 2:")
# print(f"Marca {coche_2.marca}, modelo: {coche_2.modelo}, color: {coche_2.color}\n Cantidad de ruedas : {coche_2.ruedas}")
# coche_1.acelerar()
# coche_2.acelerar()

# print(coche_2.calcular_distancia(120,2))