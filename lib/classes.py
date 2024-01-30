#class rectangulo:
#    def __init__(self, largo, ancho):
#        self.largo = largo
#        self.ancho = ancho
#        pass
#    
#    def __str__(self):
#        return f"Rectángulo de largo {self.largo} y ancho {self.ancho}"
#    def area(self):
#       pass
#   def perimetro(self):
#        return 2*(self.largo+self.ancho)


class articulo():
    def __init__(self,identificador,  marca, nombre, precio=None, pesaje=None, descuento=None, piezas=None): #Los None son valores opcionales y van al final final.
        self.Identificador = identificador
        self.Marca = marca 
        self.Nombre = nombre
        self.Precio = precio
        self.Pesaje = pesaje
        self.Descuento = descuento
        self.Piezas = piezas
        pass

    def __str__(self):
        return f"identificador: {self.Identificador} - marca: {self.Marca} - precio: {self.Precio} - pesaje: {self.Pesaje} - descuento: {self.Descuento} - piezas: {self.Piezas}"
    
    def setPrecio (self,precio):
        self.Precio = precio

    def setPesaje (self, pesaje):
        self.Pesaje = pesaje

    def setDescuento (self, descuento):
        self.Descuento = descuento

    def setPiezas (self, piezas):
        self.Piezas = piezas

class carrito():
    def __init__(self, articulo, precio, iva, descuento):
        self.Articulo = articulo
        self.Precio = precio
        self.Iva = iva 
        self.Descuento = descuento
        pass