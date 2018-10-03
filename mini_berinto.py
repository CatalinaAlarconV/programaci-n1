fila = 20
columna = 20
x=[0,2]
y=[19,17]

registro = []

def imprimir_tablero(fila, columna,x):
    
    for i in range(fila):
        for j in range (columna):
                if(x[0]==i and x[1]==j ) :
                    print(" o ", end='')
                elif (laberinto[i][j] == 1) :
                    print("---", end='')
                else :
                    print("   ", end='')
        print ()
 
def recorrer_laberinto(fila, columna, x):
	i = x[0]
	j = x[1]
	imprimir_tablero(fila,columna,x)
	
	print(" \n Arriba= 8\n Abajo = 2\n Derecha= 6\n Izquierda =4, \n Ingrese dirección:")
	
	letra = int(input())
	
	if (letra==6 and laberinto[i][j+1] == 0):
		x[1] = x[1] +1
		registro.append('Right')
		
	elif (letra==4   and laberinto[i][j-1] == 0) :
		x[1] = x[1] -1
		registro.append('Left')
		
	elif (letra==8 and laberinto[i-1][j] == 0):
		x[0] = x[0] -1
		registro.append('Up')
		
	elif (letra== 2 and laberinto[i+1][j] ==0):
		x[0] = x[0] +1
		registro.append('Down')
		
	elif(letra != 6 or letra !=8 or letra !=2 or letra != 4 or letra !=  ()):
		print("Opción no válida! , intente nuevamente :)")
		
	#Se comprueba si el juego continua o finaliza
	if (x[0]==19 and x[1]==17):
		imprimir_tablero(fila, columna, x)
		print ("HAS GANADO!!!")
		print ("¿Quiere recrear los movimientos realizados? \n (1)SI \n (2)NO")
		opcion2 = int(input())
		
		if (opcion2==1):
			x[0]=0
			x[1]=2
			a=0
			b=2
			print()
			laberinto[a][b]= ' o '
			for i in range(len(registro)):
				if (registro[i] == 'Right'):
					b=b+1
					laberinto[a][b]= ' o '

				if (registro[i] == 'Left'):
					b= b-1
					laberinto[a][b]= ' o '
					
				if (registro[i] == 'Up'):
					a=a-1
					laberinto[a][b]= ' o '
					
				if (registro[i] == 'Down'):
					a= a+1
					laberinto[a][b]= ' o '
					
	
			for i in range(0,20):
				for j in range(0,20):
					if (laberinto[i][j]== 1):
						laberinto[i][j]='---'
					elif (laberinto[i][j]== 0):
						laberinto[i][j]='   '
			for i in range(0,20):
				for j in range(0,20):
					print(laberinto[i][j], end='')
					
				print()
					
			
		menu()
						
		if (opcion2==2):
			print("GRACIAS POR JUGAR :)")
			menu()
	else:
		# ~ print("\n \n \n \n \n \n")
		recorrer_laberinto(fila, columna,x)
	#_=system('clear')
		
def registro_movimientos(): #numero de movimientos
	
	if (len(registro)==0):
		print ("No hay movimientos registrados")
	
	if (len(registro)!=0):  
		for i in range(len(registro)):
			i = i + 1
			
		print ("El Número de movimientos es: \n", i)


laberinto =   [[1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
			   [1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
			   [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],
			   [1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1],
			   [1,1,1,0,1,1,1,0,0,0,0,1,1,0,1,0,1,1,0,1],
			   [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1],
			   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1],
			   [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1],
			   [1,0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,0,1],
			   [1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1],
			   [1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1],
			   [1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,0,1],
			   [1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,1,1,1],
			   [1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1],
			   [1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1],
			   [1,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,1,1],
			   [1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1],
			   [1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,1],
			   [1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,0,1,0,1,1],
			   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]]

def menu():# función que nos mostrará el menú
    print("\n                                ---------------------MENÚ-----------------------")
    print("\n	                                -------------------------------\n")
    print("                                       ..:::::::: ESCAPA SI PUEDES  :::::::..")
    print("\n                                          -------------------------------\n")
    print("(1) Jugar  \n (2)Mostrar movimientos  \n (3) Jugar nuevamente \n (4) Salir ")
    opcion = int(input())
    
    if (opcion==1):
        recorrer_laberinto(fila, columna, x)
    if (opcion==2):
        registro_movimientos()
        menu()
    if (opcion==3):
        x[0] = 0
        x[1] = 2
        del registro[:] # deja el arrgelo en 0
        recorrer_laberinto(fila, columna, x)
      
    else:
        
        print ("Gracias por jugar :)")
		
menu()
