import os


class Artifact(object):

    def __init__(self, request, parent, location):
        self.__parent__ = parent
        self.request = request
        self.location = location
        self.name = os.path.basename(location)
        self.__name__ = self.name

    def __getitem__(self, key):
        raise KeyError

