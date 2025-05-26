
estudiantes = []


for i in range(5):
    print(f"\nEstudiante {i + 1}")
    nombre = input("Ingrese el nombre del estudiante: ")
    calificaciones = []
    for j in range(3):
        calificacion = float(input(f"Ingrese la calificación {j + 1}: "))
        calificaciones.append(calificacion)
    promedio = sum(calificaciones) / 3
    estudiantes.append((nombre, promedio))


print("\n--- Promedios Finales ---")
for nombre, promedio in estudiantes:
    print(f"{nombre}: {promedio:.2f}")
