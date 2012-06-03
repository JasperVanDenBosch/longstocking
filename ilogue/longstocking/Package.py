import os, time, fnmatch
from ilogue.longstocking.Artifact import Artifact
from ilogue.longstocking.Proxy import Proxy


class Package(object):

    def __init__(self, request, parent, name):
        self.__name__ = name
        self.name = name
        self.artifacts = []
        self.__parent__ = parent
        self.request = request
        self.cacheDir = request.registry.settings.get('longstocking.cache')
        self.proxy = Proxy(self.cacheDir)
        self.loadFiles()


    def __getitem__(self, key):
        location = os.path.join(self.cacheDir,key)
        if os.path.exists(location):
            return Artifact(self.request, self, location)
        else:
            raise KeyError

    def loadFiles(self):
        for f in os.listdir(self.cacheDir):
            if fnmatch.fnmatch(f.lower(), self.name+'*.tar.gz'):
                filelist.append(f)
        if len(filelist) == 0:
            self.proxy.getLatestArtifactForPackage(self.name)
        for f in filelist:
            a = Artifact(self.request, self, f)
            self.artifacts.append(a)



