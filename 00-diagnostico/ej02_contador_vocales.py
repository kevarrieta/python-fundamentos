texto = input("Ingrese un texto para contar las vocales:").lower()
contador = 0
for letra in texto:
    if letra in "aeiou":
        contador += 1
print(f"El texto ingresado tiene {contador} vocales.")
