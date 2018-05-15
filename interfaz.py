import gtk
def crear_ventana():
 ventana = gtk.Window()
 ventana.set_default_size (300,300)
 ventana.connect ("destroy", gtk.main_quit)
 etiqueta = gtk.Label ("hola, mundo")
 ventana.add (etiqueta)
 etiqueta.show()
 ventana.show()
crear_ventana()
gtk.main()
