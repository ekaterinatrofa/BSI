"""
Author: Kateryna Trofymenko
"""

from RC6Encryption import RC6Encryption
import os


def ask_for_password_rc6():
    while True:
        print("Tell me the byte key")
        key = str(input(">"))

        if len(key) < 8:
            print("The key is to short")
            print()

        elif len(key) > 32:
            print("The key is too long")
            print()

        else:
            break
    encode_string = key.encode()
    byte_array = bytearray(encode_string)
    return byte_array

def rc6_encryption(key, res):
    bs = 16

    if len(res) % bs:  # add padding
        padded_plaintext = str(res + '%' * (bs - len(res) % bs)).encode('utf-8')
    else:
        padded_plaintext = res.encode('utf-8')
    rc6 = RC6Encryption(key)
    ciphertext = b''
    for x in range(int(len(padded_plaintext) / bs)):
        ciphertext += (rc6.blocks_to_data(rc6.encrypt(padded_plaintext[x * bs:(x + 1) * bs])))

    # print(ciphertext)
    return ciphertext


def rc6_decryption(key, cipher):
    bs = 16  # block size 16 bytes or 128 bits
    rc6 = RC6Encryption(key)
    plaintext = b''

    for x in range(int(len(cipher) / bs)):
        plaintext += rc6.blocks_to_data(rc6.decrypt(cipher[x * bs:(x + 1) * bs]))

    # print(plaintext.decode('utf-8').strip('%'))

    return plaintext.decode('utf-8').strip('%')

def encrypt(files, key):
    for filename in files:
        with open(filename, 'r') as file:
            original = file.read()
        with open(filename, mode="wb") as nfile:
            nfile.write(rc6_encryption(key, original))


def decrypt(files, key):
    for filename in files:
        with open(filename, 'rb') as file:
            encrypted = file.read()
            # print(Bf_decode(key, encrypted).decode())
        with open(filename, mode="w", newline="") as nfile:
            nfile.write(rc6_decryption(key, encrypted))

