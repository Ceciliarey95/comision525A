## FUNCIONES

def saludar_con_return():
    return "Hola mundo con return!"

def saludar_con_print():
    print("Hola mundo con print!")

def sumar(x, y=2):
    """Retorna la suma de los dos parametros pasados"""
    return x + y

def saludar(nombre, mensaje="Hola"):
    return f"{mensaje}, {nombre}"

def receta(titulo, *args):
    print(f"Receta de {titulo}")
    print("Ingredientes: ")

    for i in args:
        print(i)

""" def suma(**kwargs):
    resultado = 0

    for clave, valor in kwargs.items():
        print(clave, "=", valor)
        resultado += valor
    return resultado """

def operaciones(a, b):
    suma = a + b
    resta = a - b

    return suma, resta


def calcular_area_circulo(radio):
    """ Retorna el area de un circulo tomando como parametro el radio """
    from math import pi
    return pi * radio ** 2


def calcular_precio(precio, descuento):
    """ Retorna el precio del producto con el descuento aplicado"""
    return precio - (precio * (descuento / 100))

def contar_pares(lista):
    """ Retorna la cantidad de numeros pares dentro de la lista pasada """
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    return contador

def caja_registradora():
    total = 0
    while True:
        entrada = input("Ingrese un precio o (0) para finalizar: ")
        if entrada == "0":
            break
        else:
            total += float(entrada)
    print(f"Total a pagar es de : ${total}")

