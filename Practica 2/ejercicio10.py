
#abro los archivos a usar en modo lectura y los nombres con el utf-8 para leer las tildes
arch_nom = open('nombres_1.txt','r',encoding="UTF-8")
arch_eva_1 = open('eval1.txt','r')
arch_eva_2 = open('eval2.txt','r')

#declaro e inicializo las variables a usar para los datos
#una lista para los alumnos y notas_total para calcular el promedio
#no uso diccionario porque como son nombres, no son unicos
alumnos_total = []
notas_total = 0

#recorro los 3 archivos agregando tuplas a la lista que contengan la suma de las notas 
# del alumno y el nombre y sumando el total de las notas
for nom,e1,e2 in zip(arch_nom,arch_eva_1,arch_eva_2):
    nombre = nom.replace("\'","").replace(",","").replace("\n","").replace(" ","")
    nota = int(e1.replace(",","")) + int(e2.replace(",",""))
    alumnos_total.append((nombre,nota))
    notas_total += nota

#cierro los archivos porque ya tengo los datos
arch_nom.close()
arch_eva_1.close()
arch_eva_2.close()

#calculo el promedio y recorro la estrucura creada anteriormente e informa
#que alumno está por debajo del promedio
promedio = notas_total / len(alumnos_total)
print(f"El promedio es de {promedio:.3f} puntos")
print("Alumnos con nota menor al promedio: ")
for alumno in alumnos_total:
    if alumno[1] < promedio:
        print(alumno)
