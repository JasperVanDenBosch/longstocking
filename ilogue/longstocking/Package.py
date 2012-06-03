import os, time
from glob import glob
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
        filelist = glob(os.path.join(self.cacheDir,self.name+'*'))
        if len(filelist) == 0:
            self.proxy.getLatestArtifactForPackage(self.name)
            time.sleep(0.1)
        for f in filelist:
            a = Artifact(self.request, self, f)
            self.artifacts.append(a)



