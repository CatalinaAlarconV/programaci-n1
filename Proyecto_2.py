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

# EN LA SIGUIENTE FUNCIÓN SE GENERARÁ UN CAMINO, EL CUAL TENDRÁ UNA ÚNICA ENTRADA Y SALIDA
def caminoSalida(laberinto):
	i = 0
	j = randint(2,18)
	INICIO[1] = j
	EvaluarPosicion = 1
	laberinto[i][j] = 0
	
	while (True):
		confirmarPosicion=0
		# SOLO TENEMOS 3 OPCIONES ABAJO, DERECHA, IZQUIERDA 
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
		# SI LLEGAMOS A LA FILA NÚMERO 18, DIREMOS QUE SE HA GENERADO UN  CAMINO. 	
		if (i == 18):
			laberinto[i+1][j] = 0
			FIN[1] = j
			break
# ESTA FUNCIÓN NO PERMITIRÁ CREAS CAMINOS ALTERNATIVOS, COMPLEMENTANDO AL ANTERIORMENTE GENERADO. 
def caminosExtras (laberinto):				
	
	cantFilasAzar = random.randrange(3,6)
	cantColsAzar = random.randrange(3,6)
	
	### CAMINOS POR COLUMNAS
	for x in range (cantColsAzar):
		iniCol = random.randrange(3,5)
		terCol = random.randrange(iniCol+1,18)
		colazar = random.randrange(2,18)
		while (iniCol < terCol):
			laberinto[iniCol][colazar] = 0
			iniCol = iniCol + 1
	
	### CAMINOS POR FILAS 
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
#EN ESTA FUNCION LLAMAMOS A LAS FUNCIONES ENCARGADAS DE CREAR LOS CAMINOS. 
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
	
    #  SE IMPRIME LA LISTA, FORMANDO EL TABLERO DONDE SE REALIZARAN LOS MOVIMIENTOS. 
	if (tipo == 'juego'):
		laberinto[X[0]][X[1]] = 2
		
	for i in range(fila):
		print ("\t", end='')
		for j in range (columna):
			if(laberinto[i][j] == 2) :
				print(chr(27)+"[1;32m"+" ° ", end='')
			elif (laberinto[i][j] == -1) :
				print(chr(27)+"[1;36m"+"▓▓▓", end='')
			else :
				print("   ", end='')
		print ('')
# ESTA FUNCIÓN NOS PERMITE MOVERNOS AL INTERIOR DEL TABLERO. 
def recorrer_laberinto(laberinto, laberintoJson, fila,  columna, X, registro, FIN):
	
	i = X[0]
	j = X[1]
	imprimir_tablero(laberinto, fila, columna, X, 'juego')
	
	print(chr(27)+"[1;35m"+" ")
	print ("\n\n\t+---------------+---------+")
	print("\t|  Arriba\t|   <8>   |\n\t|  Abajo\t|   <2>   |\n\t|  Derecha\t|   <6>   |\n\t|  Izquierda\t|   <4>   |")
	print ("\t+---------------+---------+\n")
	letra =(input("Ingrese dirección: "))
	
	#CONDICIONES PARA QUE LA FICHA CAMBIE DE LUGAR.
	if letra in dic:
		
		# OBTENGO EN A TODO EL DIC PARA ESA LETRA
		A = dic.get(letra)
		
		# OBTENER EL VALOR DE ESA CLAVE EN EL DIC.
		if  laberinto[X[0] + A[1]][X[1] + A[2]] == 0: 
			laberinto[X[0]][X[1]]=0
			X[0] = X[0] + A[1]
			X[1] = X[1] + A[2]
			registro.append(A[0])
		else:
			print("Opción no válida! , intente nuevamente :)")
	else:
		print("Opción no válida! , intente nuevamente :)")
	
	# SE COMPRUEBA SI EL JUEGO CONTINUA O FINALIZA.
	
	if (X[0]==FIN[0] and X[1]==FIN[1]):
		imprimir_tablero(laberinto, fila, columna, X, 'juego')
		print ("HAS GANADO!!!")
		registro_movimientos(registro)
		crearJson(laberinto, laberintoJson, registro)
		menu(INICIO, FIN, X)	

	else:
		recorrer_laberinto(laberinto, laberintoJson, fila,  columna, X, registro, FIN)
		
# SE RECORRE EL ARREGLO QUE CONTIENE LOS MOVIMINETOS ANTERIORES.
def recorrido (laberinto, X):
		
		# SE IGUALA LA POSICIÓN A UNA VARIABLE.  
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
#NÚMERO DE MOVIMIENTOS 		
def registro_movimientos(registro): 
	
	if (len(registro)==0):
		print ("No hay movimientos registrados")
	else:	
		print ("Movimientos realizados: ", len(registro), "\n")

def limpiar_camino(laberinto):
# CUANDO JUGAMOS LA POSICIÓN QUE SE TOMA SE TRANSFORMA EN DOS,
# PARA TENER EL CAMINO NUEVAMENTE FORMADO
# POR 0 UTILIZAREMOS ESTA FUNCION, CAMBIANDO LOS 2 POR 0. 	
	for i in range (fila):
		for j in range (columna):
			if (laberinto[i][j] == 2):
				laberinto[i][j] = 0

def limpiar_tablero(laberinto):
	
	for i in range (fila):
		for j in range (columna):
			laberinto[i][j] = -1
								 
