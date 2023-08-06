'''
Palindrome Function program:
From Lecture 17 Slides 19 & 20 with update from Ques P17P5
Define a function that removes non-letters & turns a string to all lowercase
Define a function to tell if a string is a Palindrome
    Returns True if s is a palindrome;
    Returns False otherwise.
    Recursive func
    Has print statements to trace its operation
Prompts a user for a string
While string is not empty, runs string into both functions
If empty, program ends
'''

def toChars(s):
    ''' Converts a string to lowercase & removes non-letters

    Assumes s is a str
    Converts uppercase letters to lowercase & removes non-letters '''
    s = s.lower()
    letterstring = ''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            letterstring += c
    return letterstring

def isPal(s):
    ''' Checks whether the string s is a palindrome

    Assumes that s is a str with only lowercase letters & no non-letters.
    Returns True if s is a palindrome;
    Returns False otherwise.
    Recursive func
    Has print statements to trace its operation '''
    print('isPal func called with argument', s)
    if len(s) <= 1:
        print('About to return True from isPal from the base case')
        return True
    else:
        result = s[0] == s[-1] and isPal(s[1:-1])
        print('About to return result', result, 'from isPal with argument', s)
        return result

# Prompt the user for a string & inform that an empty string will eit program
str = input('Enter a string (empty string to exit): ')

# Loop to continue accepting string inputs, unless empty: then exit
while str != '':
    if isPal(toChars(str)):
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')

    str = input('Enter a string (empty string to exit): ')

print('Finished!')