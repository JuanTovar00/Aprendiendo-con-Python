#Compara.py
#Autor: Juan Tovar
#Fecha: sabado 14 de septiembre de 2019
valor1=input("valor 1:")
valor2=input("Valor 2:")
#Aqui se le pide a usuario que ingrese 2 datos
salida="Numeros almacenados: {} y {}. {}."

if (valor1==valor2):
  print (salida.format(valor1, valor2, "Los Numeros son iguales" ))
  #Aqui entran los valores ingresados si son iguales
else:
    if valor1>valor2:
        print(salida.format(valor1, valor2, "El mayor es el primero"))
        #se ejecuta esto si el valor 1 fue mayor que el segundo
    else:
        print(salida.format(valor1, valor2, "El mayor es el segundo"))
        #si ninguna de las opciones se ejecutan, 
        #este lo hara, al no cumplir con las condiciones anteriores

