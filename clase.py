import pygtk
import gtk

class Aplication:
	def __init__(self):
		self.crea_gui()

	def crea_gui(self):
		ventana = gtk.Window()
		ventana.show()
		ventana.set_title('hola, mundo')
	
def main():
	Aplication()
	gtk.main()

main()
