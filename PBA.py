from Crypto.Cipher import AES

key = b'DN+&\xa9\xf68\xa8G\x0fe(\xe7\xb5\x020\xd5\xff\xfc\x07\x7f\xe0%\x8c\xcb\xdaC\xe2\xa9\xc5m\xd7'

message = 'this is my super secret message'
cipher = AES.new(key)


def pad(s):
    return s + ((16-len(s) % 16) * '{')


def encrypt(plaintext):
    global cipher
    return cipher.encrypt(pad(plaintext))


def decrypt(ciphertext):
    global cipher
    dec = cipher.decrypt(ciphertext).decode('utf-8')
    l = dec.count('{')
    return dec[:len(dec)-l]


print("Message:", message)
encrypted = encrypt(message)
decrypted = decrypt(encrypted)

print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)
