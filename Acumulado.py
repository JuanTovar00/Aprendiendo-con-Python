#Acumulado.py
#Autor: Juan Tovar
#Fecha: sabado 14 de septiembre de 2019

acumulado=int(0)
numero=str("")
#Se declaran las variables con  tipo expicito
while True:
    numero=input("Ingrese un numero entero")
    if numero=="":
        print("vacio.Salida del programa")
        break
    else:
        acumulado+=int(numero)
        #Se realiza un calculo (+=)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))
        #Aqui finalmente saldra del sistema si presiona
        #Enter