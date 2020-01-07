import json
import requests

from decouple import config


class CaseApi:
    URL = "https://hires.zaaksysteem.net/api/v1/case/create"
    HEADERS = {
        "Content-Type": "application/json",
        "API-Key": config("API_KEY"),
        "API-Interface-Id": config("API_INTERFACE_ID"),
    }
    PARAMS = {
        "casetype_id": config("CASETYPE_ID"),
        "source": "webformulier",
    }

    @classmethod
    def create_case(cls, data):
        r = requests.post(cls.URL, headers=cls.HEADERS, params=cls.PARAMS, json={"values": data})
        r.raise_for_status()

        data = r.json()
        return data["result"]["instance"]["number"]
