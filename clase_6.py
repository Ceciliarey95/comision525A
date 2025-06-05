# color_1 = "Rojo" # rojo
# color_2 = "Verde" # verde
# color_3 = "Rojo" # rojo

# color_capitalizado = color_1.capitalize()

# if color_1.lower() != color_2.lower() and color_2.lower() != color_3.lower() and color_1.lower() == color_3.lower():
    # print("Los colores 1 y 3 son iguales.")
    # print(color_capitalizado)
    # print(color_1)

# if color_1 == color_3:
#     print("1 y 2 son iguales")
# elif color_1 == color_3:
#     print("1 y 3 son iguales")
# else:
#     print("1 y 3 son iguales -- else")

caracter = input(" Ingrese un carácter : ")

if caracter.isupper():
    print(" Es mayuscula ")
elif caracter.islower():
    print("Es minuscula")
elif caracter.isdigit():
    print("Es un numero")
elif caracter.isascii():
    print("Es ascii")
else:
    print("Es un caracter especial")

# numeros = [ 1, 2, 3, 4, 5 ]

# for numero in numeros:
#     print(numero)

# palabra = "Python"

# for letra in palabra:
    # print(letra)

# for i in range(3,11):
#     print(i)

# diccionario = { 
#     "nombre" : "Ceci",
#     "apellido" : "Rey",
#     "provincia" : "Chaco" 
#     }

# for clave in diccionario.keys():
#     print(clave)

# print( " ---- ")

# for valor in diccionario.values():
#     print(valor)
# print( " ---- ")

# for clave, valor in diccionario.items():
#     print(f"Clave: {clave} -> Valor: {valor}")


# contador = int(input("Ingrese un munero: "))

# while contador <= 10:
#     if contador == 5:
#         continue
#     print(contador)
#     contador = int(input("Ingrese un numero: "))

# print("se termino")

# bandera = True

# while bandera:
#     respuesta = input("Queres salir? (s/n) : ")
#     if respuesta.lower() == "s":
#         bandera = True

## Bandera -> Pasarla a False para cortar
## True -> Usar break
## Expresión -> operacion que pase la expresion a False

# num = int(input("ingrese un numero: "))
# i = 1
# suma = 0

# while i <= num: 
#     suma += i
#     i +=1 

# print(f"La suma de el 1 hasta el {num} es de : {suma}")

# while i <= 10:
#     print(f" {num} x {i} = {num*i}")
#     i +=1