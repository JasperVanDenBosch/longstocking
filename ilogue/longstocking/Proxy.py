import logging
import os, subprocess


class Proxy(object):

    def __init__(self, cacheDir):
        self.cacheDir = cacheDir
        self.log = logging.getLogger(__name__)

    def getLatestArtifactForPackage(self, package):
        cmd = ['pip','install','--download',self.cacheDir,
            '--no-deps','--no-install','--use-mirrors']
        cmd.append(package)
        subprocess.Popen(cmd)

