

class Libro:
    def __init__(self, titulo, autor, ISBN, numero_de_paginas, genero):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.numero_de_paginas = numero_de_paginas
        self.genero = genero
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro {self.titulo} prestado.")
        else:
            print(f"El libro {self.titulo} no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El libro {self.titulo} ha sido devuelto.")

    def buscar_por_titulo(self, titulo):
        return self.titulo.lower() == titulo.lower()
    

class Autor:
    def __init__(self,nombre,nacionalidad,fecha_nacimiento):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.biblioteca = []

    def publicar_libro(self, libro):
        self.biblioteca.append(libro)

class Lector:

    def __init__(self, nombre , edad , direccion,numero_socio):
        self.nombre = nombre
        self.edad = edad 
        self.direccion = direccion
        self.numero_socio = numero_socio
        self.libros_prestados = []

    def solicitar_prestamo(self, libro):
        if libro.disponible:
            libro.prestar()
            self.libros_prestados.append(libro)
        else:
            print(f"El libro '{libro.titulo}' no está disponible para préstamo.")
    
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto el libro '{libro.titulo}'.")
        else:
            print(f"{self.nombre} no tiene el libro '{libro.titulo}' prestado.")

class Libreria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.lectores = []
        self.autores = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro {libro.titulo} se ha agregado a la libreria.")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.buscar_por_titulo(titulo):
                return libro
        return None

    def prestar_libro(self, lector, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            lector.solicitar_prestamo(libro)
        else:
            print(f"El libro {libro.titulo} no está en la libreria")

    def registrar_lector(self,lector):
        self.lectores.append(lector)
        print(f"Lector {lector.nombre} registrado.")

autor_1 = Autor("Julio Verne", "Francés", "1-1-1828")
libro_1 = Libro("Viaje al centro de la tierra", autor_1, 2134564684, 300, "Aventura")

autor_1.publicar_libro(libro_1)

lector_1 = Lector("Juan", 30, "Ni idea 123", 101)

libreria = Libreria("Libreria Chaco")

libreria.agregar_libro(libro_1)
libreria.registrar_lector(lector_1)

libreria.prestar_libro(lector_1, "Viaje al centro de la tierra")
libreria.prestar_libro(lector_1, "Viaje al centro de la tierra")
