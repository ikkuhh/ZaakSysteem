import cgi
import csv
import io
import json

from requests.exceptions import RequestException
from pyramid.config import Configurator
from waitress import serve

from api import CaseApi
from response import JsonResponse


def create_cases(request):
    try:
        body = request.body.decode(request.charset)
    except UnicodeDecodeError:
        return JsonResponse({"error": f"Couldn't decode body as {request.charset}."}, status=400)

    with io.StringIO(body, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        ids = []
        for row in reader:
            data = {key: [value] for key, value in row.items()}

            try:
                ids.append(CaseApi.create_case(data))
            except RequestException:
                return JsonResponse(
                    {"error": "Error while using external Zaaksysteem API.", "result": ids},
                    status=500,
                )

    return JsonResponse({"result": ids})


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('create_cases', '/')
        config.add_view(create_cases, route_name='create_cases')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)
