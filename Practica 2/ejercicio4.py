
evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures."""

#tomo el titulo y lo separo por palabras
titulo = evaluar.splitlines()[0].split()

#elimino la palabra "titulo:"
titulo.remove('título:')

if len(titulo) <= 10:
    print('El titulo está ok')
else:
    print('El titulo NO está ok')

#reemplazo los \n por espacios y separo el titulo del texto
oraciones = evaluar.replace('\n'," ").split('resumen:')

#separo el resumen en oraciones separadas por punto (esto elimina el titulo)
oraciones = oraciones[1].split(".")

#elimino el ultimo elemento de la lista que es un string vacio
oraciones.pop() 

dificultad = [0,0,0,0]
for oracion in oraciones:
    cant = len(oracion.split())
    if cant <= 12:
        dificultad[0] += 1
    elif cant >= 13 and cant <=17:
        dificultad[1] += 1
    elif cant >= 18 and cant <= 25:
        dificultad[2] += 1
    else:
        dificultad[3] += 1

print(f"Cantidad de oraciones fáciles de leer: {dificultad[0]}, aceptables para leer: {dificultad[1]}, \
dificil de leer: {dificultad[2]}, muy dificil de leer: {dificultad[3]}")

