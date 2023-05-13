"""
    Task 4: duplicate Char 
    Context: Coding interview questions
    Category: String Manipulation
    
    Problem Statement:
    You have given a string. You need to remove all the duplicates from the string.
    The final output string should contain each character only once.
    The respective order of the characters inside the string should remain the same.
    You can only traverse the string at once.

    Input string: ababacd
    Output string: abcd
"""

int_str = 'aabbcdddda'
out_str = ""

for chr in int_str:
    if len(out_str) == 0:
        out_str += chr 
    elif chr not in out_str:
        out_str += chr

print(out_str)

"""
Output>>>

    abcd
"""