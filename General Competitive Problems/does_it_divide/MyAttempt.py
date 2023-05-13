"""
    Task: check if product of permutation is divisible by the sum of permutation.
    Context: HackerEarth contest
    Category: GCP
    Problem Statement: Consider a permutation of numbers from 1 to N written on a paper. 
    Let’s denote the product of its element as ‘prod’ and the sum of its elements as ‘sum’. 
    Given a positive integer N, your task is to determine whether ‘prod’ is divisible by ‘sum’ or not.
    
    Input:
            2 
            2 
            3
    Output:
            YEAH
            NAH
"""
TEST_SIZE = int(input('Enter test size: ')) 
arr = []
for i in range(TEST_SIZE):
    arr.append(int(input('Enter an integer: ')))

for n in arr:
    if 1 <= n <= 10**9:
        # sum = N*(N+1)//2
        sum = 0
        prod = 1
        for i in range(1, n+1):
            prod *= i
            sum += i
        #print("Product of ",n, " = ", prod, "\nSum of ", i, " = " ,sum)
        if (prod % sum == 0):
            print('YEAH')
        else:
            print('NAH')

"""
Output>>>

    Enter test size: 2
    Enter an integer: 3
    Enter an integer: 6
    YEAH
    NAH
"""