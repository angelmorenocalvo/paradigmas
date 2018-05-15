import pygtk
pygtk.require('2.0')
import gtk
        
 
class HelloWorld:
    def onClick(self, widget, data=None):
        self.child.show()
 
    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False
    
    def child_delete_event(self, widget, event, data=None):
        self.child.hide()
        return True
 
    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()
 
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.child = gtk.Window(gtk.WINDOW_TOPLEVEL)
    
        self.window.connect("delete_event", self.delete_event)
        self.child.connect("delete_event", self.child_delete_event)
    
        self.window.connect("destroy", self.destroy)
        self.child.connect("destroy", self.destroy)
    
        self.window.set_border_width(10)
    
        self.button = gtk.Button("Mostrar ventana")
        self.cbutton = gtk.Button("Boton de prueba")
    
        self.button.connect("clicked", self.onClick, None)
    
        self.window.add(self.button)
        self.child.add(self.cbutton)
    
        self.button.show()
        self.cbutton.show()
        self.window.show()
        self.child.show()
 
    def main(self):
        gtk.main()
 
if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()
'''
# Load in pygtk and gtk

import pygtk
pygtk.require('2.0')
import gtk

# Define the main window

class Whc:
    def __init__(self):
        # Window and framework
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)

        # Box for multiple widgits
        self.box1 = gtk.VBox(False, 0)
        self.window.add(self.box1)

        # Three buttons
        self.button = gtk.Button("First Button")
        self.button.connect("clicked", self.hello, "Piano")
        self.box1.pack_start(self.button, True, True, 0)
        self.button.show()

        self.nextbutton = gtk.Button("Second Button")
        self.nextbutton.connect("clicked", self.hello, "Pineapple")
        self.box1.pack_start(self.nextbutton, True, True, 0)
        self.nextbutton.show()

        self.lastbutton = gtk.Button("Quit")
        self.lastbutton.connect("clicked", self.destroy)
        self.lastbutton.connect_object("clicked",gtk.Widget.destroy, self.window)
        self.box1.pack_start(self.lastbutton, True, True, 0)
        self.lastbutton.show()

        # Show the box
        self.box1.show()

        # Show the window
        self.window.show()

# Callback function for use when the button is pressed

    def hello(self, widget, info):
        print "Button %s was pressed" % info
        print "Hello World"

# Destroy method causes appliaction to exit
# when main window closed

    def destroy(self, widget, data=None):
        gtk.main_quit()

# All PyGTK applications need a main method - event loop

    def main(self):
        gtk.main()

if __name__ == "__main__":
    base = Whc()
    base.main()
''''''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygtk
pygtk.require('2.0')
import gtk
class HolaMundo:
    def hola (self, wid, data=None):
        print "\n\n\n\t\t"
        print "Decía que 'Hola, mundo', pero lo decía en inglés"
        print "\n\n\n"
    def borra_evento (self, wid, ev, data=None):
        print "\n ocurrió delete_event -> ejecutado el método borra_evento\n"
        return False
    def destruye (self, wid, data=None):
        print "\n ocurrió señal destroy --> ejecutado el método destruye"
        gtk.main_quit()
    
    def __init__(self):
        self.ventana = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.ventana.connect("delete_event", self.borra_evento)
        self.ventana.connect("destroy", self.destruye)
        self.ventana.set_border_width(100)
        self.boton = gtk.Button("Hello World") # texto en inglés, intencionado
        self.boton.connect("clicked", self.hola, None)
        #self.boton.connect_object("clicked", gtk.Widget.destroy, self.ventana)
        #self.boton.connect_object("clicked", gtk.Widget.destroy, self.boton)
        self.ventana.add(self.boton) #destroy se produce cuando
        self.boton.show() #la función asociada a delete_event devuelve False
        self.ventana.show()
    def main(self):
        gtk.main()
if __name__ == "__main__":
    hola = HolaMundo()
    hola.main()
'''
'''
#!/usr/bin/env python

# example helloworld.py

import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld:

    # This is a callback function. The data arguments are ignored
    # in this example. More on callbacks below.
    def hello(self, widget, data=None):
        print "Hello World"

    def delete_event(self, widget, event, data=None):
        # If you return FALSE in the "delete_event" signal handler,
        # GTK will emit the "destroy" signal. Returning TRUE means
        # you don't want the window to be destroyed.
        # This is useful for popping up 'are you sure you want to quit?'
        # type dialogs.
        print "delete event occurred"

        # Change FALSE to TRUE and the main window will not be destroyed
        # with a "delete_event".
        return False

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    def __init__(self):
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    
        # When the window is given the "delete_event" signal (this is given
        # by the window manager, usually by the "close" option, or on the
        # titlebar), we ask it to call the delete_event () function
        # as defined above. The data passed to the callback
        # function is NULL and is ignored in the callback function.
        self.window.connect("delete_event", self.delete_event)
    
        # Here we connect the "destroy" event to a signal handler.  
        # This event occurs when we call gtk_widget_destroy() on the window,
        # or if we return FALSE in the "delete_event" callback.
        self.window.connect("destroy", self.destroy)
    
        # Sets the border width of the window.
        self.window.set_border_width(10)
    
        # Creates a new button with the label "Hello World".
        self.button = gtk.Button("Hello World")
    
       
        self.button.connect("clicked", self.hello, None)
    
       
        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
    
        # This packs the button into the window (a GTK container).
        self.window.add(self.button)
    
        # The final step is to display this newly created widget.
        self.button.show()
    
        # and the window
        self.window.show()

    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()




'''
