#caracteres Especiales
print('Hola \n Mundo ') # \n es un salto de Linea
print('\testo es una prueba de que si funcionan \t los \t tabuladores')# \t es un tabulador o TAP
#Concatenacion
Cadena1= 'Hola'
Cadena2 = 'mundo'
Resultado= Cadena1 + ' ' + Cadena2
print(Resultado)

Resultado= ''.join([Cadena1, ' ', Cadena2])
print   (Resultado)

#Formateo
Nombre= 'Ricardo'
Edad= '22'
#formateo con F-string
mensaje= f'Hola, me llamo {Nombre} y tengo {Edad} años'
print(mensaje)
#metodo formart
mensaje='Hola, me llamo {} y tengo {} años'.format(Nombre, Edad)
print(mensaje)

#Metodos_cadenas
Cd1= 'Hola Mundo'
print(f'Cadena Orignal:{Cd1}')
mayu= Cd1.upper()#mayuscula Cerrada
print(f'cadena en mayuscula: {mayu}')
print(f'cadena en minuscula: {Cd1.lower()}') #minuscula
cd2= ' Juan Perez '
print(f'cadena con espacios: {cd2}')
print(f'Cadena sin espacios: {cd2.strip()}')#Quitar espacios

#Largo de cadena
Cd3='Hola Mundo!'
largo=len(Cd3)# conteo en almacenamiento de caracteres
print(f'Cadena original: {Cd3}')
print(f'Largo de la cadena:{largo}')

#manejo de Subcadenas
cd4= 'Hola, Mundo'
#-> obtener la subcadena de hola[Incio:fin (sin incluirlo)]
sub_cad= cd4[0:4]
print(f'Subcadena de Hola:{sub_cad}')
#Obterner solo la cadena de Mundo
sub_cad_mun= cd4[6:11]
print(f'cadena de Mundo:{sub_cad_mun}')