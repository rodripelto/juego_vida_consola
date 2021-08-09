from metodos_entrada_datos import borrar,pulsa

def menu_principal():
    opcion = ""
    while not opcion in ("1","2","3","4","5"):
        borrar()
        print("1 Empezar", "2 Ecosistemas por defecto","3 Configurar Ecosistema","4 Cargar Ecosistema","5 Salir",sep="\n")
        print("Escoja una opción: ",end="",flush=True)# Para que funcione un print sin salto de línea antes de una pulsación hay que poner flush a true.
        opcion = pulsa() # Espera una pulsación de cualquier tecla y la convierto en carácter
        
    return opcion

def menu_ecosistemas():

    opcion = ""
    while not opcion in ("01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18"):
        borrar()        
        print("01 Ecosistema por Defecto", "02 Ecosistemas Parpadeador","03 Ecosistema Estrella",
        "04 Ecosistemas Cruz","05 Ecosistema Beso con Lengua","06 Ecosistemas Reloj",
        "07 Ecosistema Molinillo","08 Ecosistemas Octógono","09 Ecosistema Fumarola",
        "10 Ecosistemas Pentoad","11 Ecosistema Galaxia de Kok","12 Ecosistemas Pentadecathlon",
        "13 Ecosistema Nave","14 Ecosistemas Diehard","15 Ecosistema Acorn","16 Ecosistemas Batalla","17 Ecosistema Aleatorio","18 Salir",sep="\n")
        print("Escoja una opción: ",end="",flush=True)
        opcion = pulsa() # Espera dos pulsación de cualquier tecla y la convierto en carácter
        print("\rEscoja una opción: ",opcion,sep="",end="",flush=True)
        opcion += pulsa()
    return opcion

def menu_configurar(filas,columnas,toroidal,turnos,tiempo,malla):
    opcion = ""
    while not opcion in ("1","2","3","4","5","6"):  
        borrar()  
        print(f"1 Tamaño del ecosistema: {filas} x {columnas}", f"2 Ecosistema toroidal: {toroidal}",
        f"3 Turnos máximos: {turnos}",f"4 Tiempo entre turnos: {tiempo}",f"5 Mostrar malla {malla}",f"6 Volver",sep="\n")
        print("Escoja una opción: ",end="",flush=True)
        opcion = pulsa() # Espera una pulsación de cualquier tecla y la convierto en carácter
    return opcion

def menu_cargar_ecosistemas(ecosistemas):
    opcion = -1
    maximo = len(ecosistemas)
    while not 0 <= opcion <= maximo:
        borrar()
        for i in range(maximo):
            print( i+1,"Ecosistema",ecosistemas[i][0])
        print (maximo + 1,"Salir")
        try:
            opcion = int(input("Seleccione una opción y pulse enter: ")) - 1
        except:
            opcion = -1
    return opcion