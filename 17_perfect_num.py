'''
Perfect Numbers Function program:
Write a program that prompts the user for a positive integer and finds all the perfect numbers up to
and including that number

Define a function that finds all perfect numbers up to & including
an arguent:
    For i in range one to an argument plus one
        Intialize a total variable and set it to zero
        For j in range one to i
            Check if i is divisble by j:
                If so, increment total by j
        Check if i equals total then return i
Inform the user of the rules of the program
Prompt the user for the positive integer
Check if user input is less than or equal to zero:
    if so, inform the user
Else, run the user input into the Perfect Num function
'''

def findPerfectNums(num):
    ''' Finds the perfect numbers up to and including the argument

    Assumes that num is a positive integer
    Returns any perfect numbers '''
    for i in range(1, num + 1):
        total = 0
        for j in range(1, i):
            if i % j == 0:
                total += j
        if i == total:
            print(i, 'is a perfect number.')

# Inform the user of the program rules and prompt for a postive integer
print('I will ask for a positive integer, and tell you all of the perfect numbers up to and including yor number.')
user_input = int(input('Please provide a positive integer: '))

# Check if user gave a positive integer and numeric
if user_input <= 0 and user_input.isnumeric():
    # Error message
    print('Number must be greater than zero.')
else:
    # Use input and findPerfectNums to return perfect numbers to user
    print(findPerfectNums(user_input))