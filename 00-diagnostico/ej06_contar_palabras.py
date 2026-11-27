frase = input("Ingrese una frase:").lower().split()
frecuencia = {}
for palabra in frase:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else: 
        frecuencia[palabra] = 1
print("Frecuencia de palabras:")
for palabra, cantidad in frecuencia.items():
    print(f"{palabra}: {cantidad}")