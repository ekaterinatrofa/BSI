class DH_Endpoint(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None

    def generate_partial_key(self):
        partial_key = self.public_key1 ** self.private_key
        partial_key = partial_key % self.public_key2
        return partial_key

    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r ** self.private_key
        full_key = full_key % self.public_key2
        self.full_key = full_key
        return full_key

    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c) + key)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c) - key)
        return decrypted_message

    def encrypt_file(self, files):
        for filename in files:
            with open(filename, 'r') as file:
                original = file.read()
                # print(self.encrypt_message(original))
            with open(filename, mode="w", encoding='utf-8') as nfile:
                nfile.write(self.encrypt_message(original))

    def decrypt_file(self, files):
        for filename in files:
            with open(filename, 'r', encoding='utf-8') as file:
                encrypted = file.read()

                # print(self.decrypt_message(encrypted))

            with open(filename, mode="w", newline="") as nfile:
                nfile.write(self.decrypt_message(encrypted))


