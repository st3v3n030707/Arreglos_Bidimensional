n = int(input("Número de filas (<10): "))
m = int(input("Número de columnas (<10): "))
matriz = [[int(input(f"Valor en [{i}][{j}]: ")) for j in range(m)] for i in range(n)]

# c. Suma por fila
for i in range(n):
    print(f"Fila {i}: suma = {sum(matriz[i])}")

# d. Promedio por columna
for j in range(m):
    suma_col = sum(matriz[i][j] for i in range(n))
    print(f"Columna {j}: promedio = {suma_col / n:.2f}")

# e. Mayor valor y posición
mayor = matriz[0][0]
fila_mayor, col_mayor = 0, 0
for i in range(n):
    for j in range(m):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            fila_mayor, col_mayor = i, j

print(f"Mayor valor: {mayor} en fila {fila_mayor}, columna {col_mayor}")
