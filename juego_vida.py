# Importaciones librerías sistema
#import os
import time
# Importaciones librerías propias
from metodos_entrada_datos import input_int, borrar,pulsa,input_float
import pantalla_inicio
import menu
import ecosistemas

# Clase para la células
class Celula:
    """
    Clase para el Objeto Célula contendrá la funcionalidad de la célula así como
    su estado y su ID
    """
    __id = 0
    def __init__(self,nuevo = False):
        """
        En caso de nuevo = True, se reinicia el contador id de la clase
        """
        if nuevo:
            Celula.__id = -1 
        Celula.__id += 1
        self._id = str(Celula.__id)
        self.__estado = False
        self.__nuevo_estado = False
        self.__cambio = False
    @property
    def estado_visible(self):
        """
        Devuelve una O si la célula esta viva y cadena vacía si esta muerta
        """
        if self.__estado:
            return "O"
        else:
            return " "

    def cambiar_estado(self):
        if self.__nuevo_estado != self.__estado:
            self.__cambio = True
            self.__estado = self.__nuevo_estado
        else:
            self.__cambio = False

    def comprobar_estado(self,celulas):
        """
        Lógica para comprobar si la célula vive o muere, si tiene al rededor 2 o 3 vive de lo contrario muere
        """
        vidas = 0
        for otra_celula in celulas:
            if otra_celula.estado:
                vidas += 1
        if self.__estado and 2 <= vidas <= 3:
            self.__nuevo_estado = True
        elif not self.__estado and vidas == 3:
            self.__nuevo_estado = True
        else:
            self.__nuevo_estado = False
        return self

    @property
    def estado(self):
        """
        Retorna el estado de la célula
        """
        return self.__estado

    @estado.setter
    def estado(self,estado):
        self.__estado = estado

    @property
    def get_id(self):
        """
        Retorna el ID de la célula
        """
        return self._id

    @property
    def ver_cambio(self):
        """
        Ver si hay cambio
        """
        return self.__cambio

