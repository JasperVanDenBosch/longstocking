from pyramid.view import view_config
from pyramid.response import Response


class PackageController(object):

    def __init__(self, request):
        self.request = request

    @view_config(
        context='ilogue.longstocking.Package:Package',
        request_method='GET',
        renderer='package.mak')
    def get_package(self):
        return {'package':self.request.context}


