
cadena = input("Ingrese una palabra o frase: ")

#primera forma: usando una lista que guarda los caracteres ya leidos
print("\n\t1ra forma")
cadena1 = cadena.lower().replace(" ", "")
es_heterograma = True
caracteres = []
for c in cadena1:
    if c not in caracteres:
        caracteres.append(c)
    else:
        es_heterograma = False

if es_heterograma:
    print(f"\"{cadena}\" es un heterograma")
else:
    print(f"\"{cadena}\" NO es un heterograma")    

#segunda forma usando: usando la funcion count con cada caracter
print("\n\t2da forma")
cadena2 = cadena.lower().replace(" ", "")
es_heterograma = True
indice = 0
while es_heterograma and indice < len(cadena):
    if cadena2.count(cadena2[indice]) > 1:
        es_heterograma = False
    indice += 1

if es_heterograma:
    print(f"\"{cadena}\" es un heterograma")
else:
    print(f"\"{cadena}\" NO es un heterograma")    

#tercera forma: usando una lista generada por Counter 
from typing import Counter

print("\n\t3ra forma")
cadena3 = cadena.lower().replace(" ", "")
mas_cantidad = Counter(cadena3).most_common(1)
print(mas_cantidad)
if mas_cantidad[0][1] > 1:
    print(f"\"{cadena}\" NO es un heterograma")
else:
    print(f"\"{cadena}\" es un heterograma")  

#cuarta forma: usando conjunto y comparando cantidad de elementos
print("\n\t4ta forma")
caracteres_sin_repetir = list(set(cadena.lower().replace(" ", "")))
lista_caracteres = list(cadena.lower().replace(" ", ""))
if len(lista_caracteres) == len(caracteres_sin_repetir):
    print(f"\"{cadena}\" es un heterograma") 
else:
    print(f"\"{cadena}\" NO es un heterograma")  


