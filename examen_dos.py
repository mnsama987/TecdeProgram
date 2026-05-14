# Escribí un programa que pida al usuario palabras hasta que ingrese la palabra 'fin'. Al finalizar, mostrá cuántas palabras ingresó y cuál tiene más letras.


# El programa debe organizarse con las siguientes funciones:

# pedir_palabras()  → pide palabras al usuario hasta que ingrese 'fin' y las devuelve en una lista.
# analizar(palabras)  → recibe la lista y devuelve la cantidad y la palabra más larga.
# mostrar_resultados(cantidad, mas_larga)  → muestra los resultados por pantalla.


# definiendo variables

# palabras = []
# cantidad = []

# # definiendo funciones

# def pedir_palabras():
#     palabras = []
#     palabra = input("Ingresa una palabra (Para finalizar ingresa la palabra FIN): ")
#     while palabra.lower() != "fin":
#         palabras.append(palabra)
#         palabra = input("Ingresa una palabra (Para finalizar ingresa la palabra FIN): ")
#     return palabras

# def analizar(palabras):
#     if not palabras:
#         return 0, None
#     cantidad = len(palabras)
#     mas_larga = max(palabras, key=len)
#     return cantidad, mas_larga    

# palabras = pedir_palabras()
# cantidad, mas_larga = analizar(palabras)

# def mostrar_resultados(palabras, cantidad, mas_larga):
#     print(f"La las palabras de la lista son: {palabras}")
#     print(f"La cantidad de palabras es:  {cantidad}")
#     print(f"La palabra mas larga es:  {mas_larga}")

# mostrar_resultados(palabras, cantidad, mas_larga)

# ejercicio 2

# temperaturas = [22, 35, 18, 40, 15, 31, 28, 12, 38, 20]

# def filtrar_calurosos(temperaturas):
#     calurosos = []
#     contador_calurosos = []
#     for temp in temperaturas:
#         if temp > 30:
#             calurosos.append(temp)
#     contador_calurosos = len(calurosos)
#     return calurosos, contador_calurosos

# calurosos, contador_calurosos = filtrar_calurosos(temperaturas)

# def calcular_promedio(temperaturas):
#     cantidad = len(temperaturas)
#     suma = 0
#     for temp in temperaturas:
#         suma = suma + temp
#         return suma
#     promedio = suma/cantidad
#     return promedio

# promedio = calcular_promedio(temperaturas)

# def mostrar_informe(contador_calurosos, promedio):
#     print(f"La cantidad de días calurosos son: {contador_calurosos}")
#     print(f"El promedio de temperatura es: {promedio}")

# mostrar_informe(contador_calurosos, promedio)

# Escribí un programa modular con las siguientes funciones:

# pedir_productos()  → pide al usuario el nombre de 5 productos y los devuelve en una lista.
# analizar_productos(productos)  → recibe la lista y devuelve la cantidad de productos y el primero en orden alfabético.
# guardar_reporte(productos, cantidad, primero)  → guarda en inventario.txt la lista de productos, la cantidad y el primero alfabéticamente. Si el archivo no se puede crear, debe mostrar un mensaje de error en lugar de romperse.

# El programa principal debe llamar a las tres funciones en orden.

# productos = []

# def pedir_productos(productos):
#     producto = 0
#     for producto in range(5):
#         producto = input("Ingresá el nombre del producto: ")
#         productos.append(producto)
#     return productos

# def analizar_productos(productos):
#     cantidad = len(productos)
#     alfabetico = sorted(productos)[0]
#     return cantidad, alfabetico

# productos = pedir_productos(productos)
# cantidad, alfabetico = analizar_productos(productos)

# def guardar_reporte(productos, cantidad, alfabetico):
#     archivo = open("inventario.txt", "w")
#     archivo.write(f"La lista de productos es: {productos}\n")
#     archivo.write(f"La cantidad de productos es: {cantidad}\n")
#     archivo.write(f"El primer de producto es: {alfabetico}\n")
#     archivo.close()

# guardar_reporte(productos, cantidad, alfabetico)