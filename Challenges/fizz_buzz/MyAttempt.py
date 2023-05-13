"""
    Task: Fizz Buzz Challenge
    Context: General Competitive Problems
    Category: Challenges

    Problem Statement: Produce replacements for multiples of certain numbers.

    if given number is multiple of 3 then result Fizz
    if given number is multiple of 5 then result Buzz
    if given number is multiple of 3 and 3 then result FizzBuzz
"""

def FizzBuzz(number) -> list:
    result = []
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(i)
    return result

if __name__ == '__main__':
    print(FizzBuzz(15))

"""
Output>>>

    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
"""