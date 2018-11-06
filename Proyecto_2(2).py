import os
import json
import random
import time
from random import randint
import os.path as path

laberintoAlea =   [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

laberintoTesting =   [[-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
			   [-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,-1],
			   [-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,0,-1],
			   [-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,0,-1,-1,0,-1],
			   [-1,-1,-1,0,-1,-1,-1,0,0,0,0,-1,-1,0,-1,0,-1,-1,0,-1],
			   [-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,0,-1,-1,0,-1],
			   [-1,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,-1,-1,0,-1],
			   [-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,0,-1],
			   [-1,0,-1,0,0,0,-1,-1,-1,-1,-1,0,0,0,0,0,-1,-1,0,-1],
			   [-1,0,-1,0,-1,0,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,0,-1],
			   [-1,0,0,0,-1,0,0,0,0,0,-1,0,-1,0,0,0,0,0,0,-1],
			   [-1,-1,-1,0,-1,-1,-1,-1,-1,0,-1,0,-1,0,-1,-1,-1,-1,0,-1],
			   [-1,-1,-1,0,-1,-1,-1,-1,-1,0,-1,0,-1,0,0,0,0,-1,-1,-1],
			   [-1,-1,-1,0,-1,-1,-1,-1,-1,0,-1,0,-1,-1,-1,-1,0,-1,-1,-1],
			   [-1,-1,-1,0,-1,-1,-1,-1,-1,0,-1,0,-1,-1,-1,-1,0,-1,-1,-1],
			   [-1,-1,-1,0,0,0,0,0,-1,0,-1,0,-1,0,0,0,0,-1,-1,-1],
			   [-1,-1,-1,0,-1,-1,-1,-1,-1,0,-1,0,-1,0,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,0,-1,-1,-1,-1,-1,0,-1,0,-1,0,0,0,0,0,0,-1],
			   [-1,-1,-1,0,-1,-1,-1,-1,-1,0,0,0,-1,-1,-1,0,-1,0,-1,-1],
			   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1]]

dic				= {'6': ['Right',0, 1,],
					'4': ['Left',0, -1],
					'8': ['Up',-1, 0],
					'2': ['Down',1, 0]}
fila 			= 20
columna 		= 20
X 				= [0,0]
INICIO 			= [0,0]
FIN 			= [19,0]
laberintoJson 	= {}
registro		= []

#  En la siguiente función se generará un camino, el cual tendrá una única entrada y salida
def caminoSalida(laberinto):
	i = 0
	j = randint(2,18)
	INICIO[1] = j
	EvaluarPosicion = 1
	laberinto[i][j] = 0
	
	while (True):
		confirmarPosicion=0
		# Solo tenemos 3 opciones abajo, derecha, izquierda  
		EvaluarPosicion=random.randrange(3)
		
		while (confirmarPosicion == 0) :
			
			if (EvaluarPosicion == 0 and (i+2) < 19):
				confirmarPosicion = 1
				laberinto[i+1][j] = 0
				laberinto[i+2][j] = 0
				i = i+2
				
			elif (EvaluarPosicion == 1 and (j-2) > 0 and laberinto[i][j-1]== -1 and laberinto[i][j-2]== -1):
				confirmarPosicion = 1
				laberinto[i][j-1] = 0
				laberinto[i][j-2] = 0
				j = j-2
				
			elif (EvaluarPosicion == 2 and (j+2) < 19 and laberinto[i][j+1]== -1 and laberinto[i][j+2]== -1):
				confirmarPosicion = 1
				laberinto[i][j+1] = 0
				laberinto[i][j+2] = 0
				j = j+1
				
			else:
				EvaluarPosicion = random.randrange(3)
		# Si llegamos a la fila número 18, diremos que se ha generado un  camino. 
		if (i == 18):
			laberinto[i+1][j] = 0
			FIN[1] = j
			break
# Esta función no permitirá creas caminos alternativos, complementando al anteriormente generado. 
def caminosExtras (laberinto):				
	
	cantFilasAzar = random.randrange(3,6)
	cantColsAzar = random.randrange(3,6)
	
	#caminos por columnas 
	for x in range (cantColsAzar):
		iniCol = random.randrange(3,5)
		terCol = random.randrange(iniCol+1,18)
		colazar = random.randrange(2,18)
		while (iniCol < terCol):
			laberinto[iniCol][colazar] = 0
			iniCol = iniCol + 1
	
	# caminos por filas
	for x in range (cantFilasAzar):
		iniFila = random.randrange(2,5)
		terFila = random.randrange(iniFila+1,18)
		filazar = random.randrange(1,19)
		# Se extrae el 0 de cada Fila
		AUX = []
		for y in range (fila):
			if laberinto[filazar][y] == 0:
				AUX.append(y)
		if 	len(AUX) > 1:
			iniFila = AUX[0]
			terFila = AUX[len(AUX)-1]
		else:
			iniFila = AUX[0]
			terFila = random.randrange(iniFila+1,18)
		
		while (iniFila < terFila):
			laberinto[filazar][iniFila] = 0
			iniFila  = iniFila + 1
# En esta función llamamos a las funciones encargadas de crear los caminos. 
def generarLaberintoAleatorio(laberinto):
	caminoSalida(laberinto)
	caminosExtras(laberinto)

def imprimir_tablero(laberinto, fila, columna, X, tipo):
	
	print(chr(27)+"[1;32m"+" ")
	print ("\t    _    ____  ____  _________  _  _     _____  ____ ")
	print ("\t   / \  /  _ \/  _ \/  __/  __\/ \/ \  //__ __\/  _  \ ")
	print ("\t   | |  | / \|| | //|  \ |  \/|| || |\ || / \  | / \ | ")
	print ("\t   | | /\ |-||| |_\\|  /_|    /| || | \|| | |  | \_/ | ")
	print ("\t   \____|_/ \|\____/\____\_/\_\\_/\_/  \| \_/  \____ / \n")
                                                  
	print(chr(27)+"[1;36m"+" ")
	
    #  Se imprime la lista, formando el tablero donde se realizaran los movimientos.
	if (tipo == 'juego'):
		laberinto[X[0]][X[1]] = 2
		
	for i in range(fila):
		print ("\t", end='')
		for j in range (columna):
			if(laberinto[i][j] == 2) :
				print(chr(27)+"[1;32m"+" o ", end='')
			elif (laberinto[i][j] == -1) :
				print(chr(27)+"[1;36m"+"▓▓▓", end='')
			else :
				print("   ", end='')
		print ('')
# Esta función nos permite movernos al interior del tablero. 
def recorrer_laberinto(laberinto, laberintoJson, fila,  columna, X, registro, FIN):
	
	i = X[0]
	j = X[1]
	imprimir_tablero(laberinto, fila, columna, X, 'juego')
	
	print(chr(27)+"[1;35m"+" ")
	print ("\n\n\t+---------------+---------+")
	print("\t|  Arriba\t|   <8>   |\n\t|  Abajo\t|   <2>   |\n\t|  Derecha\t|   <6>   |\n\t|  Izquierda\t|   <4>   |")
	print ("\t+---------------+---------+\n")
	letra =(input("Ingrese dirección: "))
	
	#Condiciones para que la ficha cambie de lugar.
	if letra in dic:
		
		# obtengo en a todo el dic para esa letra
		A = dic.get(letra)
		
		# obtener el valor de esa clave en el dic.
		if  laberinto[X[0] + A[1]][X[1] + A[2]] == 0: 
			laberinto[X[0]][X[1]]=0
			X[0] = X[0] + A[1]
			X[1] = X[1] + A[2]
			registro.append(A[0])
		else:
			print("Opción no válida! , intente nuevamente :)")
	else:
		print("Opción no válida! , intente nuevamente :)")
	
	# se comprueba si el juego continua o finaliza.
	
	if (X[0]==FIN[0] and X[1]==FIN[1]):
		imprimir_tablero(laberinto, fila, columna, X, 'juego')
		print ("HAS GANADO!!!")
		registro_movimientos(registro)
		crearJson(laberinto, laberintoJson, registro)
		menu(INICIO, FIN, X)	

	else:
		recorrer_laberinto(laberinto, laberintoJson, fila,  columna, X, registro, FIN)		
# se recorre el arreglo que contiene los moviminetos anteriores.
def recorrido (laberinto, X):
		
		# se iguala la posición a una variable 
		a=X[0]
		b=X[1]
		laberinto[a][b]= 2
		for letra in registro:
			if (letra == 'Right'):
				b = b+1
				laberinto[a][b]= 2

			elif (letra== 'Left'):
				b = b-1
				laberinto[a][b]= 2
				
			elif (letra == 'Up'):
				a = a-1
				laberinto[a][b]= 2
				
			elif (letra == 'Down'):
				a = a+1
				laberinto[a][b]= 2
		
		imprimir_tablero(laberinto, fila, columna,X, 'nojuego')
		limpiar_camino(laberinto)
		menu(INICIO, FIN, X)
#Número de moviminetos  		
def registro_movimientos(registro): 
	
	if (len(registro)==0):
		print ("No hay movimientos registrados")
	else:	
		print ("Movimientos realizados: ", len(registro), "\n")

def limpiar_camino(laberinto):
# cuando jugamos la posición que se toma se transforma en dos,
# para tener el camino nuevamente formado
# por 0 utilizaremos esta funcion, cambiando los 2 por 0.	
	for i in range (fila):
		for j in range (columna):
			if (laberinto[i][j] == 2):
				laberinto[i][j] = 0

def limpiar_tablero(laberinto):
	
	for i in range (fila):
		for j in range (columna):
			laberinto[i][j] = -1
								 
def verificarArchivo ():
#veremos si es que nuetro archivo.json existe,
#de ser así sabremos si es que hay movimientos anteriores.
	if path.exists('laberintos.json'):
		
		print ("\n\nCargando movimientos anteriores...\n")
		time.sleep(3)
		os.system ("clear")
	else:
		print ("\n\nNo se han encontrado movimientos anteriores...\n")

def traerArchivo ():
	#si encontramos el archivo.json,
	#lo primero que hacemos es abrirlo 
	#para trabajar en él
    labJson = {}
    if path.exists('laberintos.json'):
        with open('laberintos.json',"r") as file:
            labJson = json.load(file)

    return labJson

def agregarEnsenanza (laberintoJson, idLaberinto, registro):
# en esta función lo que hacemos es guardar en nuestro archivo.json 
# las enseñanzas realizadas, estas en su respectivo laberinto.
    nueva_ensenanza = len(laberintoJson[idLaberinto])
    
    print ("### Se ha agregado la enseñanza", nueva_ensenanza, "al Laberinto", idLaberinto, "### ")
    
    laberintoJson[idLaberinto].append({
        'ensenanza'+str(nueva_ensenanza): registro
        })

    ### Trabajando en json
    with open('laberintos.json',"w") as file:
        json.dump (laberintoJson, file, indent = 4)

def crearJson (laberinto, laberintoJson, registro):
	
	laberintoJson = traerArchivo()
	flag = 0
	#se verifica si es que existe un laberinto igual a otro.
	for lab in laberintoJson:
		if (laberintoJson[lab][0]['coorsLaberinto'] == laberinto):
			flag = 1
			idLaberinto = lab
	
	# si no existe uno igual a otro creamos uno nuevo.
	if flag == 0:
		idLab = len(laberintoJson) + 1
		idLaberinto = 'Laberinto'+str(idLab)
		laberintoJson[idLaberinto]=[]
		laberintoJson[idLaberinto].append({
			'coorsLaberinto': laberinto
			})
	
	agregarEnsenanza (laberintoJson, idLaberinto, registro)

def modoTesting(idLaberinto, INICIO, FIN, X):
	#esta función nos permite dar a conocer lo que el prograa es capaz de hacer. 
	# nos permite saber cual es el camino mas largo y cual es el más corto. 
	
	os.system ("clear")
	ensenanzaLarga = 0
	ensenanzaCorta = 0
	mayor = 0
	menor = 999
	ensenanzas = []
	
	# se actualiza la variable  laberintoJson
	laberintoJson = traerArchivo() 
	
	if (len(laberintoJson[idLaberinto]) <= 2):
		print (chr(27)+"[1;32m\n"+idLaberinto, "tiene tan solo 1 enseñanza, Imposible iniciar modoTesting.")
	
	else:
		cant_ensenanzas = len(laberintoJson[idLaberinto])
		print (chr(27)+"[1;32m"+"\nTesting de \'"+idLaberinto+"\'\n")
		print (chr(27)+"[1;32m"+"+ Cantidad de enseñanzas para",idLaberinto, "es de:", cant_ensenanzas-1)
		
		# for comienza desde 1 ya que hay que saltarse a coorslaberinto. 
		for i in range(1, cant_ensenanzas):
			ensenanzas.append(laberintoJson[idLaberinto][i]['ensenanza'+str(i)])
		
		for i in range (len(ensenanzas)):
			if (len(ensenanzas[i]) > mayor):
				mayor = len(ensenanzas[i])
				ensenanzaLarga = i+1
			
			if (len(ensenanzas[i]) < menor):
				menor = len(ensenanzas[i])
				ensenanzaCorta = i+1
		
		print (chr(27)+"[1;32m"+"\n+ enseñanza"+str(ensenanzaLarga), "es la solución más larga en escapar de \'"+idLaberinto+"\' tomando:", mayor, "pasos")
		print (chr(27)+"[1;32m"+"\n+ enseñanza"+str(ensenanzaCorta), "es la solución más corta en escapar de \'",idLaberinto,"\' tomando:", menor, "pasos")
	
	print ("\n\nEnter para continuar...")
	input ()
	
	# llamada de vuelta al menu principal.
	menu (INICIO, FIN, X) 
		
# función que nos permite visualizar el menú del juego. 			
def menu(INICIO, FIN, X):
	print(chr(27)+"[1;33m"+" ") 
	print("\n\t\t\t\t---------------------MENÚ-----------------------")
	print("\n\t\t\t\t\t-------------------------------\n")
	print("\n\t\t\t\t   ..:::::::: ESCAPA SI PUEDES II  :::::::::..")
	print("\n\n\t\t\t\t\t-------------------------------\n")
	print("-[1] \tJugarAlea\n-[2] \tJugar Testing\n-[3] \tMostrar recorrido\n-[4] \tVer Testing\n-[0] \tSalir")
	opcion = int(input(":"))
	
	if (opcion == 1):
		del registro[:]
		limpiar_tablero(laberintoAlea)
		generarLaberintoAleatorio(laberintoAlea)
		X[0] = INICIO[0]
		X[1] = INICIO[1]
		recorrer_laberinto(laberintoAlea, laberintoJson, fila,  columna, X, registro, FIN)
		
	elif (opcion == 3):
		print("\n\n-[1] \tLaberinto Aleatorio\n-[2] \tLaberinto Testing\n-[0] \tSalir")
		opcion2 = int(input(":"))
		
		if opcion2 == 1:
			X[0] = INICIO[0]
			X[1] = INICIO[1]
			recorrido(laberintoAlea, X)
		
		elif opcion2 == 2:
			
			# Inicio fijo en caso de jugar en modoTesting
			INICIO = [0,2] 	
			X[0] = INICIO[0]
			X[1] = INICIO[1]
			recorrido(laberintoTesting, X)
		
	elif (opcion == 2):
		limpiar_camino(laberintoTesting)
		del registro[:]
		
		# Inicio fijo en caso de jugar en modoTesting
		INICIO = [0,2] 	
		# fin fijo en caso de jugar en modoTesting
		FIN = [19,17] 	
		X[0] = INICIO[0]
		X[1] = INICIO[1]
		recorrer_laberinto(laberintoTesting, laberintoJson, fila,  columna, X, registro, FIN)
		
	elif(opcion == 4):
		idLaberinto = 'Laberinto1'
		modoTesting(idLaberinto, INICIO, FIN, X)
				
	elif (opcion == 0):
		print ("Gracias por jugar :)")
	
	else:
		print ("Opción invalida")

# Main
verificarArchivo()
laberintoJson = traerArchivo()
menu(INICIO, FIN, X)
