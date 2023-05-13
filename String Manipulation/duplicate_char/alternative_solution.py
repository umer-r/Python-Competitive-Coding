msg = " ababacd"
li = [0] * 26
print(f"Origional string: {msg}")
out= ""
for ch in msg:
    ind = ord(ch) - ord('a')
    if li[ind] == 0:
        out=out+ch
        li[ind] = 1

print(f"Unique characters in string: {out}") 