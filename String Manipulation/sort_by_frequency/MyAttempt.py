"""
    Task: Sort by frequency
    Context: general coding interview
    Category: String manipulation
    Problem statement:
    The characters in the string should be sorted based on the following conditions.
    1 - Sort the characters in the string by their frequency of occurrences 
        (the number of times characters have occurred in the string).
    2 - If the two different characters have the same frequency, these 
        letters should be sorted based on their alphabetical order.
"""

def sort_by_freq(msg):
    char_freq = {}
    for c in msg:
        if c in char_freq:
            char_freq[c] += 1
        else:
            char_freq[c] = 1
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1])
    return ''.join([char * freq for char, freq in sorted_chars])

out = sort_by_freq("aabbccdddddeeeee")
print(f"String sorted by char frequency: {out}")


"""
Output>>>

    String sorted by char frequency: aabbccdddddeeeee
"""