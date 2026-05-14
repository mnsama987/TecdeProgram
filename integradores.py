## 🧠 Integradores

# ---

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
lista, contador = pedir_numeros()

# - cantidad de datos
# 3. luego calcule:

# - suma total
def sumar():
    suma = 0
    for i in lista:
        suma += i
    return suma
# - promedio
suma = sumar()
print(f"la suma es {suma}")

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
print(f"los numeros pares son {pares} y la cantidad de pares es {cantidad_pares}")   





# ### Ejercicio 21 — Persistencia de datos



# Extender el ejercicio anterior para:

# - guardar los datos en un archivo
# - luego leerlos desde el archivo
# - mostrar nuevamente los resultados

# ---




# ### Ejercicio 22 — Sistema completo

# Simular un sistema que:

# 1. permita ingresar datos numéricos
# 2. los almacene en una estructura
# 3. los procese
# 4. los persista en archivo

# El programa debe mostrar:

# - valores mayores a un umbral (ej: >10)
# - promedio
# - valor máximo
# - cantidad de datos