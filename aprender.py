import pygtk
pygtk.require('2.0')
import gtk

class Base:
	def hello(self, widget, data = None):
		print 'hello world'
	def delete_event(self, widget, event, date = None):
		print 'delete event occurred'
		return False
	def destroy(self, widget, data = None):
		print 'destroy signal occurred'
		gtk.main_quit()
   
	def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.windo.connect('delete_event', self.destroy)
		
		
		self.window.show()
		
    def main(self):
        gtk.main()

print __name__
if __name__ == "__main__":
    base = Base()
    base.main()

