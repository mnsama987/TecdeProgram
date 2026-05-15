## 🧠 Integradores

# ### Ejercicio 20 — Sistema de análisis de datos
# Desarrollar un programa que:
# 1. permita ingresar números hasta 0
def pedir_numeros():
    lista = []
    numeros = int(input("Ingresar un numero: "))
    while numeros >= 0:
        lista.append(numeros)
        numeros = int(input("Ingresar un numero: "))
    contador = len(lista)
    return lista, contador

# 2. los almacene en una lista
# - cantidad de datos
lista, contador = pedir_numeros()

# 3. luego calcule:
# - suma total
def sumar():
    suma = 0
    for i in lista:
        suma += i
    return suma
suma = sumar()
print(f"la suma es {suma}")

# - promedio
def promediar():
    promedio = suma/contador
    return promedio

print(f"el promedio es {promediar()}")

# - cantidad de números pares
def contar_pares():
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    cantidad_pares = len(pares)
    return pares, cantidad_pares  

pares, cantidad_pares = contar_pares()
print(f"los numeros pares son {pares} y la cantidad de numeros pares es {cantidad_pares}")   

