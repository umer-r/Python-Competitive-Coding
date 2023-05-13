"""
    Task: Ceaser cipher
    Context: InfoSec Questions
    Category: Cryptographic algorithms
    Problem statement:

    Julius Caesar protected his confidential information by encrypting it using a cipher.
    Caesar's cipher shifts each letter by a number of letters. If the shift takes you
    past the end of the alphabet, just rotate back to the front of the alphabet.
    In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
    
    Original alphabet:      abcdefghijklmnopqrstuvwxyz
    Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
"""
def caesar_cipher(s, k):
    shifted_chars = {}
    for i in range(26):
        upper_case_letter = chr( 65 + i )
        shifting_ucl = chr(( i + k ) % 26 + 65)
        lower_case_letter = chr( 97 + i)
        shifting_lcl = chr(( i + k ) % 26 + 97)

        shifted_chars[upper_case_letter] = shifting_ucl
        shifted_chars[lower_case_letter] = shifting_lcl

    encrypted_str = ""
    for char in s:
        if char in shifted_chars:
            encrypted_str += shifted_chars[char]
        else:
            encrypted_str += char
    return encrypted_str

s = "abcdefghijklmnopqrstuvwxyz"
k = 3

print(caesar_cipher(s, k))

"""
Output>>>

    defghijklmnopqrstuvwxyzabc
"""