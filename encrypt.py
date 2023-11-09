from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
import base64

from settings import DEFAULT_KEY, DEFAULT_IV, DEFAULT_SALT


class Encryptor():
    def __init__(self, key=None, iv=DEFAULT_IV):
        self.key = key or self.generate_keys()
        self.iv = iv

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return str(base64.b64encode(cipher.encrypt(pad(bytes(data, "utf-8"), 32))).decode("utf-8"))

    def decrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv.encode("utf-8"))
        return unpad(cipher.decrypt(base64.b64decode(data)), AES.block_size)

    def generate_keys(self):
        key = PBKDF2(DEFAULT_KEY, DEFAULT_SALT, 32, count=65536, hmac_hash_module=SHA256)

        return key
