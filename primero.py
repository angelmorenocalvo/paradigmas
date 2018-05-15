
def alrededor(self, row, col):
        x=0
        if row>1 and row<filas-1:
            if col>1 and col<columnas-1:
                if self.tabla[row][col].cerrada == False:
                    if self.tabla[row-1][col].detras == '*':
                        x+=1
                    if self.tabla[row][col-1].detras == '*':
                        x+=1
                    if self.tabla[row+1][col-1].detras == '*':
                        x+=1
                    if self.tabla[row+1][col].detras == '*':
                        x+=1
                    if self.tabla[row][col+1].detras == '*':
                        x+=1
                    if col%2==1:    
                        if self.tabla[row+1][col+1].detras == '*':
                            x+=1
                    else:
                        if self.tabla[row-1][col-1].detras == '*':
                            x+=1
        if row == 0 and col == 0:
            if self.tabla[row][col].cerrada == False:
                if self.tabla[row][col+1].cerrada == '*':
                    x+=1
                if self.tabla[row+1][col].cerrada == '*':
                    x+=1
        if row == filas and col == columnas:
            if self.tabla[row][col].cerrada == False:
                if self.tabla[row-1][col-1].cerrada == '*':
                    x+=1
                if self.tabla[row-1][col].cerrada == '*':
                    x+=1
                if self.tabla[row][col-1].cerrada == '*':
                    x+=1
        if row == 0 and col == columnas:
            if self.tabla[row][col].cerrada == False:
                if self.tabla[row][col-1].cerrada == '*':
                     x+=1
                if self.tabla[row+1][col].cerrada == '*':
                    x+=1
                if self.tabla[row+1][col-1].cerrada == '*':
                    x+=1
        if row == filas and col == 0:
            if self.tabla[row][col].cerrada == False:
                if self.tabla[row-1][col].cerrada == '*':
                    x+=1
                if self.tabla[row][col+1].cerrada == '*':
                    x+=1    
        if row == 0 and col != 0 and col != columnas:
            if self.tabla[row][col].cerrada == False:
                if self.tabla[row][col-1].cerrada == '*':
                    x+=1
                if self.tabla[row][col+1].cerrada == '*':
                    x+=1
                if self.tabla[row+1][col-1].cerrada == '*':
                   x+=1
                if self.tabla[row+1][col].cerrada == '*':
                    x+=1
        if row == filas and col != 0 and col != columnas:
            if self.tabla[row][col].cerrada == False:
                if self.tabla[row][col-1].cerrada == '*':
                    x+=1
                if self.tabla[row][col+1].cerrada == '*':
                    x+=1
                if self.tabla[row-1][col-1].cerrada == '*':
                    x+=1
                if self.tabla[row-1][col].cerrada == '*':
                    x+=1
        if columnas%2 == 0 and row != 0 and row != filas and col == 0:
            if self.tabla[row][col].cerrada == False:
                if self.tabla[row-1][col].cerrada == '*':
                    x+=1
                if self.tabla[row-1][col+1].cerrada == '*':
                    x+=1
                if self.tabla[row][col+1].cerrada == '*':
                    x+=1
                if self.tabla[row+1][col].cerrada == '*':
                    x+=1
                if self.tabla[row+1][col+1].cerrada == '*':
                    x+=1
        if columnas%2 == 1 and row != 0 and row != filas and col == 0:
            if self.tabla[row][col].cerrada == False:
                if self.tabla[row-1][col].cerrada == '*':
                    x+=1
                if self.tabla[row+1][col].cerrada == '*':
                    x+=1
                if self.tabla[row][col+1].cerrada == '*':
                    x+=1
        if columnas%2 == 1 and row != 0 and row != filas and col == columnas:
            if self.tabla[row][col].cerrada == False:
                if self.tabla[row-1][col].cerrada == '*':


                    x+=1
                if self.tabla[row-1][col-1].cerrada == '*':
                    x+=1
                if self.tabla[row][col-1].cerrada == '*':
                    x+=1
                if self.tabla[row+1][col].cerrada == '*':
                    x+=1
                if self.tabla[row+1][col-1].cerrada == '*':
                    x+=1
        if columnas%2 == 0 and row != 0 and row != filas and col == columnas:
            if self.tabla[row][col].cerrada == False:
                if self.tabla[row-1][col].cerrada == '*':
                    x+=1
                if self.tabla[row+1][col].cerrada == '*':
                    x+=1
                if self.tabla[row][col-1].cerrada == '*':
                    x+=1 
        return x
