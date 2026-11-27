numero = int(input("Ingrese un número para generar su tabla de multiplicar:"))

for tabla in range (1,11):
    resultado = numero * tabla 
    print(f"{numero} x {tabla} = {resultado}")
