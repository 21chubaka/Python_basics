'''
Recursive Function program:
Define a function:
    n == 0: 13
    n == 1: 8
    n < 0: exit
    else: f(n - 2) + 13 * f(n - 1)

Inform user of program rules
Intialize user_input variable
While user_input is greater or equal to 1:
    Return function result
    Prompt user for number
Else, end program
'''
# Import sys
import sys

def funcRec(num):
    ''' Function from P15P3 requirements 
    num == 0: 13
    num == 1: 8
    n < 0: exit
    else: f(num - 2) + 13 * f(num - 1)'''
    if num == 0:
        return 13
    elif num == 1:
        return 8
    elif num < 0:
        print('Goodbye!')
        sys.exit()
    else:
        return (funcRec(num - 2) + 13 * funcRec(num - 1))

# Inform user of rules of the program
print('I will keep asking for a positive integer number and run it through a function.')
print('The program will end if a negative number is entered.')

# Intialize user input variable as zero to start
user_input = 0

# Loop to check that user input is non-negative
while user_input >= 0:
    # Prompt user for an input
    user_input = int(input('Please provide a positive integer number: '))
    # Return result to user after passing user input into funcRec func
    print('Function result: ', funcRec(user_input))
else:
    # Else, end program
    print('Goodbye!')