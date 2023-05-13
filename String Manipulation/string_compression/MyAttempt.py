"""
    Task: Compress a string
    Context: general programming question
    Category: String manipulation
    Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'.
"""

def comp_str(string):
    if string == None:
        return None
    string_li = list(string)
    counter = 0
    new_string = ""
    for i, chr in enumerate(string_li):
        if i+1 == len(string_li):
            counter += 1
            new_string += chr
            new_string += str(counter)
            break
        if string_li[i] == string_li[i + 1]:
            # print(string_li[i], " [i] == [i+1] ", string_li[i + 1])
            counter += 1
        else:
            # print(string_li[i], " [i] != [i+1] ", string_li[i + 1])
            counter += 1
            new_string += chr
            new_string += str(counter)
            counter = 0

    return new_string


string = "AAAABCCCDDDD"
print("Resulting String:", comp_str(string))

"""
Output>>>

    Resulting String: A4B1C3D4
"""