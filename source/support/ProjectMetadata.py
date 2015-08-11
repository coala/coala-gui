import shelve
import time
import platform
import os


class ProjectMetadata:
    def __init__(self, file=None):
        """
        Accessor for metadata from file.

        :param file: If file is none then use default file.
        """
        if file is None:
            if platform.system() == 'Windows':  # pragma: no cover
                self.file = os.getenv("APPDATA") + '\\coala\\.coala'
            else:
                self.file = os.path.expanduser('~/.local/.coala')
        else:
            self.file = file

    def add_project(self, name, location):
        """
        Opens a shelf to store the data of the project in the file member of
        the object.

        :param name:     Name of the project.
        :param location: Location path of the project.
        """
        shelf = shelve.open(self.file)
        timestamp = time.localtime()
        shelf[name] = (timestamp, location)
        shelf.close()

    def delete_project(self, name):
        """
        Delete project and its metadata from file member of the object.

        :param name: Name of the project.
        """
        shelf = shelve.open(self.file)
        del shelf[name]
        shelf.close()
