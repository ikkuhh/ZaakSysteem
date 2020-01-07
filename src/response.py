import json

from pyramid.response import Response


class JsonResponse(Response):
    def __init__(self, body=None, status=200, content_type='application/json', charset='utf-8', **kwargs):
        body = json.dumps(body)
        super().__init__(body, status, content_type=content_type, charset=charset, **kwargs)
