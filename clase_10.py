class Vehiculo:

    def __init__(self, ruedas, marca, modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ruedas = ruedas

    def acelerar(self):
        print("Estoy acelerando!! ")

    def frenar(self):
        pass

class Coche(Vehiculo):

    def __init__(self, ruedas , marca, modelo,color, dueño):
        super().__init__(ruedas,marca,modelo,color)
        self.dueño = dueño
    
    def bocina(self):
        print("PIIIIIIIIII ")

class Bicicleta(Vehiculo):
    def acelerar(self):
        print("Estoy pedaleando más rápido!")

auto_1 = Coche(4, "Ford", "Focus", "Gris","Juan")

bici_1 = Bicicleta(2,"SLP", "100", "Blanco")

# auto_1.bocina()
# bici_1.acelerar()

# print(f"Mi auto es un {auto_1.marca} {auto_1.modelo} de color {auto_1.color} con {auto_1.ruedas} ruedas y mi nombre es {auto_1.dueño}")
# print(f"Mi bici es una {bici_1.marca} {bici_1.modelo} de color {bici_1.color} con {bici_1.ruedas} ruedas")

# class A : 
#     def __init__(self):
#         print("Soy la clase A")

# class B : 
#     def __init__(self):
#         print("Soy la clase B")

# class C(A,B):

#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         print("Soy la clase C")

# test= C()

class Empleado:
    def __init__(self, sueldo):
        self.sueldo = sueldo
    
    def calcular_sueldo_anual(self):
        sueldo_anual = 12 * self.sueldo * (1+ 1/100)

        print(f"El sueldo anual de un empleado General es {sueldo_anual}")

class Programador(Empleado):

    def calcular_sueldo_anual(self):
        sueldo_anual = 12 * self.sueldo * (1 + 4/100)

        print(f"El sueldo anual de un PROGRAMADOR es de {sueldo_anual}")

class Diseñador(Empleado):

    def calcular_sueldo_anual(self):
        sueldo_anual = 12 * self.sueldo * (1 + 6/100)

        print(f"El sueldo anual de un DISEÑADOR es de {sueldo_anual}")


empleados = [
    Empleado(1000),
    Programador(500),
    Diseñador(1500),
    Empleado(1200),
    Programador(2000)
]

def calculo_sueldos():
    for empleado in empleados:
        empleado.calcular_sueldo_anual()

# calculo_sueldos()

class Circulo:

    def __init__(self,radio):
        self.radio = radio
        self.__pi = 3.1415
        self._color = "Rojo"

    def calcular_perimetro(self):
        return 2 * self.__pi * self.radio
    
    def calcular_area(self):
        return self.__pi * self.radio ** 2
    
circulo_1 = Circulo(3.5)

print(circulo_1.calcular_area())

print(circulo_1.calcular_perimetro())

print(f" El color de PI dentro de la clase es de {circulo_1._color}")