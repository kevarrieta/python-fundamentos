for Numeros in range(1, 31):
    if Numeros % 3 == 0 and Numeros % 5 == 0:
        print("FizzBuzz")
    elif Numeros % 3 == 0:
        print("Fizz")
    elif Numeros % 5 == 0:
        print("Buzz")
    else:
        print(Numeros)