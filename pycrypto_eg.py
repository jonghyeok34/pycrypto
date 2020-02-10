import base64
from Crypto.Cipher import AES
from Crypto import Random
import os


BS = 128
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]

# random_key = os.urandom(32) # 32byte
# random_key = b'DN+&\xa9\xf68\xa8G\x0fe(\xe7\xb5\x020\xd5\xff\xfc\x07\x7f\xe0%\x8c\xcb\xdaC\xe2\xa9\xc5m\xd7'
random_key = b'12345678901234567890123456789012'

class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ).decode('utf-8')

    def decrypt( self, enc ):
        enc = enc.encode('utf-8')
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] )).decode('utf-8')

cipherA = AESCipher(random_key)
enc_email = cipherA.encrypt("cafudibu@simpleemail.in")
enc_password = cipherA.encrypt("123123qq!")

print(enc_email)
print(enc_password)
email = cipherA.decrypt(enc_email)
password = cipherA.decrypt(enc_password)
print(email)
print(password)