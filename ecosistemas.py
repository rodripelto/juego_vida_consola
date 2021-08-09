import random
import os
def defecto():
    """
    Ecosistema por defecto
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = 5
    columna = 5
    turnos = 100
    tiempo = 1.5
    toroidal ="Si"
    vida =[]
    return fila,columna,toroidal,turnos,tiempo,vida

def parpadeador():
    """
    Ecosistema parpadeador
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = 5
    columna = 5
    toroidal = "No"
    turnos = 50
    tiempo = 0.25
    vida =["12","13","14"]
    return fila,columna,toroidal,turnos,tiempo,vida

def estrella():
    """
    Ecosistema estrella
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = 13
    columna = 13
    toroidal = "No"
    turnos = 100
    tiempo = 0.5
    vida =["19","20","21","43","45","47","49","67","69","75","77","80","90","93","95","101","103","121","123","125","127","149","150","151"]
    return fila,columna,toroidal,turnos,tiempo,vida

def cruz():
    """
    Ecosistema estrella
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = 10
    columna = 10
    toroidal = "No"
    turnos = 100
    tiempo = 0.5
    vida =["14","15","16","17","24","27","32","33","34","37","38","39","42","49","52","59","62","63","64","67","68","69","74","77","84","85","86","87"]
    return fila,columna,toroidal,turnos,tiempo,vida

def beso_lengua():
    """
    Ecosistema estrella
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = 10
    columna = 9
    toroidal = "No"
    turnos = 100
    tiempo = 0.5
    vida =["8","9","17","23","24","26","31","33","34","41","50","57","58","60","65","67","68","74","82","83"]
    return fila,columna,toroidal,turnos,tiempo,vida

def reloj():
    """
    Ecosistema estrella
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = 12
    columna = 12
    toroidal = "No"
    turnos = 100
    tiempo = 0.5
    vida =["7","8","19","20","41","42","43","44","49","50","52","57","61","62","64","67","69","76","79","81","83","84","88","90","93","95","96","101","102","103","104","125","126","137","138"]
    return fila,columna,toroidal,turnos,tiempo,vida

def molinillo():
    """
    Ecosistema molinillo
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = 12
    columna = 12
    toroidal = "No"
    turnos = 100
    tiempo = 0.5
    vida =["7","8","19","20","41","42","43","44","49","50","52","57","61","62","64","65","69","76","79","81","83","84","88","90","93","95","96","101","102","103","104","125","126","137","138"]
    return fila,columna,toroidal,turnos,tiempo,vida

def octogono():
    """
    Ecosistema Octógono
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = 8
    columna = 8
    toroidal = "No"
    turnos = 100
    tiempo = 0.5
    vida =["4","5","11","14","18","23","25","32","33","40","42","47","51","54","60","61"]
    return fila,columna,toroidal,turnos,tiempo,vida

def fumarola():
    """
    Ecosistema fumarola
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = 7
    columna = 8
    toroidal = "No"
    turnos = 100
    tiempo = 0.5
    vida =["12","13","18","19","22","23","26","31","35","38","41","43","46","48","49","50","55","56"]
    return fila,columna,toroidal,turnos,tiempo,vida

def pentoad():
    """
    Ecosistema Pentoad
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = 12
    columna = 13
    toroidal = "No"
    turnos = 100
    tiempo = 0.5
    vida =["12","13","25","36","38","46","48","49","50","59","60","61","71","73","84","86","96","97","98","107","108","109","111","119","121","132","144","145"]
    return fila,columna,toroidal,turnos,tiempo,vida

def galaxia_kok():
    """
    Ecosistema Galaxia de Kok
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = 15
    columna = 15
    toroidal = "No"
    turnos = 100
    tiempo = 0.5
    vida =["38","39","40","41","49","50","52","57","63","67","72","78","83","84","93","96","101","102","108","111","115","118","124","125","130","133","142","143","148","154","159","163","169","174","176","177","185","186","187","188"]
    return fila,columna,toroidal,turnos,tiempo,vida

def pentadecathlon():
    """
    Ecosistema Pentadecathlon
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = 9
    columna = 16
    toroidal = "No"
    turnos = 100
    tiempo = 0.5
    vida =["53","55","58","60","65","66","68","71","74","77","79","80","85","87","90","92"]
    return fila,columna,toroidal,turnos,tiempo,vida

def nave():
    """
    Ecosistema nave
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia, Modificado por Rodrigo para que colisione nave y asteroide
    """
    fila = 19
    columna = 20
    toroidal = "Si"
    turnos = 300
    tiempo = 0.25
    vida =["2","23","41","42","43","201","204","225","241","245","262","263","264","265"]
    return fila,columna,toroidal,turnos,tiempo,vida

def diehard():
    """
    Ecosistema Diehard
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = 20
    columna = 20
    toroidal = "Si"
    turnos = 500
    tiempo = 0.25
    vida =["112","126","127","147","151","152","153"]
    return fila,columna,toroidal,turnos,tiempo,vida

def acorn():
    """
    Ecosistema acorn
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = 20
    columna = 20
    toroidal = "No"
    turnos = 5220
    tiempo = 0.25
    vida =["112","134","151","152","155","156","157"]
    return fila,columna,toroidal,turnos,tiempo,vida

def batalla():
    """
    Ecosistema Batalla
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = 15
    columna = 36
    toroidal = "No"
    turnos = 500
    tiempo = 0.25
    vida =["25","59","61","85","86","93","94","107","108","120","124","129","130","143","144","145","146","155","161","165","166","181","182","191","195","197","198","203","205","227","233","241","264","268","301","302"]
    return fila,columna,toroidal,turnos,tiempo,vida

def aleatorio():
    """
    Ecosistema Aleatorio
    Devuelve fila, columna ,toroidal ,turnos ,tiempo , vida
    Rodrigo, Fuente Wikipedia
    """
    fila = random.randint(5,20)
    columna = random.randint(5,20)
    toroidal = random.choice(["Si","No"])
    turnos = 500
    tiempo = 0.25
    total = fila * columna
    vida = []
    for i in range(total//2): # Como máximo permito la mitad de la cuadricula que haya salido
        vida.append(str(random.randint(1,total)))
    return fila,columna,toroidal,turnos,tiempo,vida

def grabar_ecosistema(*arg):
    guardar = ";".join([str(x) for x in arg])
    ruta = os.path.dirname(os.path.realpath(__file__)) + "\\ecosistema.eco"
    try:
        with open(ruta,mode="a",encoding="utf-8") as fichero:
            fichero.write(guardar + "\n")
    except:
        print("Imposible guardar el ecosistema \n fallo en el mutiverso")

def cargar_ecosistemas():
    ecosistemas = []
    ruta = os.path.dirname(os.path.realpath(__file__)) + "\\ecosistema.eco"
    try:
        with open(ruta,mode="r",encoding="utf-8") as fichero:
            for linea in fichero:
                ecosistemas.append(linea.replace("\n","").split(";"))#Quito el salto de línea antes de guardar en la lista
    except:
        print("Imposible encontrar los ecosistemas \n Cuadrante no valido")
    return ecosistemas