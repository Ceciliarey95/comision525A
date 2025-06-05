
def biblioteca_1():
    pass

def crear_libro(titulo, autor, año):
    return {"titulo" : titulo,
            "autor": autor,
            "año": año}

def agregar_libro(biblioteca, libro):
    biblioteca.append(libro)

def buscar_libro(biblioteca, titulo):
    for libro in biblioteca:
        if libro["titulo"].upper() == titulo.upper():
            return libro
    return "No existe el libro mencionado"

def mostrar_libros(biblioteca):
    for libro in biblioteca:
        print(f'Titulo: {libro["titulo"]} | Autor : {libro["autor"]} | Año: {libro["año"]}')

def eliminar_libro():
    pass