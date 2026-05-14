# #  programa para pedir numeros enteros hasta que sea un numero negativo
# # mostrar cuantos numeros ingresaron
# # mostrar cual es el mayor numero ingresado

# numeros = []

# # funciones

# def pedir_numeros(numeros):
# # pide numeros y los devuelve en una lista
#     numero = int(input("Ingrese un numero entero(negativo para terminar programa): "))
#     while numero > 0:
#         numeros.append(numero)
#         numero = int(input("Ingrese un numero entero(negativo para terminar programa): "))
#     return numeros


# def analizar(numeros):
#     cantidad = 0
#     mayor = 0
#     for i in numeros:
#         # suma al contador la cantidad de numeros ingresados 
#         cantidad +=1  
#         # esto es igual a cantidad = cantidad + 1
#         #  encuentra el mayor numero
#         if i > mayor:
#             mayor = i
#         # ejecuta el bucle y realiza la operacion
#     return cantidad, mayor

# def mostrar_resultados(cantidad, mayor):
#     print(f"Cantidad de numeros ingresados: {cantidad}")
#     print(f"Mayor numero ingresado: {mayor}")


# numeros = pedir_numeros(numeros)
# cantidad, mayor = analizar(numeros)
# mostrar_resultados(cantidad, mayor)

# ejercicio 2
# notas = [7, 8, 9, 5, 6, 2, 8]

# def filtrar_notas(notas):
#     aprobados = []
#     desaprobados = []
#     for nota in notas:
#         if nota >= 6:
#             aprobados.append(nota)
#         else:
#             desaprobados.append(nota)
#     return aprobados, desaprobados

# def contar_notas(notas):
#     aprobados = 0
#     desaprobados = 0
#     for nota in notas:
#         if nota >= 6:
#             aprobados += 1
#         else:
#             desaprobados += 1
#     return aprobados, desaprobados

# def sumar(notas):
#     suma = 0
#     for nota in notas:
#         suma = suma + nota
#     return suma


# # def calcular_promedio(notas):
# #     cantidad = len(notas)
# #     promedio = sumar(notas)/cantidad
# #     return promedio

# # aprobados, desaprobados = filtrar_notas(notas)
# # promedio = calcular_promedio(notas)
# # aprobados_count, desaprobados_count = contar_notas(notas)

# # # print(f"los aprobados son {aprobados}")
# # # print(f"el promedio es {promedio}")
    
# # def mostrar_informe(aprobados, desaprobados, promedio, aprobados_count, desaprobados_count):
# #     print(f"los aprobados son {aprobados}")
# #     print(f"los desaprobados son {desaprobados}")
# #     print(f"el promedio es general es {promedio}")
# #     print(f"Cantidad de aprobados: {aprobados_count}")
# #     print(f"Cantidad de desaprobados: {desaprobados_count}")

# # mostrar_informe(aprobados, desaprobados, promedio, aprobados_count, desaprobados_count)


# # ejercicio 3

# # pide 5 notas al usuario y las devuelve en una lista

# def pedir_notas():
#     notas = []
#     for i in range(5):
#         nota =  int(input("Ingresa una nota:"))
#         notas.append(nota)
#     return notas

# # recibe la lista y devuelve el promedio

# def filtrar_notas(notas):
#     aprobados = []
#     desaprobados = []
#     for nota in notas:
#         if nota >= 6:
#             aprobados.append(nota)
#         else:
#             desaprobados.append(nota)
#     return aprobados, desaprobados

# def contar_notas(notas):
#     aprobados = 0
#     desaprobados = 0
#     for nota in notas:
#         if nota >= 6:
#             aprobados += 1
#         else:
#             desaprobados += 1
#     return aprobados, desaprobados

# def sumar(notas):
#     suma = 0
#     for nota in notas:
#         suma = suma + nota
#     return suma


# def calcular_promedio(notas):
#     cantidad = len(notas)
#     promedio = sumar(notas)/cantidad
#     return promedio

# notas = pedir_notas()
# aprobados, desaprobados = filtrar_notas(notas)
# promedio = calcular_promedio(notas)
# aprobados_count, desaprobados_count = contar_notas(notas)
    