class Ecosistema:

    def __init__(self):
        pantalla_inicio.pantalla_inicio()
        self.filas,self.columnas,self.toroidal,self.turnos,self.tiempo,vivas = ecosistemas.defecto()
        self.malla ="Si"
        self.vida_inicial = []
        self.menu() # Aprovecho el constructor/ inicializador para lanzar el juego

    def menu(self):
        """
        Menú principal
        """
        continuar = True
        sel_menu = {"1":self.iniciar,"2":self.menu_configuracion_defecto,"3":self.menu_configurar_ecosistema,
        "4":self.menu_cargar_ecosistema}
        while continuar:
            opcion = menu.menu_principal()
            if opcion in sel_menu:
                funcion = sel_menu[opcion]
                funcion()
            elif opcion == "5":
                continuar = False

    def menu_configurar_ecosistema(self):
        """
        Menú de configuración
        """
        continuar = True
        sel_menu = {"1":self.numero_celulas,"2":self.cambio_toroidal,"3":self.cambio_turnos,"4":self.cambio_tiempo,"5":self.cambio_malla}
        while continuar:
            opcion = menu.menu_configurar(self.filas,self.columnas,self.toroidal,self.turnos,self.tiempo,self.malla)
            if opcion in sel_menu:
                funcion = sel_menu[opcion]
                funcion()
            elif opcion == "6":
                continuar = False

    def menu_configuracion_defecto(self):
        """
        Menú para las configuraciones por defecto
        """
        continuar = True
        sel_menu ={"01":ecosistemas.defecto,"02":ecosistemas.parpadeador,"03":ecosistemas.estrella,"04":ecosistemas.cruz,"05":ecosistemas.beso_lengua,
        "06":ecosistemas.reloj,"07":ecosistemas.molinillo,"08":ecosistemas.octogono,"09":ecosistemas.fumarola,"10":ecosistemas.pentoad,
        "11":ecosistemas.galaxia_kok,"12":ecosistemas.pentadecathlon,"13":ecosistemas.nave,"14":ecosistemas.diehard,
        "15":ecosistemas.acorn,"16":ecosistemas.batalla,"17":ecosistemas.aleatorio}
        while continuar:
            opcion = menu.menu_ecosistemas()
            if opcion in sel_menu:
                funcion = sel_menu[opcion]
                self.filas,self.columnas,self.toroidal,self.turnos,self.tiempo,vivas = funcion()
                if opcion !="01":
                    self.celulas = self.crear_tablero()
                    self.inicializar_vidas(vivas)
                    self.iniciar(False)
                else:
                    self.iniciar(True)
                #continuar = False
            elif opcion == "18":
                continuar = False
    
    def menu_cargar_ecosistema(self):
        ecos_cargados = ecosistemas.cargar_ecosistemas()
        continuar = True
        while continuar:
            opcion = menu.menu_cargar_ecosistemas(ecos_cargados)
            if 0 <= opcion < len(ecos_cargados):
                self.filas = int(ecos_cargados[opcion][1])
                self.columnas = int(ecos_cargados[opcion][2])
                self.toroidal = ecos_cargados[opcion][3]
                self.turnos = int(ecos_cargados[opcion][4])
                self.tiempo = float(ecos_cargados[opcion][5])
                vivas = list(ecos_cargados[opcion][6])
                self.celulas = self.crear_tablero()
                self.inicializar_vidas(vivas)
                self.iniciar(False)
            elif opcion == len(ecos_cargados):
                continuar = False

    def cambio_toroidal(self):
        """
        Método para cambiar de sistema toroidal a no toroidal
        """
        if self.toroidal == "Si":
            self.toroidal = "No"
        else:
            self.toroidal = "Si"

    def cambio_malla(self):
        """
        Método para cambiar de sistema toroidal a no toroidal
        """
        if self.malla == "Si":
            self.malla = "No"
        else:
            self.malla = "Si"

    def cambio_turnos(self):
        """
        Método para seleccionar el número de turnos
        """
        self.turnos = 0
        while not 10 <= self.turnos <= 1000:
            borrar()
            self.turnos = input_int("¿Cuantos turnos quieres como máximo, entre 10 y 1000: ")
    
    def cambio_tiempo(self):
        """
        Método para seleccionar el número de turnos
        """
        self.tiempo = -1
        while not 0 <= self.tiempo <= 60:
            borrar()
            self.tiempo = input_float("¿Cuantos tiempo quieres que pase entre turnos, máximo 60 segundos, recuerda que los decimales son con . ")

    def iniciar(self, inicio = True):
        """
        Inicio del juego
        """
        contador = 0
        cambio = True
        if inicio:
            self.celulas = self.crear_tablero()
            self.mostrar_vida(True)
            print("Este es tu ecosistema de vida, ¿que células quieres que tengan vida?")
            vivas = self.lista_string()
            self.inicializar_vidas(vivas)
        self.mostrar_vida()
        print("Este es tu ecosistema de vida, pulsa una tecla para empezar ")
        pulsa() # Espera una pulsación de cualquier tecla
        vivas = 1
        while contador <= self.turnos and cambio and vivas > 0:
            contador +=1
            if self.toroidal == "Si":
                self.comprobar_celulas_todoiral()
            else:
                self.comprobar_celulas()
            self.cambiar_celulas()
            self.mostrar_vida()
            print ("\nTurno:",contador)
            vivas, cambio = self.contar_vivas()
            print ("células vivas:",vivas)
            time.sleep(self.tiempo)
            
        if contador > self.turnos:
            print("Juego terminado por exceder los", self.turnos,"turnos")
        elif vivas == 0:
            print("Juego terminado por desaparición de la vida en el ecosistema")
        else:
            print("Juego terminado no hay cambios en el eco sistema" )
        if inicio:
            print ("¿Quieres guardar el ecosistema S/N: ")
            if pulsa().upper()=="S":
                nombre = input ("Ponle un nombre al ecosistema: ")
                ecosistemas.grabar_ecosistema(nombre,self.filas,self.columnas,self.toroidal,self.turnos,self.tiempo,self.vida_inicial)
        else:
            print("Pulsa una tecla para continuar")
            pulsa()       

    def numero_celulas(self):
        """
        Método para elegir el número de filas y columnas que tendra el ecosistema
        """
        continua = True
        while continua:
            borrar()
            self.filas = input_int("¿Cuantas filas quieres que tenga tú ecosistema?, entre 5 y 20: ")
            if self.filas < 5 or self.filas > 20:
                print("Tienes que introducir un número entre 5 y 20")
                time.sleep(4)
            else: 
                continua = False
        continua = True
        while continua:
            borrar()
            self.columnas = input_int("¿Cuantas columnas quieres que tenga tú ecosistema?, entre 5 y 20: ")
            if self.columnas < 5 or self.columnas > 20:
                print("Tienes que introducir un número entre 5 y 20")
                time.sleep(4)
            else:
                continua = False

    def lista_string(self):
        """
        Método para pedir al usuario una lista de string
        Devuelve una lista de string
        """
        seguir=True # Bandera para controlar bloque
        palabras=[] # Lista que contendrá los números a analizar

        # Bloque para obtener la lista de números
        while seguir:
            palabra = input("Introduzca el número de la célula y pulse la tecla enter, deje en blanco para salir: ")
            if palabra != "":
                palabras.append(palabra)
            else:
                seguir = False # Cambio la bandera para que salga del bucle, también podría haber usado break
        return palabras

    def mostrar_vida(self,inicio = False):
        """
        Método para imprimir en pantalla el estado de las células
        Si inicio = True mostrara el Id de cada Célula
        """
        total = len(str(len(self.celulas) * len(self.celulas[0]))) # Cálculo el máximo de células y cojo su longitud
        if self.malla == "Si":
            separador = "|"
        else:
            separador = " "
        borrar()
        for fila in range(len(self.celulas)):
            linea=""
            for columna in range(len(self.celulas[fila])):
                if inicio:
        # Calculo la longitud total - la longitud del id de la célula para incluir espacios y que todo cuadre
                    espacios = total - len(self.celulas[fila][columna].get_id)
                    linea = linea + separador + (" " * espacios) + self.celulas[fila][columna].get_id
                else:
                    linea = linea + separador + self.celulas[fila][columna].estado_visible
            linea += separador
            print(linea)

    def crear_tablero(self):
        """
        Creamos el ecosistema
        """   
        celulas =[]
        Celula(True)# Resinicio el contador de id de las células
        for i in range(self.filas):
            fila_celulas = []
            for n in range(self.columnas):
                fila_celulas.append(Celula())
            celulas.append(fila_celulas)
        return celulas

    def inicializar_vidas(self,vivas):
        """
        Cambiamos el estado de las células según ha elegido el usuario
        """
        self.vida_inicial = vivas # Hago una copia el estado original para luego poder grabarlo
        for filas_celulas in self.celulas:
            for celula in filas_celulas:
                if celula.get_id in vivas:
                    celula.estado = True

    def comprobar_celulas_todoiral(self):
        for fila_celulas in range(len(self.celulas)):
            for columna_celulas in range(len(self.celulas[fila_celulas])):
                celulas_al_rededor = []
                # Fila de arriba columna de la izquierda
                celulas_al_rededor.append(self.celulas[(fila_celulas - 1) % self.filas][(columna_celulas - 1) % self.columnas])
                # Fila arriba columna central
                celulas_al_rededor.append(self.celulas[(fila_celulas - 1) % self.filas][columna_celulas])
                # Fila arriba columna derecha
                celulas_al_rededor.append(self.celulas[(fila_celulas - 1) % self.filas][(columna_celulas + 1) % self.columnas])
                # Fila de abajo columna de la izquierda
                celulas_al_rededor.append(self.celulas[(fila_celulas + 1) % self.filas][(columna_celulas - 1) % self.columnas])
                # Fila abajo columna central
                celulas_al_rededor.append(self.celulas[(fila_celulas + 1) % self.filas][columna_celulas])
                # Fila abajo columna derecha
                celulas_al_rededor.append(self.celulas[(fila_celulas + 1) % self.filas][(columna_celulas + 1) % self.columnas])
                # Fila central columna izquierda
                celulas_al_rededor.append(self.celulas[fila_celulas][(columna_celulas - 1) % self.columnas])
                # Fila central columna derecha
                celulas_al_rededor.append(self.celulas[fila_celulas][(columna_celulas + 1) % self.columnas])
                self.celulas[fila_celulas][columna_celulas].comprobar_estado(celulas_al_rededor) 

    def comprobar_celulas(self):
        """
        Método para seleccionar las células que hay alrededor y poder comprobar si la célula vive o muere
        """
        for fila_celulas in range(len(self.celulas)):
            for columna_celulas in range(len(self.celulas[fila_celulas])):
                celulas_al_rededor = []
                fila_arriba = fila_celulas - 1
                fila_abajo = fila_celulas + 1
                columna_izquierda = columna_celulas - 1
                columna_derecha = columna_celulas + 1
                if columna_derecha < self.columnas:
                    # Si existe columna a la derecha la añado a la lista de células a comprobar
                    celulas_al_rededor.append(self.celulas[fila_celulas][columna_derecha])
                    if fila_arriba >= 0:
                        # Si ademas existe fila arriba la añado a la lista de células a comprobar
                        celulas_al_rededor.append(self.celulas[fila_arriba][columna_derecha])
                    if fila_abajo < self.filas:
                        # Si ademas existe fila abajo la añado a la lista de células a comprobar
                        celulas_al_rededor.append(self.celulas[fila_abajo][columna_derecha])
                if columna_izquierda >= 0:
                    # Si existe columna a la izquierda la añado a la lista de células a comprobar
                    celulas_al_rededor.append(self.celulas[fila_celulas][columna_izquierda])
                    if fila_arriba >= 0:
                        # Si ademas existe fila arriba la añado a la lista de células a comprobar
                        celulas_al_rededor.append(self.celulas[fila_arriba][columna_izquierda])
                    if fila_abajo < self.filas:
                        # Si ademas existe fila abajo la añado a la lista de células a comprobar
                        celulas_al_rededor.append(self.celulas[fila_abajo][columna_izquierda])
                if fila_arriba >= 0:
                    # Si existe fila arriba la añado a la lista de células a comprobar
                    celulas_al_rededor.append(self.celulas[fila_arriba][columna_celulas])
                if fila_abajo < self.filas:
                    # Si existe fila abajo la añado a la lista de células a comprobar
                    celulas_al_rededor.append(self.celulas[fila_abajo][columna_celulas])
                self.celulas[fila_celulas][columna_celulas].comprobar_estado(celulas_al_rededor)

    def cambiar_celulas(self):
        """
        Método para enviar a cambiar el estado de las células
        """
        for fila_celulas in self.celulas:
            for celula in fila_celulas:
                celula.cambiar_estado()        

    def contar_vivas(self):
        """
        Método para contar cuantas células hay vivas y si hay cambios
        """
        vidas = 0
        cambio = False
        for fila_celulas in self.celulas:
            for celula in fila_celulas:
                if celula.estado:
                    vidas += 1
                cambio = cambio or celula.ver_cambio
        return vidas,cambio

Ecosistema()