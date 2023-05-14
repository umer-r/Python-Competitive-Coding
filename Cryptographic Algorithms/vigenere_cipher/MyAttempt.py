"""
    Task: Vigenere cipher encryption & decryption
    Context: General InfoSec Problems
    Category: Cryptographic algorithms

    Problem statement:
    Vigenere Cipher is a method of encrypting alphabetic text. It uses a simple form of polyalphabetic substitution. 
    A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets.

    Input: (HELLOWORLD, WORLD)
    Output:
        Encrypted message:  wlvpklvbpz
        Decrypted message:  helloworld
        Encrypted message:  QFPJEFPVJT
        Decrypted message:  HELLOWORLD
"""

def vigenere_cipher(s, k):
    sli = list(s)
    kli = list(k)
    req_items = len(s)
    kli = [kli * req_items][0][:req_items]
    en_str = ""
    for pi, ki in zip(sli, kli):
        pi = ord(pi)
        ki = ord(ki)
        if 64 < pi < 91 and 64 < ki < 91:
            E = (pi - 65 + ki) % 26 + 65
        if 96 < pi < 123 and 96 < ki < 123:
            E = (pi - 97 + ki) % 26 + 97
        en_str += chr(E)
    return en_str

def decrypt_vigenere_cipher(s, k):
    sli = list(s)
    kli = list(k)
    req_items = len(s)
    kli = [kli * req_items][0][:req_items]
    en_str = ""
    for pi, ki in zip(sli, kli):
        pi = ord(pi)
        ki = ord(ki)
        if 64 < pi < 91 and 64 < ki < 91:
            E = (pi - 65 - ki) % 26 + 65
        if 96 < pi < 123 and 96 < ki < 123:
            E = (pi - 97 - ki) % 26 + 97
        en_str += chr(E)
    return en_str

string = "helloworld"
key = "world"
decipher = "wlvpklvbpz"

print("Encrypted message: ", vigenere_cipher(string, key))
print("Decrypted message: ", decrypt_vigenere_cipher(decipher, key))

string = "HELLOWORLD"
key = "WORLD"
decipher = "QFPJEFPVJT"

print("Encrypted message: ", vigenere_cipher(string, key))
print("Decrypted message: ", decrypt_vigenere_cipher(decipher, key))

"""
Output>>>

    Encrypted message:  wlvpklvbpz
    Decrypted message:  helloworld
    Encrypted message:  QFPJEFPVJT
    Decrypted message:  HELLOWORLD
"""