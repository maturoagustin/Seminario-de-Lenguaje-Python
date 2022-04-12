"""cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):")
if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
cant = 0
for car in cadena:
    if car == "@" or car == "!":
        cant = cant + 1
if cant >= 1:
    print("Ingresaste alguno de estos símbolos: @ o !" )
else:
    print("Clave válida")"""

cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):")
if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
elif (cadena.count('@') > 0) or (cadena.count('!') > 0):
    print("Ingresaste alguno de estos símbolos: @ o !" )
else:
    print("Clave válida")

