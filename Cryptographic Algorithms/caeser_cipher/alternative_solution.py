def caesar_cipher(s, k):
    result = ""
    for char in s:
        n = ord(char)
        if 64 < n < 91:
            n = ((n - 65 + k) % 26) + 65
        if 96 < n < 123:
            n = ((n - 97 + k) % 26) + 97
        result = result + chr(n)
    return result

s = "ABC"
k = 3
print(caesar_cipher(s, k))