def verificarArchivo ():
	#VEREMOS SI ES QUE NUETRO ARCHIVO.JSON EXISTE,
	#DE SER ASÍ SABREMOS SI ES QUE HAY MOVIMIENTOS ANTERIORES.
	if path.exists('laberintos.json'):
		
		print ("\n\nCargando movimientos anteriores...\n")
		time.sleep(3)
		os.system ("clear")
	else:
		print ("\n\nNo se han encontrado movimientos anteriores...\n")

def traerArchivo ():
	#SI ENCONTRAMOS EL ARCHIVO.JSON,
	#LO PRIMERO QUE HACEMOS ES ABRIRLO 
	#PARA TRABAJAR EN ÉL. 
    labJson = {}
    if path.exists('laberintos.json'):
        with open('laberintos.json',"r") as file:
            labJson = json.load(file)

    return labJson

def agregarEnsenanza (laberintoJson, idLaberinto, registro):
	# EN ESTA FUNCIÓN LO QUE HACEMOS ES GUARDAR EN NUESTRO ARCHIVO.JSON 
    # LAS ENSEÑANZAS REALIZADAS, ESTAS EN SU RESPECTIVO LABERINTO.
    nueva_ensenanza = len(laberintoJson[idLaberinto])
    
    print ("### Se ha agregado la enseñanza", nueva_ensenanza, "al Laberinto", idLaberinto, "### ")
    
    laberintoJson[idLaberinto].append({
        'ensenanza'+str(nueva_ensenanza): registro
        })

    ### TRABAJANDO CON JSON
    with open('laberintos.json',"w") as file:
        json.dump (laberintoJson, file, indent = 4)

def crearJson (laberinto, laberintoJson, registro):
	
	laberintoJson = traerArchivo()
	flag = 0
	# SE VERIFICA SI ES QUE EXISTE UN LABERINTO IGUAL A OTRO.
	for lab in laberintoJson:
		if (laberintoJson[lab][0]['coorsLaberinto'] == laberinto):
			flag = 1
			idLaberinto = lab
	
	# SI NO EXISTE UNO IGUAL A OTRO CREAMOS UNO NUEVO.
	if flag == 0:
		idLab = len(laberintoJson) + 1
		idLaberinto = 'Laberinto'+str(idLab)
		laberintoJson[idLaberinto]=[]
		laberintoJson[idLaberinto].append({
			'coorsLaberinto': laberinto
			})
	
	agregarEnsenanza (laberintoJson, idLaberinto, registro)

def modoTesting(idLaberinto, INICIO, FIN, X):
	#ESTA FUNCIÓN NOS PERMITE DAR A CONOCER LO QUE EL PROGRAA ES CAPAZ DE HACER. 
	# NOS PERMITE SABER CUAL ES EL CAMINO MAS LARGO Y CUAL ES EL MÁS CORTO. 
	#
	os.system ("clear")
	ensenanzaLarga = 0
	ensenanzaCorta = 0
	mayor = 0
	menor = 999
	ensenanzas = []
	
	# SE ACTUALIZA LA VARIABLE laberintoJson
	laberintoJson = traerArchivo() 
	
	if (len(laberintoJson[idLaberinto]) <= 2):
		print (chr(27)+"[1;32m\n"+idLaberinto, "tiene tan solo 1 enseñanza, Imposible iniciar modoTesting.")
	
	else:
		cant_ensenanzas = len(laberintoJson[idLaberinto])
		print (chr(27)+"[1;32m"+"\nTesting de \'"+idLaberinto+"\'\n")
		print (chr(27)+"[1;32m"+"+ Cantidad de enseñanzas para",idLaberinto, "es de:", cant_ensenanzas-1)
		
		# FOR COMIENZA DESDE 1 YA QUE HAY QUE SALTARSE A coorsLaberinto. 
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
	
	# LLAMADA DE VUELTA AL MENU PRINCIPAL.
	menu (INICIO, FIN, X) 
		
# FUNCIÓN QUE NOS PERMITE VISUALIZAR EL MENÚ DEL JUEGO. 		
def menu(INICIO, FIN, X):
	print(chr(27)+"[1;33m"+" ") 
	print("\n\t\t\t\t---------------------MENÚ-----------------------")
	print("\n\t\t\t\t\t-------------------------------\n")
	print("\n\t\t\t\t   ..:::::::: ESCAPA SI PUEDES  :::::::::..")
	print("\n\n\t\t\t\t\t-------------------------------\n")
	print("-[1] \tJugar\n-[2] \tJugar Testing\n-[3] \tMostrar recorrido\n-[4] \tVer Testing\n-[0] \tSalir")
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
			
			# INICIO FIJO EN CASO DE JUGAR EN modoTesting
			INICIO = [0,2] 	
			X[0] = INICIO[0]
			X[1] = INICIO[1]
			recorrido(laberintoTesting, X)
		
	elif (opcion == 2):
		limpiar_camino(laberintoTesting)
		del registro[:]
		
		# INICIO FIJO EN CASO DE JUGAR EN modoTesting
		INICIO = [0,2] 	
		# FINAL FIJO EN CASO DE JUGAR EN modoTesting
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

# MAIN
verificarArchivo()
laberintoJson = traerArchivo()
menu(INICIO, FIN, X)
