from pyramid.view import view_config
from pyramid.response import Response


class RootController(object):

    def __init__(self, request):
        self.request = request

    @view_config(
        context='ilogue.longstocking.Root:Root',
        request_method='GET',
        renderer='root.mak')
    def get_root(self):
        return {'root':self.request.context}

    @view_config(
        context='ilogue.longstocking.Root:Root',
        name='robots.txt',
        request_method='GET')
    def get_robots(self):
        robotstxt ="User-agent: *\nDisallow: /"
        return Response(content_type='text/plain',body=robotstxt)

