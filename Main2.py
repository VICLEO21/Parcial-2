from lib import *



obj_poly_1 = Poligono(10,18)
print(obj_poly_1)
"""print(f"Num lados: {obj_poly_1.numLado }")"""
print(obj_poly_1.nomPoly())
print(obj_poly_1.periPoly())

obj_poly_2 = PoligonoRegular(5,20,2)
print(obj_poly_2)
print(obj_poly_2.nomPoly())
print(obj_poly_2.periPoly())

#print (obj_poly_2.getArea ())
#print (obj_poly_2.chkArea ())

obj_poly_2.setColor ("Verde Vejiga")

print (obj_poly_2.setColor)

num1 = 10
num2 = 0

try:
    div: num1/num2
except ZeroDivisionError:
    print ("No puedes dividir entre cero...")
except TypeError:
    print ("No puedes dividir strings entre Números")
except Exception as e:
    print (f"Error desconocido: {e} ")
