from lib import *

hw ()
print ("")

obj_rect = rectangulo (12,4)
print (obj_rect)
print ("Ancho del Rectángulo 1: " +str(obj_rect.ancho)+ " [cm]")
print ("Largo del Rectángulo 1: " +str(obj_rect.largo)+ " [cm]")
print("Perímetro del Rectángulo 1: " + str(obj_rect.perimetro())+ " [cm]")
print("Área del Rectángulo 1: " + str(obj_rect.area())+ " [cm^2]")
print ("")

obj_rect_2 = rectangulo (50,20)
print (obj_rect_2)
print ("Ancho del Rectángulo 2: " +str(obj_rect_2.ancho)+ " [cm]")
print ("Largo del Rectángulo 2: " +str(obj_rect_2.largo)+ " [cm]")
print("Perímetro del Rectángulo 2: " + str(obj_rect_2.perimetro())+ " [cm]")
print("Área del Rectángulo 2: " + str(obj_rect_2.area())+ " [cm^2]")
print("")

obj_rect_3 = rectangulo (0,0)
obj_rect_3.ancho =88
obj_rect_3.largo =44
print (obj_rect_3)
print ("Ancho del Rectángulo 3: " +str(obj_rect_3.ancho)+ " [cm]")
print ("Largo del Rectángulo 3: " +str(obj_rect_3.largo)+ " [cm]")
print("Perímetro del Rectángulo 3: " + str(obj_rect_3.perimetro())+ " [cm]")
print("Área del Rectángulo 3: " + str(obj_rect_3.area())+ " [cm^2]")
print ("")





