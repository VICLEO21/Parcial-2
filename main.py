from lib import *



#def info ():
#    Número = int(input ("¿Cuál es mi número? " ))
#    NombreArchivo = input ("¿Cuál es el nombre del archivo a procesar? " ) 
#    return Número 

#datosEval (NombreArchivo)


print ("¿Cuál es mi número? " )
Num = input(int())
print ("¿Cuál es el nombre del archivo a procesar? " )
NombreArchivo = input ( )

print ("Números en archivo, el \033[31mrojo\033[0m es mi número")

Datos (NombreArchivo)
#------------------------------------

#meter datos-Eval-2.xlsx a arrDatos
arrDatos = []
print ("")
print ("Árbol por extensión:")

nodoRaiz = nodo(Num)
   
for i in range (1,len (arrDatos),1):
    agregaNodos(nodoRaiz,arrDatos [i])

printArbol (nodoRaiz)

#------------------------------------
print ("")
print ("Recorridos de Árbol:")
print ("")
print ("In order")
#------------------------------------
print ("")
print ("Pre order")
#------------------------------------
print ("")
print ("Post order")