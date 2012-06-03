

class Root(object):

    def __init__(self, request):
        self.__name__ = ''
        self.__parent__ = None
        self.request = request

    def __getitem__(self, key):
        raise KeyError
