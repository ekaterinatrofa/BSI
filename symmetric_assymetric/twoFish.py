"""
Source: https://devrescue.com/python-twofish-encryption/

Author: Kateryna Trofymenko
"""

from twofish import Twofish


def ask_for_password_twoFish():
    while True:
        print("Tell me the byte key")
        key = str(input(">"))

        if len(key) < 4:
            print("The key is to short")
            print()

        elif len(key) > 32:
            print("The key is too long")
            print()
        else:
            break

    key = bytes(key, 'utf-8')
    return key


def twofish_encryption(key, msg):
    bs = 16  # block size 16 bytes or 128 bits

    if len(msg) % bs:
        padded_plaintext = str(msg + '%' * (bs - len(msg) % bs)).encode('utf-8')
    else:
        padded_plaintext = msg.encode('utf-8')

    T = Twofish(key)
    ciphertext = b''

    for x in range(int(len(padded_plaintext) / bs)):
        ciphertext += T.encrypt(padded_plaintext[x * bs:(x + 1) * bs])

    return ciphertext


def twofish_decryption(key, msg):
    bs = 16  # block size 16 bytes or 128 bits
    ciphertext = msg
    T = Twofish(key)
    plaintext = b''

    for x in range(int(len(ciphertext) / bs)):
        plaintext += T.decrypt(ciphertext[x * bs:(x + 1) * bs])

    return plaintext.decode('utf-8').strip('%')  # remove padding


def encrypt(files, key):
    for filename in files:
        with open(filename, 'r') as file:
            original = file.read()
        with open(filename, mode="wb") as nfile:
            nfile.write(twofish_encryption(key, original))


def decrypt(files, key):
    for filename in files:
        with open(filename, 'rb') as file:
            encrypted = file.read()
        with open(filename, mode="w", newline="") as nfile:
            nfile.write(twofish_decryption(key, encrypted))
