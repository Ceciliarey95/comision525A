import tkinter as ttk
from tkinter import simpledialog
from tkinter import messagebox

from paquete.biblioteca import crear_libro, agregar_libro, buscar_libro, mostrar_libros

def interfaz_agregar_libro():
    titulo = simpledialog.askstring("Agregar libro", "Título del libro:")
    if not titulo:
        return
    autor = simpledialog.askstring("Agregar libro", "Autor del libro:")
    if not autor:
        return
    año = simpledialog.askinteger("Agregar libro", "Año de publicación:")
    if not año:
        return
    libro = crear_libro(titulo, autor, año)
    agregar_libro(biblioteca_1, libro)
    messagebox.showinfo("Éxito", "Libro agregado con éxito")

def interfaz_mostrar_libros():
    libros = mostrar_libros(biblioteca_1)
    messagebox.showinfo("Biblioteca", libros)

def interfaz_buscar_libro():
    titulo = simpledialog.askstring("Buscar libro", "Título del libro a buscar:")
    if not titulo:
        return
    libro = buscar_libro(biblioteca_1, titulo)
    if libro:
        mensaje = f'Título: {libro["titulo"]}\nAutor: {libro["autor"]}\nAño: {libro["año"]}'
        messagebox.showinfo("Libro encontrado", mensaje)
    else:
        messagebox.showwarning("No encontrado", "No existe el libro mencionado")


biblioteca_1 = []

ventana = ttk.Tk()
ventana.title("Biblioteca")
ventana.geometry("300x250")

btn_agregar = ttk.Button(ventana, text="Agregar Libro", command=interfaz_agregar_libro)
btn_agregar.pack(pady=10)

btn_mostrar = ttk.Button(ventana, text="Mostrar Todos", command=interfaz_mostrar_libros)
btn_mostrar.pack(pady=10)

btn_buscar = ttk.Button(ventana, text="Buscar Libro", command=interfaz_buscar_libro)
btn_buscar.pack(pady=10)

btn_salir = ttk.Button(ventana, text="Salir", command=ventana.quit)
btn_salir.pack(pady=20)

ventana.mainloop()