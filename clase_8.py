import random
import tkinter as tk

from paquete.biblioteca import crear_libro, agregar_libro, buscar_libro, mostrar_libros

## MODULOS

"""def generador_num():
    return random.randint(1,100)

print("Bienvenido al generador de números aleatorios! (1 - 100)")

entrada = input("Desea comenzar? (S/N)")

while entrada.upper() == "S":
    numero = generador_num()
    print(f"El numero generado es {numero}")
    entrada = input("Desea continuar y generar otro numero? (S/N)")

print("Gracias por utilizar nuestro programa")"""

## BIBLIOTECA

"""biblioteca_1 = []

libro_1 = crear_libro("Harry Potter", "J.K.Rowling", 1991)
libro_2 = crear_libro("Logica de programacion", "Omar Trejos Buritica", 2015)

agregar_libro(biblioteca_1, libro_1)
agregar_libro(biblioteca_1, libro_2)

mostrar_libros(biblioteca = biblioteca_1)

libro_buscado = buscar_libro(biblioteca_1, "harry PoTter")

print(libro_buscado)"""

## TKINTER

# Creamos una ventana

"""ventana = tk.Tk()
ventana.title("Bienvenidos!!")
ventana.geometry("600x800")

# Creamos un label
etiqueta = tk.Label(ventana, text="Hola mundo con Tkinter!", font=("Arial", 30))
etiqueta.pack()

## Iniciamos la ventana principal en loop
ventana.mainloop()"""

## Creamos una interfaz con boton que interactua con la consola

def saludar():
    print("Hola")

ventana = tk.Tk()
ventana.title("Bienvenidos!!")
ventana.geometry("400x300")

boton = tk.Button(ventana, text="Saludar", font=("Arial", 20), command=saludar)
boton.pack()

ventana.mainloop()