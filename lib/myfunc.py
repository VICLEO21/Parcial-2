#import openpyxl 
from .classes import *

#def datosEval (datos):
#    workbook = openpyxl.load_workbook (datos)
#    hoja = workbook.active
#    data = [ ]
#    for row in hoja.iter_rows (values_only = True):
#        data.append(row)
#    return data

 
def Datos (datosEval):    
    archivo = open((str(datosEval)),'r')
    contenido = archivo.read ()
    print (contenido)
    archivo.close()


def printArbol (nodo): 
    if nodo is not None:
        nodoPadre = nodo
        print(nodoPadre.getArbol())
        printArbol (nodoPadre.izq)
        printArbol (nodoPadre.der)
       
        return 0

def agregaNodos (currentNodo, nuevoNum):

    cola = []
    cola.append (currentNodo)

    while cola:
        currentNodo = cola.pop(0)

        if currentNodo.izq is None:
            currentNodo.izq = nodo (nuevoNum)
            return 0
    
        if currentNodo.der is None:
            currentNodo.der = nodo (nuevoNum)
            return 0
    
        cola.append (currentNodo.izq)
        cola.append (currentNodo.der)

    return 0


