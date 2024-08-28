# Crear un sistema de reserva de Hoteles
#Crear un sista de reverda de hoteles que contegna la sigiente informacion de una reserva
#1. Nombre del cliente
#2.Dias de estancia
#3.Tarifa Diaria
#4. Indicar si el cuarto tiene vista al mar
#Despues de mandar ainprimer valores de cada variable, Hacer algunos cambios y re imprimir

print('**** Sistama de Reserva de Hotel****')
nombre_cliente=str(input("ingrese el nombre del cliente:"))
dias_estancia=int(input("Ingrese la cantidad de dias que desea quedarse:"))

if dias_estancia == 1:
    precio_estatancia= 50
    print("su tarifa es de :", precio_estatancia)
if dias_estancia == 2:
    precio_estatancia = 145
    print("su tarifa es de :",precio_estatancia)
if dias_estancia ==3:
    precio_estatancia = 275
    print("su tarifa es de :", precio_estatancia)
vista_mar=str(input("Desea que su habitacion tenga vista al mar ingrese True o False:"))

if vista_mar == "True":
    print("Se le añade un cargo extra por 50 dolares")
    precio_mar= 50
    totalventas = precio_estatancia + precio_mar
    print("Usted eligio la habitacion con vista al mar:", vista_mar)
    print("Su total por la estancia en nuestro Hotel es de: ", totalventas)

if vista_mar == "False":
    print("No desea habitacion con vista al mar:", vista_mar)
    print("No llevara cargo extra")
    totalventas = precio_estatancia
    print("Su total por la estancia en nuestro Hotel es de: ", totalventas)






