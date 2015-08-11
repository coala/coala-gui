import os
from gi.repository import Gtk, Gio, GObject

from source.Searchbar.Searchbar import Searchbar
from source.support.EditableLabel import EditableLabel
from source.scrolledWindow.coalaScrolledWindow import coalaScrolledWindow


class coalaApp(Gtk.Application):
    def __init__(self,  data_path):
        GObject.type_register(coalaScrolledWindow)
        GObject.type_register(Searchbar)
        GObject.type_register(EditableLabel)
        Gtk.Application.__init__(self,
                                 application_id="org.coala",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        gresource = os.path.join(data_path, 'coala.gresource')
        self.resource = Gio.resource_load(gresource)
        Gio.Resource._register(self.resource)

        self.connect("activate", self.activate)

    def activate(self, app):
        pass
