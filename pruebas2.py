import random
import time
cadena1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&'
cadena2 = 'abcdefghijklmnopqrstuvwxyz=+-:/'

COE  = u'\u2500' # ─ 
CNS  = u'\u2502' # │ 
CES  = u'\u250C' # ┌ 
CSO  = u'\u2510' # ┐ 
CNE  = u'\u2514' # └ 
CON  = u'\u2518' # ┘ 
COES = u'\u252C' # ┬ 
CNES = u'\u251C' # ├ 
CONS = u'\u2524' # ┤ 
CONE = u'\u2534' # ┴ 
CSOM = u'\u2593' # ▒
class Celda:
    def __init__(self, bomba, bombas_alrededor):
        self.delante = CSOM
        self.detras = bomba
        self.prox = bombas_alrededor
        self.marcada = False
        self.cerrada = True
class Tablero:
    def __init__(self,mayusculas,minusculas,filas,columnas,bombas,):
        self.may = mayusculas
        self.min = minusculas
        self.tabla = [[ Celda(0,0) for i in range (columnas)]for j in range (filas)]
        self.cant_bombas = bombas
        self.bombas_restantes = bombas
        self.inicio = 0
        self.filas = filas
        self.columnas = columnas
    def fuera_limites(self,fila,columna):
        return 0<fila>(self.filas-1) or 0<columna>(self.columnas-1)
    def bombas_alrededor(self,fila, columna):
        contador = 0
        if fila%2 == 0:
            rango = [(-1, -1),(-1, 0),(0, -1),(0, 1),(1, -1),(1, 0)]#par
        else:
            rango = [(-1, 1),(-1, 0),(0, -1),(0, 1),(1, 1),(1, 0)]#impar
        for a in range(len(rango)):#len(rango)
            if not self.fuera_limites(fila + rango[a][0],columna + rango[a][1]):
                
                if self.tabla[fila + rango[a][0]][columna + rango[a][1]].detras == '*':
                    contador+=1
                if self.tabla[fila + rango[a][0]][columna + rango[a][1]].marcada == True:
                    contador-= 1
            
        return str(contador)
    def rellenar_bombas2(self,filas,columnas,minas):
        minasA = 0
        while(minasA<minas):
            
            for i in range(filas):
                    for j in range(columnas):
                        if minasA<minas:
                            a = random.randint(0,filas*columnas-1)
                            if a == 0:
                                if self.tabla[i][j].detras == '*':
                                    minasA-=1
                                self.tabla[i][j].detras= '*'
                                minasA+=1
                                
                            elif(self.tabla[i][j].detras != '*'):
                                self.tabla[i][j].detras= ' '
    def imprimir_bombas(self,filas,columnas):
        
        print '   ',
        for a in range(columnas):
            print unichr(ord('a')+ a)+ '  ',
        print '\n',
        print '  ' + CES + (3 * COE) + COES + ((columnas-2)*((3 * COE) + COES)) + (3 * COE) + CSO,
        print '\n',
        for i in range(filas):
            for j in range(columnas):
                print (unichr(ord('A') + i) + ((3 if (i%2==1) else (1)) * (" "))+ CNS + ' ' + self.tabla[i][j].detras if (j== 0) else CNS + ' ' + self.tabla[i][j].detras),
            print CNS,
            print '\n',
            if i==filas-1:
                 print ('  ' + CNE + (columnas-1)*(3*COE + CONE) + 3*(COE) + CON)
            elif (i%2==0):
                print (('  ' + CNE + (columnas)*(COE + COES + COE + CONE) + COE + CSO))
            
            else:
                print (('  ' + CES + (columnas)*(COE + CONE + COE + COES) + COE + CON))


    def imprimir_tablero(self,filas,columnas):
        print 'bombas restantes: ' + str(self.bombas_restantes),
        print 'tiempo jugando: ' + str(time.time () - self.inicio)
        print '   ',
        for a in range(columnas):
            print unichr(ord('a')+ a)+ '  ',
        print '\n',
        print '  ' + CES + (3 * COE) + COES + ((columnas-2)*((3 * COE) + COES)) + (3 * COE) + CSO,
        print '\n',
        for i in range(filas):
            for j in range(columnas):
                print (unichr(ord('A') + i) + ((3 if (i%2==1) else (1)) * (" "))+ CNS + ' ' + self.tabla[i][j].delante if (j== 0) else (CNS + ' ' + self.tabla[i][j].delante)),
            print CNS,
            print '\n',
            if i==filas-1:
                 print (3 if (i%2==1) else (1)) * (" ") +' '+ CNE + (columnas-1)*(3*COE + CONE) + 3*(COE) + CON
            elif (i%2==0):
                print (('  ' + CNE + (columnas)*(COE + COES + COE + CONE) + COE + CSO))
            
            else:
                print (('  ' + CES + (columnas)*(COE + CONE + COE + COES) + COE + CON))

    def cerca_atras(self,filas,columnas):
        for i in range(filas):
            for j in range(columnas):
                if self.tabla[i][j].detras != '*':
                    self.tabla[i][j].detras = self.bombas_alrededor(i,j)
                
                    
def jugar(filas,columnas):
    t.inicio = time.time()
    t.cerca_atras(filas,columnas)
    for i in range(1):
        
        
        t.imprimir_bombas(filas,columnas)
    
        t.imprimir_tablero(filas,columnas)

print "BUSCAMINAS"
print "----------"
print "1-Principiante (9x9, 10 minas)"
print "2-Intermedio (16x16, 40 minas)"
print "3-Experto (16x30, 99 minas)"
print "4-Leer de fichero "
print "5-Salir"

modo=int(input('Escoja opcion: '))
while (modo<1 or modo >5):
    modo=int(input("Introduzca un modo valido, por favor"))
    


if (modo==1):
    filas=columnas=9
    minas = 10
    t = Tablero(cadena1,cadena2,filas,columnas,minas)
    t.rellenar_bombas2(filas,columnas,minas)
    t.imprimir_bombas(filas,columnas)
    jugar(filas,columnas)
elif (modo==2):
    filas = columnas=16
    minas = 40
    t = Tablero(cadena1,cadena2,filas,columnas,minas)
    t.rellenar_bombas2(filas,columnas,minas)
    t.imprimir_bombas(filas,columnas)
    jugar(filas,columnas)
elif (modo == 3):
    filas, columnas, minas = 16,30,99
    t = Tablero(cadena1,cadena2,filas,columnas,minas)
    t.rellenar_bombas2(filas,columnas,minas)
    t.imprimir_bombas(filas,columnas)
    jugar(filas,columnas)
elif(modo == 4):
    print "leer fichero"
    nfichero = raw_input('escriba el nombre del fichero: ')
    t = Tablero(cadena1,cadena2,0,0,0)
    filas,columnas = fichero(nfichero)
    jugar(filas,columnas)
else:
    exit
