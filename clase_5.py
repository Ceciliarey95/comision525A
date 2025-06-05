lista = ["Hola", 30, True]

# print(lista[0])
# print(lista[1])
# print(lista[2])

# lista1 = [ "Ceci", "Eze", "Franco"]
# print(f"Id lista 1: {id(lista1)}")
# lista2 = lista1
# lista2.append("Jorge")
# print(f"Id lista 2: {id(lista2)}")
# print(lista1)
# print(lista2)

# lista1 = [" Romi", "Paola", "Monica"]
# print(f"Id lista 1 v2 : {id(lista1)}")
# print(f"Id lista 2 v2: {id(lista2)}")

lista1 = ["Ceci", "Diego", "Franco"]

lista2 = ["Hola", "Chau", "Bienvenidos"]

lista3 = ["Info", 25, lista1, lista2]


# print(lista1, lista2)

lista1[-1] = "Eva"

# print(lista1)

# lista3.append(30)
# lista3.append(30)
# print(lista3)
# lista3.remove(30)
# print(lista3)

conjunto = { 2 , 3, 4, 1 , 0 ,2, 5, 3 ,4 }
conjunto_2 = {"hola", "chau", "info", 2}

interseccion = conjunto & conjunto_2
# print(len(interseccion))

diccionario= { 'nombre' : 'Ceci', 'edad' : 30, 'cargo': 'profesora' }

claves = list(diccionario.keys())

valor = list(diccionario.values())

print(f"Claves: {claves}\nValores: {valor}")