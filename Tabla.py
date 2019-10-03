#Taba.py
#Autor: Juan Tovar
#Fecha: sabado 14 de septiembre de 2019
numero=input("Dame un numero del 1 al 9: ")
#Aqui se le pedira al usuario que ingrese un numero del 1 al 9
numero=int(numero)

for i in range(1,11):
#for ejcutara un bloque de codigo un numero determinado de veces
#dependiendo del numero que se haya ingresado
    salida="{} x {}= {}"
    print(salida.format(numero,i,i*numero))
    #Aqui aparecera la tabla de multiplicar del numero ingresado