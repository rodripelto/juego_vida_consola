# Importaciones librerias sistema
import os
import time
import msvcrt as key
# Importaciones librerias propias
from metodos_entrada_datos import input_int
import pantalla_inicio

# Clase para la celulas
class Celula:
    """
    Clase para el Objeto Célula contendrá la funcionalidad de la célula así como
    su estado y su ID
    """
    __id = 0
    def __init__(self,nuevo = False):
        """
        En caso de nuevo = True se resetea el contador id de la clase
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

class Tablero:

    def __init__(self):
        self.iniciar() # Aprobecho el contructor/inicializador para lanzar el juego

    def iniciar(self):
        """
        Inicio del juego
        """
        pantalla_inicio.pantalla_inicio()
        continuar = True
        ecosistema = True
        while continuar:
            contador = 0
            cambio = True
            turnos = 100
            if ecosistema:
                filas,columnas = self.numero_celulas()
            self.celulas = self.crear_tablero(filas,columnas)
            self.mostrar_vida(True)
            print("Este es tu ecosistema de vida, ¿que células quieres que tengan vida?")
            vivas = self.lista_string()
            self.inicializar_vidas(vivas)
            self.mostrar_vida()
            print("Este es tu ecosistema de vida, pulsa una tecla para empezar ")
            key.getch() # Espera una pulsación de cualquier tecla
            vivas = 1
            while contador <= turnos and cambio and vivas > 0:
                contador +=1
                self.comprobar_celulas(filas,columnas)
                self.cambiar_celulas()
                self.mostrar_vida()
                print ("\nTurno:",contador)
                vivas, cambio = self.contar_vivas()
                print ("Células vivas:",vivas)
                time.sleep(1.5)
            
            if contador > turnos:
                print("Juego terminado por exceder los 100 turnos")
            elif vivas == 0:
                print("Juego terminado por desaparición de la vida en el ecosistema")
            else:
                print("Juego terminado no hay cambios en el eco sistema" )
            print("Pulsa la tecla S para una nueva partida, otra tecla para salir ")
            tecla = chr(ord(key.getch())) # Espera una pulsación de cualquier tecla y la combierto en caracter
            if tecla.upper() == "S":
                print("¿Quieres un nuevo ecosistema? , pulasa S para nuevo otra tecla para continuar con el mismo")
                tecla = chr(ord(key.getch())) # Espera una pulsación de cualquier tecla y la combierto en caracter
                if tecla.upper() == "S":
                    ecosistema = True
                else:
                    ecosistema = False
            else:
                continuar = False

    def borrar(self):
        """
        Método para borrar la consola según sistema operativo
        """
        if os.name == "posix":
            os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")

    def numero_celulas(self):
        """
        Método para elegir el número de filas y columnas que tendra el ecosistema
        """
        filas= 0
        columnas = 0
        continua = True
        while continua:
            self.borrar()
            filas = input_int("¿Cuantas filas quieres que tenga tú ecosistema?, entre 5 y 20: ")
            if filas < 5 or filas > 20:
                print("Tienes que introducir un número entre 5 y 20")
                time.sleep(4)
            else: 
                continua = False
        continua = True
        while continua:
            self.borrar()
            columnas = input_int("¿Cuantas columnas quieres que tenga tú ecosistema?, entre 5 y 20: ")
            if columnas < 5 or columnas > 20:
                print("Tienes que introducir un número entre 5 y 20")
                time.sleep(4)
            else:
                continua = False
        return filas,columnas

    def lista_string(self):
        """
        Método para pedir al usuario una lista de string
        Devuelve una lista de string
        """
        seguir=True # Bandera para controlar bloque
        palabras=[] # Lista que contendrá los números a analizar

        # Bloque para obtener la lista de números
        while seguir:
            palabra = input("Introduzca el número de la célula y pulse intro, deje en blanco para salir: ")
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
        self.borrar()
        for fila in range(len(self.celulas)):
            linea=""
            for columna in range(len(self.celulas[fila])):
                if inicio:
        # Calculo la longitud total - la longitud del id de la célula para incluir espacios y que todo cuadre
                    espacios = total - len(self.celulas[fila][columna].get_id)
                    linea = linea + "|" + (" " * espacios) + self.celulas[fila][columna].get_id
                else:
                    linea = linea + "|" + self.celulas[fila][columna].estado_visible
            linea += "|"
            print(linea)

    def crear_tablero(self,filas,columnas):
        """
        Creamos el ecosistema
        """   
        celulas =[]
        Celula(True)# Reseteo el contador de id de las celulas
        for i in range(filas):
            fila_celulas = []
            for n in range(columnas):
                fila_celulas.append(Celula())
            celulas.append(fila_celulas)
        return celulas

    def inicializar_vidas(self,vivas):
        """
        Cambiamos el estado de las células según ha elegido el usuario
        """
        for filas_celulas in self.celulas:
            for celula in filas_celulas:
                if celula.get_id in vivas:
                    celula.estado = True

    def comprobar_celulas(self,filas,columnas):
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
                if columna_derecha < columnas:
                    # Si exite columna a la derecha la añado a la lista de celulas a comprobar
                    celulas_al_rededor.append(self.celulas[fila_celulas][columna_derecha])
                    if fila_arriba >= 0:
                        # Si ademas exite fila arriba la añado a la lista de celulas a comprobar
                        celulas_al_rededor.append(self.celulas[fila_arriba][columna_derecha])
                    if fila_abajo < filas:
                        # Si ademas exite fila abajo la añado a la lista de celulas a comprobar
                        celulas_al_rededor.append(self.celulas[fila_abajo][columna_derecha])
                if columna_izquierda >= 0:
                    # Si exite columna a la izquierda la añado a la lista de celulas a comprobar
                    celulas_al_rededor.append(self.celulas[fila_celulas][columna_izquierda])
                    if fila_arriba >= 0:
                        # Si ademas exite fila arriba la añado a la lista de celulas a comprobar
                        celulas_al_rededor.append(self.celulas[fila_arriba][columna_izquierda])
                    if fila_abajo < filas:
                        # Si ademas exite fila abajo la añado a la lista de celulas a comprobar
                        celulas_al_rededor.append(self.celulas[fila_abajo][columna_izquierda])
                if fila_arriba >= 0:
                    # Si exite fila arriba la añado a la lista de celulas a comprobar
                    celulas_al_rededor.append(self.celulas[fila_arriba][columna_celulas])
                if fila_abajo < filas:
                    # Si exite fila abajo la añado a la lista de celulas a comprobar
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

Tablero()