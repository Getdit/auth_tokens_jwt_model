import json
import requests

from settings import AUTH_HOST

def send_post_json(message: dict) -> dict:
    if AUTH_HOST:
        jsonfied = json.dumps(message)
        response = requests.post(AUTH_HOST, data=jsonfied)
        return json.loads(response.json())
    else:
        return "ATENÇÃO: AUTH_HOST não configurado.\n\n"