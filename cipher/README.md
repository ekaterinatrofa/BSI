## Cipher

### Implemented ciphers

_Blowfish, Twofish and RC6_

---

### Blowfish

Blowfish is a symmetric block cipher designed by Bruce Schneier.
It has a fixed data block size of 8 bytes and its keys can vary in length from 32 to 448 bits (4 to 56 bytes).
Blowfish is deemed secure and it is fast. However, its keys should be chosen to be big enough to withstand a brute force attack (e.g. at least 16 bytes).

###### Encrypted text

![]https://github.com/ekaterinatrofa/BSI/blob/main/cipher/image%20(1).png)

###### Decrypted text

![]https://github.com/ekaterinatrofa/BSI/blob/main/cipher/image.png

###### Installation:

```
pip install pycryptodome
```
###### References: 

- [https://pycryptodome.readthedocs.io/en/latest/src/cipher/blowfish.html](https://pycryptodome.readthedocs.io/en/latest/src/cipher/blowfish.html)
---

### Twofish

Twofish is a symmetric key block cipher with a block size of 128 bits (16 bytes) and key sizes up to 256 bits. 
This cipher is a Feistel Network, which is a cryptographic technique which works by splitting the data block into two equal pieces and applying encryption in multiple rounds. 
In each round, half of the text block is sent through a function, and then “XORed” with the other half of the text block.

###### Installation:

```
pip install twofish
```

###### References: 

- [https://devrescue.com/python-twofish-encryption/](https://devrescue.com/python-twofish-encryption/)

---

### RC6

RC6 (Rivest Cipher 6) is derived from RC5, and is a symmetric key block cipher. 
It was submitted to the NIST Advanced Encryption Standard (AES) competition. 
It is patented by RSA Security. 
It uses a block size of 128 bits and has keys sizes of 128, 192, and 256 bits, and then up to 2040-bits.


###### Installation:

```
pip install RC6Encryption
```


###### References: 

- [https://pypi.org/project/RC6Encryption/](https://pypi.org/project/RC6Encryption/)
- [https://asecuritysite.com/encryption/rc6](https://asecuritysite.com/encryption/rc6)

Author:

_Kateryna Trofymenko_