#Aleatorio.py
#Autor: Juan Tovar
#Fecha: sabado 14 de septiembre de 2019

import random
valor1=float(10.5)
#Aqui se asigna una variable float
#para posteriormente asignarle un valor
def mifuncion():
    #El numero generado por random.randrage se convierte a float
    valor2=float(random.randrange(1,10))
    mensaje= "la suma de {} y {} es {}"
    #se usan meta de sustitucion para el resutado
    print(mensaje.format(valor1,valor2,valor1+valor2))
    #De aqui saldra el resultado de la operacion anterior

mifuncion()
#Aqui ya se ejecuta la funcion que se defino en el codigo