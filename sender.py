import json
import requests

from settings import AUTH_HOST

def send_post_json(message: dict) -> dict:
    if AUTH_HOST:
        jsonfied = json.dumps(message)
        response = requests.post(AUTH_HOST, headers={'Content-Type': 'application/json'}, data=jsonfied)
        if response.status_code == 200:
            content = "\n".join([f"    {k}: {v}" for k, v in json.loads(response.content).items()])
            return f"STATUS {response.status_code}\n REPONSE:\n{content}\n\n"
        return f"STATUS {response.status_code} REPONSE: {response.content}\n\n"
    else:
        return "ATENÇÃO: AUTH_HOST não configurado.\n\n"