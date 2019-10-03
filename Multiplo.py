#Multiplo.py
#Autor: Juan Tovar
#Fecha: sabado 14 de septiembre de 2019

numero=int(input ("Dame un numero entero:" ))
#El numero que se almaceno se trasnforma en int
#Se guardan valores booleanos para la operacion
#Si el residual es igual a 0, entonces es un multiplo
esmultiplode3=((numero%3)==0)
esmultiplode5=((numero%5)==0)
esmultiplode7=((numero%7)==0)
#Cuand se usa el and el resultado es verdadero si todas las condiciones son verdaderas
#Para or el resultado es es verdadero si almenos una de las condiciones es verdadera
#En python los parentesis para las primeras 2 condiciones va juntas y la tercera sea independiente

if ((esmultiplode3 and esmultiplode5) or esmultiplode7):
    print("Muy bien es correcto ")
else:
    print("Incorrecto intente nuevamente")