matriz = [
    [1, 2, 3, 7],
    [4, 5, 6, 8]
]

lineal = []
columnas = len(matriz[0])
filas = len(matriz)
for col in range(columnas):
    for fil in range(filas):
        lineal.append(matriz[fil][col])

print("Arreglo linealizado:", lineal)