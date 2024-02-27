
def linkHijo(nodoPadre,nodoHijoIzq=None,nodoHijoDer=None):
    if nodoHijoIzq is not None:
        nodoPadre.izq = nodoHijoIzq

    if nodoHijoDer is not None:
        nodoPadre.der = nodoHijoDer
    pass


def LVR (nodo,InOrderArr): #Left Visit Right (In Order)
    if nodo is not None:
        nodoPadre = nodo
        LVR (nodoPadre.izq,InOrderArr)
        InOrderArr.append(nodoPadre.valor)
        LVR (nodoPadre.der,InOrderArr)
       
        return InOrderArr

    else:
        pass

    return InOrderArr


def VLR(Nodo, PreOrderArr):  #Visit Left Right (Pre Order)
    if Nodo is not None:
        nodoPadre = Nodo
        PreOrderArr.append(nodoPadre.valor)
        LVR(nodoPadre.izq, PreOrderArr)        
        LVR(nodoPadre.der, PreOrderArr)
    else:
        pass

    return PreOrderArr




def LRV(Nodo, PostOrderArr): #Left Right Visit (Post Order)
    if Nodo is not None:
        nodoPadre = Nodo
        LVR(nodoPadre.izq, PostOrderArr)        
        LVR(nodoPadre.der, PostOrderArr)
        PostOrderArr.append(nodoPadre.valor)        
    else:
        pass

    return PostOrderArr


def printArbol (nodo): 
    if nodo is not None:
        nodoPadre = nodo
        print(nodoPadre.getArbol())
        printArbol (nodoPadre.izq)
        printArbol (nodoPadre.der)
       
        return 0

def nodosOrdenados (nodoPadre, newNodo):
    if newNodo.valor < nodoPadre.valor : #Izquierda
        if nodoPadre.izq is None:
            nodoPadre.izq = newNodo
        else:
            nodosOrdenados (nodoPadre.izq, newNodo)   

    if newNodo.valor > nodoPadre.valor: #Derecha
        if nodoPadre.der is None:
            nodoPadre.der = newNodo
        else:
            nodosOrdenados (nodoPadre.der, newNodo)
    pass