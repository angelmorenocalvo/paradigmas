import gtk
import sys


class MyWindow(gtk.ApplicationWindow):
    # a window

    def __init__(self, app):
        gtk.Window.__init__(self, title="GNOME Button", application=app)
        self.set_default_size(250, 50)

        # a button
        button = gtk.Button()
        # with a label
        button.set_label("Click me")
        # connect the signal "clicked" emitted by the button
        # to the callback function do_clicked
        button.connect("clicked", self.do_clicked)
        # add the button to the window
        self.add(button)

    # callback function connected to the signal "clicked" of the button
    def do_clicked(self, button):
        print("You clicked me!")


class MyApplication(gtk.Application):

    def __init__(self):
        gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
