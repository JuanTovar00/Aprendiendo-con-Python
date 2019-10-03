#Entrada.py
#Autor: Juan Tovar
#Fecha: sabado 14 de septiembre de 2019
print("Ingrese un numero")
#Aqui se le pedira al usario que ingrese un numero

inicio=input()

print(type(inicio))
#En la variable booleana esta el resultado a verificar
#si se ingresa un numero, y si es un numero entero
#

esEntero=(inicio.isdigit() and inicio.find(".")==-1)

if (esEntero):
    print("Dato entero.Muy bien!")
    #Si el numero cumple con la condicion se ejecutara este resultado
else:
    print("Dato no es entero. Intentar nuevamente")
    #Aqui se ejecutara si la condicion no es un numero entero