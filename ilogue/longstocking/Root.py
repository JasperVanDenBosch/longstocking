import os
from ilogue.longstocking.Package import Package


class Root(object):

    def __init__(self, request):
        self.__name__ = ''
        self.__parent__ = None
        self.request = request
        cacheDir = request.registry.settings.get('longstocking.cache')
        self.loadFiles(cacheDir)

    def __getitem__(self, key):
        return Package(self.request, self, key)

    def loadFiles(self, cacheDir):
        self.files = os.listdir(cacheDir)
