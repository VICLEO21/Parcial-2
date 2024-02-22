from lib import *

InOrderArr=[]
PreOrderArr=[]
PostOrderArr=[]

nodo1 = nodo(1)
nodo2 = nodo(2)
nodo3 = nodo(3)
nodo4 = nodo(4)
nodo5 = nodo(5)
nodo6 = nodo(6)
nodo7 = nodo(7)

linkHijo (nodo1,nodo2,nodo3)
linkHijo (nodo2,nodo4,nodo5)
linkHijo (nodo3,nodo6,nodo7)





LVR(nodo1,InOrderArr)
print ("In order:")
print (InOrderArr)

#VLR(nodo1,InOrderArr)
#print (PreOrderArr)


#LRV(nodo1,InOrderArr)
#print (PostOrderArr)

#print(nodo1.getArbol())

print("-----------------------------------------------------------------------------------------------------------------------")

# Manera Harcodeada

#nodoRaiz = nodo(16)
#nodo9 = nodo(5)
#nodo10 = nodo(7)
#nodo11 = nodo(12)
#nodo12 = nodo(9)
#nodo13 = nodo(20)
#nodo14 = nodo(18)
#nodo15 = nodo(3)
#nodo16 = nodo(10)
#nodo17 = nodo(14)



#nodosOrdenados (nodoRaiz, nodo9)
#nodosOrdenados (nodoRaiz, nodo10)
#nodosOrdenados (nodoRaiz, nodo11)
#nodosOrdenados (nodoRaiz, nodo12)
#nodosOrdenados (nodoRaiz, nodo13)
#nodosOrdenados (nodoRaiz, nodo14)
#nodosOrdenados (nodoRaiz, nodo15)
#nodosOrdenados (nodoRaiz, nodo16)
#nodosOrdenados (nodoRaiz, nodo17)

#print (nodoRaiz.getArbol())
#print (nodo9.getArbol())
#print (nodo10.getArbol())
#print (nodo11.getArbol())
#print (nodo12.getArbol())
#print (nodo13.getArbol())
#print (nodo14.getArbol())
#print (nodo15.getArbol())
#print (nodo16.getArbol())
#print (nodo17.getArbol())


print("-----------------------------------------------------------------------------------------------------------------------")

# Manera Dinámica
nodoRaiz = None
arrNodos = [16,5,7,12,9,20,18,3,10,14]

for i in range (0, len(arrNodos), 1):
    if i == 0:
        nodoRaiz = nodo (arrNodos[i])
    else:
        nodosOrdenados (nodoRaiz, nodo(arrNodos[i]))

printArbol (nodoRaiz)