try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")

print("FIN.")
