from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

from settings import DEFAULT_KEY, DEFAULT_IV

class Encryptor():
    def __init__(self, key=DEFAULT_KEY, iv=DEFAULT_IV):
        self.key = key
        self.iv = iv

    def encrypt(self, data):
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_CBC, self.iv.encode("utf8"))
        return str(base64.b64encode(cipher.encrypt(pad(bytearray(data, "utf-8"), AES.block_size))).decode("utf-8"))

    def decrypt(self, data):
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_CBC, self.iv.encode("utf8"))
        return unpad(cipher.decrypt(base64.b64decode(data)), AES.block_size)
