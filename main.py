from settings import MENU_OPTIONS
from utils import menu
from auth_setup import get_keys
from encrypt import Encryptor
from sender import send_post_json

PRIV_KEY = None
PUB_KEY = None

PRIV_KEY_LOCATION = None
PUB_KEY_LOCATION = None

menu_option = None
message = ""

while menu_option != (len(MENU_OPTIONS) - 1):
    title = ('CONFIGURADO:\n' +
             f'     Chave privada: {PRIV_KEY_LOCATION if (not PRIV_KEY_LOCATION is None) else "-- Não configurado --"}\n' +
             f'     Chave pública: {PUB_KEY_LOCATION if (not PUB_KEY_LOCATION is None) else "-- Não configurado --"}\n\n {message}' +
             'Escolha uma opção:')
    message = ""
    menu_option = menu(title, MENU_OPTIONS)

    if menu_option == 0:
        try:
            PRIV_KEY, PUB_KEY, PRIV_KEY_LOCATION, PUB_KEY_LOCATION = get_keys()
            message = ("CHAVES CONFIGURADAS COM SUCESSO! \n\n")
        except ValueError:
            message = "ATENÇÃO: Senha incorreta. \n\n"

    elif menu_option == 1:
        if not (PRIV_KEY is None) and not (PUB_KEY is None):
            e = Encryptor()

            encrypted_key = e.encrypt(PUB_KEY)
            print(encrypted_key)
            user_name = input("Digite seu nome de usuário:\n    - ")

            user_id = ""
            while not user_id.isnumeric():
                user_id = input("Digite seu ID de usuário:\n    - ")

            message = {
                "userName": user_name,
                "userId": int(user_id),
                "iat": 1697415114,
                "exp": 1697425114,
                "pubKeyId": int(user_id),
                "pubKey": encrypted_key,
            }

            message = send_post_json(message)
        else:
            message = "ATENÇÃO: Você precisa configurar uma chave privada e uma chave pública para enviar a chave pública.\n\n"
