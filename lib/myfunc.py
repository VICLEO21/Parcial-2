#import openpyxl 


#def datosEval (datos):
#    workbook = openpyxl.load_workbook (datos)
#    hoja = workbook.active
#    data = [ ]
#    for row in hoja.iter_rows (values_only = True):
#        data.append(row)
#    return data


def Datos (datosEval):    
    archivo = open((datosEval),'r')
    contenido = archivo.read ()
    print (contenido)
    archivo.close()

