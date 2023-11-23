import json
import requests
import socket
import time
import random
from settings import AUTH_HOST, COMM_HOST, COMM_PORT
from utils import PersonalPyJWS


import jwt

pjws = PersonalPyJWS()

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

def send_message_udp(message):
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_client.settimeout(5)

    addr = (COMM_HOST, COMM_PORT)
    socket_client.sendto(message, addr)

    try:
        data, server = socket_client.recvfrom(1024)

        socket_client.close()
        return data.decode()

    except socket.timeout:
        print('ERROR: request timed out')
    except Exception as e:
        print(f'ERROR: {e}')

    return None



# def jwt_encode(payload: dict, key: str):
#     return pjws.encode(payload, key, algorithm='HS256')
#
# def jwt_decode(token: str, key: str):
#     return pjws.decode(token, key, algorithms=['HS256'])

def get_random_16bytes_hexa():
    return "".join([('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')[random.randint(0, 15)] for _ in range(32)])

def send_message_by_jwt(key: str, seq_state_number: int, matricula: int):
    key = "secret-key-for-dec7557".encode()
    seq_state = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "INDIGO", "VIOLET"][seq_state_number]
    jti = get_random_16bytes_hexa()

    payload = {
        "sub": "CHEDIMON",
        "aud": COMM_HOST,
        "seq_state_number": seq_state_number + 1,
        "seq_state": seq_state,
        "seq_max": 2,
        "registration": 222222,
        "jti": jti,
        "iat": int(time.time()),
        "exp": int(time.time()) + 30,
        "registration": matricula,
        }

    token = jwt.encode(payload, key)

    print(f"Sending message: \n    {payload}\n    {token}\n\n")

    response = send_message_udp(token.encode())
    print(f"------> Response: \n    {response}\n\n")
    if not response is None:
        response_data = jwt.decode(response, key, algorithms=['HS256'])

        print(f"Response: \n    {response_data}\n    {response}\n\n")
        return False
    else:
        return True
