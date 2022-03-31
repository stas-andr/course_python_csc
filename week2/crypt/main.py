import simplecrypt
from simplecrypt import decrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt", "r") as inp:
    passwords = inp.read().split('\n')

text = ''

for pass_ in passwords:
    try:
        text = decrypt(pass_, encrypted)
        if text:
            break
    except simplecrypt.DecryptionException:
        continue

print(text)