'''
Approximate Square Root program:
Define a function that takes two arguments: number & tolerance
    Inside function for i in range zero to number plus one
        Check if i**2 is inside the tolerance range
            If so, return the aprox square
            Exit program
Inform user of rules of program
Ask user for number and tolerance
Check if number and tolerance is greater than or equal to zero:
    If so, run function
    Else, inform user number & tolerance needs to be positive
'''
import sys

def squareRoot(num, tol):
    for i in range(0, int(num) + 1):
        if (i ** 2 >= (num - tol)) and (i ** 2 <= (num + tol)):
            print('The number', i, 'is the approximate square.')
            sys.exit()

print('I will ask for a positive number and positive tolerance number and return an approximation square root.')
num = float(input('Please provide a positvie number: '))
tol= float(input('Please provide a positvie tolerance number: '))

if num >= 0 and tol >= 0:
    squareRoot(num, tol)
else:
    print('Number and Tolerance must be a positive number. Please try again.')