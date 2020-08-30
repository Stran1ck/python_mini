from simplecrypt import *


with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open("passwords.txt", "r") as inp:
    for line in inp:
        password = line.strip()
        try:
            plaintext = decrypt(password, encrypted)
        except DecryptionException:
            print(password, "Bad password or corrupt")
    print(plaintext.decode('utf8'))
