'''
Recursive Factorial program:
Define a function that runs the factorial of an argument.
    Check is argument is equal to zero or one, if so
        set result variable to one
        print argument and result
    Else, set result to factorial equation
        print argument and result
Inform user of rules of program
Prompt user for positive integer
Check is user input is greater or equal to zero, if so:
    Run function and print result
Else, inform user number needs to be positive
'''
def factorial(num):
    ''' Function that return the Factorial of its argument '''
    if num == 0 or num == 1:
        result = 1
        print('Base case - num:', num, 'result:', result)
    else:
        result = num * factorial(num - 1)
        print('num:', num, 'result:', result)

    return result

print('Provide a positive integer and I will tell you its factorial.')
user_input = int(input('Provide a positive integer: '))

if user_input >= 0:
    print('The factorial of', user_input, 'is', factorial(user_input))
else:
    print('Number must be a positive integer. Please try again.')