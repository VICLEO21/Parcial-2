from lib import *
import pandas as pd


#print ("¿Cuál es mi número? " )
Num = int(input(("¿Cuál es mi número? ")))
#print ("¿Cuál es el nombre del archivo a procesar? " )
NombreArchivo = input ("¿Cuál es el nombre del archivo a procesar? " )

print ("")
print ("Números en archivo, el \033[31mrojo\033[0m es mi número")


data = pd.read_excel(r'C:\Users\Gaels\Downloads\datos-Eval-2 (1).xlsx', sheet_name='Hoja1', engine='openpyxl')
print (data)

#------------------------------------



print ("")
print ("Árbol por extensión:")

arrDatos = [69,75,173,34,7,54,55,185,165,169,8,96,104,37,188,106,98,156,179,29,70,93,36,147,89,6,178,15,137,142,78,32,187,168,6,136,82,123,63,57,114,18,51,172,124,11,99,2,25,74,112,127,159,88,22,33,83,44,197,185,1,92,181,9,77,60,166,128,195,84,200,138,138,5,42,55,36,139,93,106,196,75,135,132,87,169,7,134,127,123,185,155,19,110,193,29,66,109,3,100 ]    
#archivo = open((str(NombreArchivo)),'r')
#arrDatos = [archivo.read ()]
#archivo.close()

nodoRaiz = nodo(arrDatos[0])

for i in range (1,len (arrDatos),1):
    agregaNodos(nodoRaiz,arrDatos [i])
printArbol (nodoRaiz)











#------------------------------------
print ("")
print ("Recorridos de Árbol:")
#------------------------------------





InOrderArr=[]
PreOrderArr=[]
PostOrderArr=[]

nodo1 = nodo(arrDatos[0])
nodo2 = nodo(arrDatos[1])
nodo3 = nodo(arrDatos[2])
nodo4 = nodo(arrDatos[3])
nodo5 = nodo(arrDatos[4])
nodo6 = nodo(arrDatos[5])
nodo7 = nodo(arrDatos[6])
nodo8 = nodo(arrDatos[7])
nodo9 = nodo(arrDatos[8])
nodo10 = nodo(arrDatos[9])
nodo11 = nodo(arrDatos[10])
nodo12 = nodo(arrDatos[11])
nodo13 = nodo(arrDatos[12])
nodo14 = nodo(arrDatos[13])
nodo15 = nodo(arrDatos[14])
nodo16 = nodo(arrDatos[15])
nodo17 = nodo(arrDatos[16])
nodo18 = nodo(arrDatos[17])
nodo19 = nodo(arrDatos[18])
nodo20 = nodo(arrDatos[19])

linkHijo (nodo1,nodo2,nodo3)
linkHijo (nodo2,nodo4,nodo5)
linkHijo (nodo3,nodo6,nodo7)
linkHijo (nodo4,nodo8,nodo9)
linkHijo (nodo5,nodo10,nodo11)
linkHijo (nodo6,nodo12,nodo13)
linkHijo (nodo7,nodo14,nodo15)
linkHijo (nodo8,nodo16,nodo17)
linkHijo (nodo9,nodo18,nodo19)



LVR(nodo1,InOrderArr)
print ("In order:")
print (InOrderArr)

VLR(nodo1,PreOrderArr)
print ("Pre order:")
print (PreOrderArr)

LRV(nodo1,PostOrderArr)
print ("Post order:")
print (PostOrderArr)















#-------------------------------------
print("")
print ("Árbol por ordenamiento: ")

nodoRaiz = None

for i in range (0, len(arrDatos), 1):
    if i == 0:
        nodoRaiz = nodo (Num)
    else:
        nodosOrdenados (nodoRaiz, nodo(arrDatos[i]))

printArbol (nodoRaiz)