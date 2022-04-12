minas = [
        '-*-*-',
        '--*--',
        '----*',
        '*----',
        ]

def contarMinas(fila,columna):
    """Recorre las casillas que rodean a la posicion enviada por paramatro,
    verificando y sumando las bombas para retornar la cantidad que encontró, 
    teniendo en cuenta que en los extremos el area a recorrer es menor."""
    #si hay fila para analzizar arriba: comienzo en fila - 1 sino empiezo desde fila:
    inicio_fila = fila if fila == 0 else fila -1
    #si hay fila para analzizar abajo: finalizo en fila + 1 sino finalizo en fila
    final_fila = fila if fila == (len(minas) - 1) else fila + 1 
    #si hay columna para analizar a la izquierda:
    inicio_columna = columna if columna == 0 else columna - 1
    #si hay columna para analizar a la derecha:
    final_columna = columna if columna == (len(minas[fila]) - 1) else columna + 1

    cant = 0
    for f in range(inicio_fila,final_fila+1):
        for c in range(inicio_columna,final_columna+1):
            if minas[f][c] == '*':
                cant += 1
    return cant

fila = 0
columna = 0
cantidad_minas =[]
for fila in range(len(minas)): 
    #recorre la lista
    cantidad_minas_fila = ''
    for columna in range(len(minas[fila])): 
        #recorre cada string
        if minas[fila][columna] == '-':
            cantidad = contarMinas(fila,columna)
            cantidad_minas_fila = ''.join((cantidad_minas_fila,str(cantidad)))
        else:
            cantidad_minas_fila = ''.join((cantidad_minas_fila,'*'))
    cantidad_minas.append(cantidad_minas_fila)


for i in range(len(minas)):
    print(minas[i])
print('')
for i in range(len(cantidad_minas)):
    print(cantidad_minas[i])


  