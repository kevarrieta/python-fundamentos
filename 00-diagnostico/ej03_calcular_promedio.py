Nota = (input("Ingrese las notas separadas por comas:"))
Nota = Nota.split(",")

notas = []
for nota in Nota:
    notas.append(float(nota))
suma = sum(notas)
cantidad = len(notas)
promedio = suma / cantidad
print("El promedio de las notas es:", promedio)

