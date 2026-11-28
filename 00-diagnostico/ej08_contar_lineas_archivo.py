with open ("00-diagnostico/texto.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(f"El archivo tiene {len(lineas)} líneas")