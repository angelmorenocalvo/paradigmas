def prueba(filas,columnas):
    cadena1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&'
    cadena2 = 'abcdefghijklmnopqrstuvwxyz=+-:/'
    cadena3 = []
    
    for i in range(filas):
        for j in range(columnas):
            cadena3.append(str(i)+str(j))
            #cadena3.append( cadena1[i]+ cadena2[j])
    return cadena3
    
a = prueba(input("numero de filas"),input("numero de columnas"))

print a

#ahora hay que integrar esta lista en un diccionario con las celdas necesarias
#y este seria nuestro tablero 

#ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&
#abcdefghijklmnopqrstuvwxyz=+-:/
#dicciconario = {hola: 1,hola2:2}

'''
class celda(object):

    def __init__(self,bomba):
        self.casilla = u'\u2593'
        self.detras = bomba

    def abrir(self):
        if self.detras == True:
            print 'fin del juego'
        else:
            self.casilla = self.detras

    def recursiva():
        pass

class tablero:
    def __init__(self, ):
        matriz = rellenar(fila,columna)
'''

'''def comprobar():
    while(f<
'''
