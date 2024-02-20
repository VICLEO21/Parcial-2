
def linkHijo(nodoPadre,nodoHijoIzq=None,nodoHijoDer=None):
    if nodoHijoIzq is not None:
        nodoPadre.izq = nodoHijoIzq

    if nodoHijoDer is not None:
        nodoPadre.der = nodoHijoDer
    pass
    


def LVR (nodo,InOrderArr):
    if nodo is not None:
        nodoPadre = nodo
        LVR (nodoPadre.izq,InOrderArr)
        InOrderArr.append(nodoPadre.valor)
        LVR (nodoPadre.der,InOrderArr)
       
        return InOrderArr

    else:
        pass

    return InOrderArr