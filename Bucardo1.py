ventas = [
    [12, 15, 10, 9],   # Vendedor 1
    [20, 18, 22, 16],  # Vendedor 2
    [8, 11, 7, 10]     # Vendedor 3
]

# a. Zona con más computadoras vendidas
zonas = [sum([ventas[v][z] for v in range(3)]) for z in range(4)]
print("Zona con más ventas:", zonas.index(max(zonas)))

# b. Vendedor que menos vendió
total_vendedor = [sum(v) for v in ventas]
print("Vendedor con menos ventas:", total_vendedor.index(min(total_vendedor)))

# c. Total de computadoras vendidas
print("Total de computadoras vendidas:", sum(total_vendedor))