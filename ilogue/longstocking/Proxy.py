import logging
import os, subprocess


class Proxy(object):
    getting = []

    def __init__(self, cacheDir):
        self.cacheDir = cacheDir
        self.log = logging.getLogger(__name__)

    def getLatestArtifactForPackage(self, package):
        if package in self.getting:
            return
        self.getting.append(package)
        cmd = ['pip','install','--download',self.cacheDir,
            '--no-deps','--no-install','--use-mirrors']
        cmd.append(package)
        subprocess.Popen(cmd)

