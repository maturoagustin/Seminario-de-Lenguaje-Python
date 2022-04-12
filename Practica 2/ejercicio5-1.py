
from typing import Counter


frase = input("Ingrese frase: ").lower()
palabra = input("Ingrese palabra: ").lower()
cantidad = frase.count(palabra) 
print(f"La palabra \"{palabra}\" se repite {cantidad} veces en la frase ingresada.")