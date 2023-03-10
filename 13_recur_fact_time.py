'''
Recursive Factorial Time Track program:
Import time tracking libs
Start timer
Define a function that recursively calculates the factorial of an argument.
    Check if argument is equal to zero or one, if so
        set result variable to one
        print argument and result
    Else, set result to factorial equation
        print argument and result
Inform the user of the rules of the program.
Intialize user_input variable and set it to zero.
Intialize a total variable and set it to one.
While user_input is greater or equal to zero:
    Prompt the user to enter a positive integer
    For i in the range of one to user_input + 1
        Update total to total * i
    Return the factorial to the user
    Reset total to one
Else, inform the user it is a negative number
End timer
Return time to user
'''
from timeit import default_timer as timer
from datetime import timedelta

start = timer()



def factorial(num):
    ''' Function that return the Factorial of its argument '''
    if num == 0 or num == 1:
        result = 1
        #print('Base case - num:', num, 'result:', result)
    else:
        result = num * factorial(num - 1)
        #print('num:', num, 'result:', result)

    return result

print('Provide a positive integer and I will tell you its factorial.')
user_input = int(input('Provide a positive integer: '))

if user_input >= 0:
    print('The factorial of', user_input, 'is', factorial(user_input))
else:
    print('Number must be a positive integer. Please try again.')

end = timer()
print(timedelta(seconds=end-start))