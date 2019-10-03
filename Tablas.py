#Tablas.py
#Autor: Juan Tovar
#Fecha: sabado 14 de septiembre de 2019

for i  in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    print()
    #print sin agurmentaos se utiiza para dar un salto de linea
    for j in range(1,11):
        #Dentro de for se agrega otro for
        salida="{} x {} ={}"
        print(salida.format(i,j,i*j))
    else:
         print ()