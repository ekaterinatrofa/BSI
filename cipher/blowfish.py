"""
Author: Kateryna Trofymenko
"""

from Crypto.Cipher import Blowfish
from struct import pack


def ask_for_password_blowfish():
    while True:
        print("Tell me the byte key")
        key = str(input(">"))
        if len(key) < 4:
            print("The key is to short")
            print()
        elif len(key) > 56:
            print("The key is too long")
            print()
        else:
            break
    encode_string = key.encode()
    byte_array = bytearray(encode_string)
    return byte_array


def blowfish_encryption(key, message):
    bs = Blowfish.block_size
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    plen = bs - len(message) % bs
    padding = [plen] * plen
    padding = pack('b' * plen, *padding)
    msg = cipher.iv + cipher.encrypt(message + padding)
    return msg


def blowfish_decryption(key, ciphertext):
    bs = Blowfish.block_size
    iv = ciphertext[:bs]
    ciphertext = ciphertext[bs:]

    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    msg = cipher.decrypt(ciphertext)

    last_byte = msg[-1]
    msg = msg[:- (last_byte if type(last_byte) is int else last_byte)]
    return msg


def encrypt(files, key):
    for filename in files:
        with open(filename, 'rb') as file:
            original = file.read()
        with open(filename, mode="wb") as nfile:
            nfile.write(blowfish_encryption(key, original))


def decrypt(files, key):
    for filename in files:
        with open(filename, 'rb') as file:
            encrypted = file.read()
        with open(filename, mode="w", newline="") as nfile:
            nfile.write(blowfish_decryption(key, encrypted).decode())
