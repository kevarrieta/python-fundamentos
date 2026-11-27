contraseña = input("Ingresa tú contraseña:")

tiene_mayusculas = False
tiene_numeros = False

for caracter in contraseña:
    if caracter.isupper():
        tiene_mayusculas = True
    if caracter.isdigit():
        tiene_numeros = True

if len(contraseña) >= 8 and tiene_mayusculas and tiene_numeros:
    print("Contraseña válida")
else:
    print("Contraseña inválida. Debe tener al menos 8 caracteres, una letra mayúscula y un número.")