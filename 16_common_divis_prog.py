'''
Common Divisors Function program:
Implement the program to calculate common divisors from Lecture 16. You may use the solution on
Pages 14–17 of the slides in your solution

From Lecture 16 slides pages 16 & 17
Define a function that takes two arguments
    Runs through the range of one to the min of the two arguments:
        If both are divisible by i add to a divisors tuple
        Return divisors
Prompt user for two ints
Check if two user numbers are less than or equal to zero
    If so, inform user number should be greater than zero
Else, runs numbers into divisor function and print results
'''

def findDivisors(num1, num2):
    ''' Finds the common divisors of num1 & num2

    Assumes that num1 & num2 are positive integers
    Returns a tuple containing the common divisors of num1 & num2 '''
    divisors = ()
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            divisors += (i,)

    return divisors

# Prompt the user for two positive integers
number1 = int(input('Enter a positive integer: '))
number2 = int(input('Enter another positive integer: '))

if number1 <= 0 or number2 <= 0:
    print('Numbers should be > 0.')
else:
    divisors = findDivisors(number1, number2)
    print('The common divisors of', number1, 'and', number2, 'are:', divisors)

    total = 0
    for d in divisors:
        total += d
    print('Sum of the common divisors are:', total)

print('Finished')