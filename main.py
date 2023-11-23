from settings import MENU_OPTIONS
from utils import menu
from auth_setup import get_keys
from encrypt import Encryptor
from sender import send_post_json, send_message_by_jwt

PRIV_KEY = None
PUB_KEY = None

PRIV_KEY_LOCATION = None
PUB_KEY_LOCATION = None

menu_option = None
message = ""

while menu_option != (len(MENU_OPTIONS) - 1):
    PRIV_KEY, PUB_KEY, PRIV_KEY_LOCATION, PUB_KEY_LOCATION = get_keys()
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

    elif menu_option == 2:
        matriculas = [21203167, 21203171]
        send_finished = False

        attempts = 0
        while send_finished == False:
            attempts += 1
            print(f"ATTEMPT {attempts}")
            send_error = False
            for i in range(7):
                if not send_error:
                    matricula = matriculas[i % 2]
                    send_error = send_message_by_jwt("-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAtsccPpsSqLBV5T9yiNVX4Qq1c0d64dQTwx7Zyebl/qGCwSMV\ngXp8PvJ/NuLK2IjOYlnVZ2Nfj6zRpYq8XmPiiRhb/suh/BeMh8PR6BcmcW1SmHkU\n+WOn2JFYSl8qbO2TugXHAcZiaWDj98d1BYNxpz+VyYRWaVPPOOedi+G2U7lFrJk1\n4Y8uYENDBHXe+UYjMqAINK0X7qpCMJS6GlcPkLU9zsW1vl2hJb/E3YN0M5qqmQBS\n+D778OtRpb3lRUOfTpnj5pd7RQ3vXoio7UEvR+Euj07WisA3edn1SpTOppYNPXIN\nomFY/MTWfRH0M7c8Qi+7tjAhFCu3IMAuXS8SnQIDAQABAoIBAC9M18Jb3zhIafIp\nuTov+84BN3Pdy68lcvfLxBC78Ek1AuF4cthPGlgv6TwK9POUc9R/6voWfWRxFNAC\nVz0WHEneQ/BsQj862ONJicjGNOylnfpXW1YutAEXnAGjHxeRY+mAFUAgVtdue5Bj\nzaTfn0no6pp75ODdD4NqbRsGDmkb2TX0lBLyrzmqsOiTc9j/NUNThEXQtAJv9HAb\nXvd0ris7UqFbJq5QiLfGJ93vaBetrmXGgtBjAa8kt+TkLSvsYBKDUfleIxSPMnw6\nXcdKeTFbl62o0ms3xEEdxh6+VUMtC6aaP3TrwF2FfZUcVwt19DapU5U3rHVpp0HL\nUt/ZCAECgYEA2dUb+41xS7pbiGnZWiBHk5WhIUy58ijvLMFjDbN0K++LmZqt1fEZ\nEjz/ElenbPZ2teO9Jsh31cV6sNq4GR0LT7ZgWKjR9B2TF0CZ9BwNJ9kXlCkojTrH\nZyeWYtS1vw5HyXkX6fN3SowQEPA6CKRfWO+R8U1AgUbNLwanqnlp16kCgYEA1s2e\n40WGL0L6aDMt9itNj5Mz61qXd5jADTjbd/OhmMNQULD8tC/vrqm8WwjjqmRrWdks\nV1ANZad6qk7yND8E7gqmJ8oWPub2ZAUawGJ3pPW4E/rpbMDYN8t4mE8poHpS3wCj\n8ycETRe+Bd+ICd9UB1vUsz85+9x9+meU0nQDa9UCgYBU6dDlp0ZR2cxSichzbH/a\nVQqhm3IkprZNQPlm3txbQB6v+u7mpfw68tIPiWG3hP/TeXpDgwPLrhZcmHYJPBwr\nr5ExHmXxfhHXj5Qz5zdtoB+j3sNzAkW2vWTPE9HhLyTmsbCTvxdyVNTydWJ5+fE9\nDu5aHN4XRs03FqYHOxr6OQKBgQCSsehhw/hIzJAgm1s3NAmLFPevMrYgmjQGk57m\ng38HydNO2CAsmlQwz4BwF1kL4/qgaL1sf6I2mzMdnj6wyZz/SEyC/fNFUAxS8F19\np4GYKatmEcRaXjULnaylL+L40rFH1LMi+rFoSN+gOTE5tMg5IlDXfUWHKOTsHtM3\nCr3PZQKBgGrKgp0/w4SxBKPXJCEL6oc3KeTtEqdOJoTXV/Op3Fh30IYZTxO4VlxV\nTcJMP2MBp+iFt6KuLEOAWD+NdW2weaBnw8TSQ04+hKHSaC1YzAElz3wTUxD6HvWE\nxmFcLpbVZ1rSYDXbOmwrFzAyjWa434BDRhDcLlZTGD7x2SqN9SVj\n-----END RSA PRIVATE KEY-----", i, matricula)
                    #send_error = send_message_by_jwt("\n".join(PRIV_KEY), i, matricula)

            if not send_error:
                send_finished = True



