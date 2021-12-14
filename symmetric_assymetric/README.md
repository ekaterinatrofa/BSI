## Symmetric&Asymmetric ciphers

This program allows to encrypt and decrypt files with symmetric and asymmetric ciphers

### Symmetric ciphers

- Blowfish
- Twofish
- RC6
- 
### Asymmetric ciphers

- Diffie-Hellman
- ElGamal

---

#### Blowfish

Blowfish is a symmetric block cipher designed by Bruce Schneier.
It has a fixed data block size of 8 bytes and its keys can vary in length from 32 to 448 bits (4 to 56 bytes).
Blowfish is deemed secure and it is fast. However, its keys should be chosen to be big enough to withstand a brute force attack (e.g. at least 16 bytes).

###### References: 

- [https://pycryptodome.readthedocs.io/en/latest/src/cipher/blowfish.html](https://pycryptodome.readthedocs.io/en/latest/src/cipher/blowfish.html)
---

#### Twofish

Twofish is a symmetric key block cipher with a block size of 128 bits (16 bytes) and key sizes up to 256 bits. 
This cipher is a Feistel Network, which is a cryptographic technique which works by splitting the data block into two equal pieces and applying encryption in multiple rounds. 
In each round, half of the text block is sent through a function, and then “XORed” with the other half of the text block.

###### References: 

- [https://devrescue.com/python-twofish-encryption/](https://devrescue.com/python-twofish-encryption/)

---

#### RC6

RC6 (Rivest Cipher 6) is derived from RC5, and is a symmetric key block cipher. 
It was submitted to the NIST Advanced Encryption Standard (AES) competition. 
It is patented by RSA Security. 
It uses a block size of 128 bits and has keys sizes of 128, 192, and 256 bits, and then up to 2040-bits.

###### References: 

- [https://pypi.org/project/RC6Encryption/](https://pypi.org/project/RC6Encryption/)
- [https://asecuritysite.com/encryption/rc6](https://asecuritysite.com/encryption/rc6)

#### Diffie-Hellman

Diffie–Hellman (DH) key exchange is a method of securely exchanging cryptographic keys over a public channel and was one of the first public-key protocols as originally conceptualized by Ralph Merkle and named after Whitfield Diffie and Martin Hellman. 
DH is one of the earliest practical examples of public key exchange implemented within the field of cryptography. 

###### References: 

- [https://medium.com/@sadatnazrul/diffie-hellman-key-exchange-explained-python-8d67c378701c](https://medium.com/@sadatnazrul/diffie-hellman-key-exchange-explained-python-8d67c378701c)

#### ElGamal
ElGamal encryption is a public-key cryptosystem. 
It uses asymmetric key encryption for communicating between two parties and encrypting the message. 

- [https://github.com/RyanRiddle/elgamal](https://github.com/RyanRiddle/elgamal)


### Required Python packages 

- pycryptodome
- twofish
- RC6Encryption

###### Installation:

```
pip install pycryptodome
```

```
pip install twofish
```

```
pip install RC6Encryption
```

Author:

_Kateryna Trofymenko_