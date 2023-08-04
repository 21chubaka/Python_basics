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