# def mostrar_informe(notas, aprobados, desaprobados, promedio, aprobados_count, desaprobados_count):
#     print(f"las notas ingresadas son {notas}")
#     print(f"los aprobados son {aprobados}")
#     print(f"los desaprobados son {desaprobados}")
#     print(f"el promedio es general es {promedio}")
#     print(f"Cantidad de aprobados: {aprobados_count}")
#     print(f"Cantidad de desaprobados: {desaprobados_count}")

# mostrar_informe(notas, aprobados, desaprobados, promedio, aprobados_count, desaprobados_count)
# archivo = open("resultado.txt", "w")
# archivo.write(f"las notas ingresadas son {notas}\n")
# archivo.write(f"los aprobados son {aprobados}\n")
# archivo.write(f"los desaprobados son {desaprobados}\n")
# archivo.write(f"el promedio es general es {promedio}\n")
# archivo.write(f"Cantidad de aprobados: {aprobados_count}\n")
# archivo.write(f"Cantidad de desaprobados: {desaprobados_count}\n")
# archivo.close()

# examen 1 ejercicio 1
# numeros = []

# def  pedir_numeros(numeros):
#     print("Para finalizar el programa ingresa un numero negativo")
#     numero = int(input("Ingresa un numero: "))
#     while numero >= 0:
#         numero = int(input("Ingresa un numero: "))
#         numeros.append(numero)
#     return numeros

# def analizar(numeros):
#     cantidad = len(numeros)
#     mayor = max(numeros)
#     return cantidad, mayor

# numeros = pedir_numeros(numeros)
# cantidad, mayor = analizar(numeros)

# def mostrar_resultados(cantidad, mayor):
#     print(f"La cantidad de numeros ingresados es: {cantidad}")
#     print(f"El numero mayor del listado es: {mayor}")

# mostrar_resultados(cantidad, mayor)

# examen 1 ejercicio 2
# Trabajá con el siguiente listado de notas:


# notas = [7, 3, 9, 5, 6, 2, 8]
# Escribí un programa con las siguientes funciones:
# filtrar_aprobados(notas)  → devuelve una lista con las notas mayores o iguales a 6.
# calcular_promedio(notas)  → devuelve el promedio de toda la lista.
# mostrar_informe(aprobados, promedio)  → muestra cuántos aprobaron, cuántos desaprobaron y el promedio general.
# ⚠ Nota: No se aceptan soluciones sin funciones.

# notas = [7, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 1]

# def filtrar_aprobados(notas):
#     aprobados = []
#     desaprobados = []
#     for nota in notas:
#         if nota >= 6:
#             aprobados.append(nota)
#         else:
#             desaprobados.append(nota)
#     aprobados_total = len(aprobados)
#     desaprobados_total = len(desaprobados)
#     return aprobados, desaprobados, aprobados_total, desaprobados_total

# aprobados, desaprobados, aprobados_total, desaprobados_total = filtrar_aprobados(notas)

# def calcular_promedio(notas):
#     cantidad = len(notas)
#     suma = 0
#     for nota in notas:
#         suma += nota
#     promedio = suma/cantidad
#     return promedio

# promedio = calcular_promedio(notas)


# def mostrar_informe(aprobados, desaprobados, aprobados_total, desaprobados_total, promedio):
#     print(f"Los aprobados son :{aprobados}")
#     print(f"La cantidad de aprobados es:{aprobados_total}")
#     print(f"Los desaprobados son :{desaprobados}")
#     print(f"La cantidad de desaprobados es: {desaprobados_total}")
#     print(f"El promedio general es :{promedio}")
#     return(
#         f"Los aprobados son: {aprobados}\n"
#         f"La cantidad de aprobados es: {aprobados_total}\n"
#         f"Los desaprobados son: {desaprobados}\n"
#         f"La cantidad de desaprobados es: {desaprobados_total}\n"
#         f"El promedio general es: {promedio}\n"
#     )

# archivo = open("informe.txt", "w")
# archivo.write(
#     mostrar_informe(
#         aprobados,
#         desaprobados,
#         aprobados_total,
#         desaprobados_total,
#         promedio))
# archivo.close()