"""
Blowfish

Blowfish is a symmetric block cipher designed by Bruce Schneier.
It has a fixed data block size of 8 bytes and its keys can vary in length from 32 to 448 bits (4 to 56 bytes).

Twofish

Twofish is a symmetric key block cipher with a block size of 128 bits (16 bytes) and key sizes up to 256 bits.

RC6

RC6 (Rivest Cipher 6) is derived from RC5, and is a symmetric key block cipher
"""
import blowfish
# import rc6
import twoFish
import helper

if __name__ == "__main__":
    while True:
        print("1 - Blowfish")
        print("2 - Twofish")
        print("3 - RC6")
        print("0 - exit")
        choice = input("Choose the type of cipher ")
        print()
        if choice == "1":
            folder_name = input("Provide the folder name for creating folder and files ")
            folder = helper.make_folder(folder_name)
            blowfish.encrypt(folder, blowfish.ask_for_password_blowfish())
            print("Do you want to decrypt?")
            i = str(input())
            if i == "yes":
                blowfish.decrypt(folder, blowfish.ask_for_password_blowfish())
            elif i == "no":
                print('You refuse to decrypt files')
        elif choice == "2":
            folder_name = input("Provide the folder name for creating folder and files ")
            folder = helper.make_folder(folder_name)
            twoFish.encrypt(folder, twoFish.ask_for_password_twoFish())
            print("Do you want to decrypt?")
            i = str(input())
            if i == "yes":
                twoFish.decrypt(folder, twoFish.ask_for_password_twoFish())
            elif i == "no":
                print('You refuse to decrypt files')
        elif choice == "3":
            folder_name = input("Provide the folder name for creating folder and files ")
            folder = helper.make_folder(folder_name)
            rc6.encrypt(folder, rc6.ask_for_password_rc6())
            i = str(input())
            if i == "yes":
                print("Do you want to decrypt?")
                rc6.decrypt(folder, rc6.ask_for_password_rc6())
            elif i == "no":
                print('You refuse to decrypt files')
        elif choice == "0":
            break
