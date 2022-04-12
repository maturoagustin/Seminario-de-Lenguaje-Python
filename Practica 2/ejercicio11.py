#Abro los archivos a usar en modo lectura y los nombres con el utf-8 para leer las tildes
arch_nom_1 = open('nombres_1.txt','r',encoding="UTF-8")
arch_nom_2 = open('nombres_2.txt','r',encoding="UTF-8")
arch_eva_1 = open('eval1.txt','r')
arch_eva_2 = open('eval2.txt','r')

#Tomo los datos de los archivos y los copio en variables con un formato para trabajar mejor
nombres_1 = arch_nom_1.read().replace("\'","").replace("\n","").replace(" ","").split(",")
nombres_2 = arch_nom_2.read().replace("\'","").replace("\n","").replace(" ","").split(",")
notas_1 = [int(n.replace(",","")) for n in arch_eva_1]
notas_2 = [int(n.replace(",","")) for n in arch_eva_2]


#cierro los archivos porque ya copie los datos
arch_nom_1.close()
arch_nom_2.close()
arch_eva_1.close()
arch_eva_2.close()

# Compruebo las coincidencias con list comprehension generando un conjunto
# para que no haya nombre repetidos.
coincidencias = {n for n in nombres_1 if n in nombres_2}
print("Los nombres que aparecen en los dos archivos son: \n", coincidencias)

# Recorro los datos e imprimo con formato nombre, notas y total
print("{:>5} {} \t {:>5} \t {:>5} \t {:>5}".format('ID','Nombre','Eval1','Eval2','Total'))
for x,nom,ev1,ev2 in zip(range(len(nombres_1)),nombres_1,notas_1,notas_2):
    print("{:>5} {} \t {:>5} \t {:>5} \t {:>5}".format(x,nom,ev1,ev2,ev1+ev2))