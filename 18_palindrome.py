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