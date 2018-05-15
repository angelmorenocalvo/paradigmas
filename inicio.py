import pygtk
import gtk

class Aplicacion:
    def __init__(self):
        self.crea_ventana()

    def crea_ventana(self):
        builder = gtk.Builder()
        builder.add_from_file("ejemplo2.glade")
        builder.connect_signals({
            "salir": self.salir,
        })
        tabla = builder.get_object("table1")
        self.etiq = builder.get_object("label1")
        tabla.resize(20,30)
        for fil in range(20):
            for col in range(30):
                btn = gtk.Button(str(fil)+","+str(col))
                btn.show()
                btn.connect("clicked", self.click, (fil,col))
                tabla.attach(btn, col, col+1, fil, fil+1)

    def click(self, widget, data = None):
        self.etiq.set_text("Pulsado boton posicion = "+str(data))
       
    def salir(self, widget, data = None):
        gtk.main_quit()

if __name__ == "__main__":
    Aplicacion()
    gtk.main()
