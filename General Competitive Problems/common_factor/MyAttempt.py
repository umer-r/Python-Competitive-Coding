"""
    Task: Find Common factors
    Context: HackerEarth contest
    Category: General competitive problems

    Problem Statement: Little Robert likes mathematics. Today his teacher has given him two 
    integers and asked him to find out how many integers can divide both the numbers. 
    Would you like to help him in completing his school assignment?
    Both the input value should be in a range of 1 to 10^12.

    Input: 10 15
    Output: 2
"""
a = int(input("input integer a: "))
b = int(input("input integer b: "))

def input_inrange(x, y):
    if 1 <= x <= 10**12 and 1 <= y <= 10**12:
        return True
    else:
        return False

if input_inrange:
    set_a = set()
    set_b = set()

    for i in range(1, a+1):
        divident = a % i
        if divident == 0:
            set_a.add(i)

    for j in range(1, b+1):
        divident = b % j
        if divident == 0:
            set_b.add(j)


print("Factors of integer a: ", set_a)
print("Factors of integer b: ", set_b)
print("Common Factors: ", len(set_a.intersection(set_b)))

"""
Output>>>

    input integer a: 10
    input integer b: 15
    Factors of integer a:  {1, 2, 10, 5}
    Factors of integer b:  {1, 3, 5, 15}
    Common Factors:  2
"""