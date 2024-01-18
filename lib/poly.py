class poligono:
    def __init__(self, numLados, tamañoLado):
        self.numLados = numLados
        self.tamañoLado = tamañoLado
        pass

    def __str__(self):
        return f"Número de lados:  {self.numLados} y tamaño de lados: {self.tamañoLado}"

