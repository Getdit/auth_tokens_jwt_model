AUTH_HOST = "http://172.233.186.185:33444/pubkey"
COMM_HOST = "172.233.186.185"
COMM_PORT = 44555

DEFAULT_KEYPAIR_FILENAME= "id_rsa"
DEFAULT_KEYPAIR_LOCATION= "./"

DEFAULT_KEY = b'This is FOR DEC7557.'
DEFAULT_IV =  bytes.fromhex('2451da89a7ef8d5739a06796b8698e7c')

MENU_OPTIONS = ['Configurar par de chaves', 'Enviar par de chaves', 'Enviar mensagens', 'Sair']

DEFAULT_SALT = bytes.fromhex("f25bc2f1d7f7cb0674e70752f50c02d2")

import base64
DECODE_KEY = "c2VjcmV0LWtleS1mb3ItZGVjNzU1Nw=="
