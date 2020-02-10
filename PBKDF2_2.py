from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import os
from pbkdf2 import crypt

salt = os.urandom(8)  # 64-bit salt
key = PBKDF2(b'This passphrase is a secret.', salt, 16, 1000)  # 256-bit key

print(key)