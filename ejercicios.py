lista = [[1,2,3],[4,5,6],[7,18,9]]

for i in range(1):
    print("Los numeros de la matriz son:")
    print(lista[0])
    print(lista[1])
    print(lista[2])

for i in lista:
    for j in i:
        if j > 10:
            print("Los numeros mayores a 10")
            print(j)
    else:
        print("No hay mayores a 10:")

# def diagonal_principal(matriz):
#     if not matriz: return []
#     n = min(len(matriz), len(matriz[0]))
#     return [matriz[i][i] for i in range(n)]

# m = [[1,2,3],[4,5,6],[7,8,9]]
# diag = diagonal_principal(m)
# print(diag)        # [1, 5, 9]
# print(sum(diag))   # 15