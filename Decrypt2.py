from random import choice
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


#How to decrypt with just the salt and password


salt = #PUT binary salt here
password = "PUT password here"



KEY = PBKDF2(password, salt, dkLen = 32)

#Make sure you have the correct file you want to open "filename.bin"
with open("encrypt.bin", "rb") as f:
    iv = f.read(16)
    data = f.read()

cipher = AES.new(KEY, AES.MODE_CBC, iv = iv)
message = unpad(cipher.decrypt(data), AES.block_size)

print("message: ", message)
