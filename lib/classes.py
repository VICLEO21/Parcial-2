class nodo():
    def __init__(self, valor,):
        self.valor = valor
        self.izq = None
        self.der = None
        pass

    def getArbol (self):
        strOut = " "
        strOut += f"NodoPadre [{self.valor}]"
        if type(self.izq) != type(None):
            strOut += f" - Izquierda [{self.valor}]->[{self.izq}] "
            
        if self.der is not None:
            strOut += f" - Derecha [{self.valor}]->[{self.der}] "
        
        return strOut 
    
    def __str__(self):        
        return f"Valor: {self.valor}"
    
    
    
    
pass