import msvcrt as key
import os
def borrar():
    """
    Método para borrar la consola según sistema operativo
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def input_int(mensaje):
    """
    Este método solo aceptara números enteros y devolverá un numero entero
    """
    for caracter in mensaje:
        key.putwch(caracter)
    entrada = ""
    tecla = 0
    while tecla != 13:
        tecla = ord(key.getch())
        # print(tecla) # Print para depuración
        if tecla >= 48 and tecla <= 57:  # Si es numero
            entrada += chr(tecla)
            key.putwch(chr(tecla))
        elif tecla == 45 or tecla == 43:  # Si es + o -
            if len(entrada) < 1:  # Solo si es el primer dígito
                key.putwch(chr(tecla))
                entrada += chr(tecla)
        elif tecla == 8:  # Para la tecla borrar
            key.putwch(chr(tecla))  # Me muevo atrás
            key.putwch(chr(32))  # Escribo espacio para borrar
            key.putwch(chr(tecla))  # Me muevo atrás para colocar el cursor
            entrada = entrada[:-1]  # Borro lo último

    key.putwch("\n")  # Para que ponga un salto de linea
    # Si lo han dejado vacío o solo + o - entonces 0
    if len(entrada) < 1 or entrada == "+" or entrada == "-":
        entrada = 0
    else:
        try:
            entrada = int(entrada)
        except ValueError:
            entrada = 0
    return entrada

def input_float(mensaje):
    """
    Este método solo aceptara números flotante y devolverá un numero flotante
    No acepta la coma como símbolo decimal
    """
    for caracter in mensaje:
        key.putwch(caracter)
    entrada = ""
    tecla = 0
    while tecla != 13:
        tecla = ord(key.getch())
        # print(tecla) # Print para depuración
        if tecla >= 48 and tecla <= 57:  # Si es numero
            entrada += chr(tecla)
            key.putwch(chr(tecla))
        elif tecla == 45 or tecla == 43:  # Si es + o -
            if len(entrada) < 1:  # Solo si es el primer dígito
                key.putwch(chr(tecla))
                entrada += chr(tecla)
        elif tecla == 8:  # Para la tecla borrar
            key.putwch(chr(tecla))  # Me muevo atrás
            key.putwch(chr(32))  # Escribo espacio para borrar
            key.putwch(chr(tecla))  # Me muevo atrás para colocar el cursor
            entrada = entrada[:-1]  # Borro lo último
        elif tecla == 46:  # Para incluir el punto decimal
            if not "." in entrada:  # solo puede haber 1
                if len(entrada) < 1:  # y si es al inicio inserta un cero
                    key.putwch("0")
                    key.putwch(".")
                    entrada += "0."
                else:
                    key.putwch(chr(tecla))
                    entrada += chr(tecla)

    key.putwch("\n")  # Para que ponga un salto de linea
    # Si lo han dejado vacío o solo + o - entonces 0
    if len(entrada) < 1 or entrada == "+" or entrada == "-":
        entrada = ""
    else:
        try:
            entrada = float(entrada)
        except:
            entrada = ""
    return entrada

def input_doble(mensaje_in, mensaje_fin):
    """
    Método que hacepta una frase al inicio y una frase al final, lo introducido por el usuario se encontrá
    entre las dos frases
    """
    entrada = ""
    tecla = 0

    def mensaje(borrar=0):
        # Limpio la linea
        print("\r", " "*borrar, end="\r", flush=True)
        # Escribo la frase
        print("\r", mensaje_in, " ", entrada, " ",
              mensaje_fin, sep="", end="\r", flush=True)
        # Escribo la frase hasta la entrada para posicionar el cursor
        print("\r", mensaje_in, " ", entrada, sep="", end="", flush=True)
    mensaje()
    while tecla != 13:
        tecla = ord(key.getch())
        if tecla != 8:
            entrada += chr(tecla)
        else:  # Para la tecla borrar
            entrada = entrada[:-1]  # Borro lo último
        entrada = entrada.rstrip()  # Elimino espacios y retornos de carro
        # Le sumo 2 ya que tenemos un espacio y longitud de entrada vale uno menos que cuando se escribió
        mensaje(len(mensaje_in)+len(entrada)+len(mensaje_fin)+2)
    print("\n")  # Para que ponga un salto de linea
    return entrada  # Elimino espacios y retornos de carro

def lista_numeros_int():
    """
    Método para pedir al usuario una lista numérica de enteros
    Devuelve una lista
    """
    seguir = True  # Bandera para controlar bloque
    numeros = []  # Lista que contendra los números a analizar

    # Bloque para obtener la lista de números
    while seguir:
        borrar()
        numero = input_int("Introduzca un número: ")
        if numero != "":
            numeros.append(numero)
        else:
            seguir = False  # Cambio la bandera para que salga del bucle, también podría haber usado break
    return numeros

def lista_numeros_float():
    """
    Método para pedir al usuario una lista numérica de flotantes
    Devuelve una lista
    """
    seguir = True  # Bandera para controlar bloque
    numeros = []  # Lista que contendra los números a analizar

    # Bloque para obtener la lista de números
    while seguir:

        numero = input_float("Introduzca un número: ")
        if numero != "":
            numeros.append(numero)
        else:
            seguir = False  # Cambio la bandera para que salga del bucle, también podría haber usado break
    return numeros

def lista_string():
    """
    Método para pedir al usuario una lista de string
    Devuelve una lista de string
    """
    seguir=True # Bandera para controlar bloque
    palabras=[] # Lista que contendra los números a analizar

    # Bloque para obtener la lista de números
    while seguir:
        borrar()
        palabra = input("Introduzca una palabra: ")
        if palabra!="":
            # Necesitaremos control de errores para asegura que la conversión no falla
            palabras.append(palabra)
        else:
            seguir=False # Cambio la bandera para que salga del bucle, también podría haber usado break
    return palabras

def pulsa():
    return chr(ord(key.getch()))