from pyramid.view import view_config
from pyramid.response import FileResponse

class ArtifactController(object):

    def __init__(self, request):
        self.request = request

    @view_config(
        context='ilogue.longstocking.Artifact:Artifact',
        request_method='GET')
    def get_artifact(self):
        artifact = self.request.context
        response = FileResponse(artifact.location, 
            request=self.request)
        cdh = 'attachment; filename="{0}"'.format(artifact.name)
        response.headers['Content-Disposition'] = cdh
        return response



