'''
Backet Balance program:
 Write a program that reads a file and checks that brackets (ie ( and ), < and >, { and }
and [ and ]) are balanced, ie there should never be a situation where there are more right
brackets of a particular type than there are corresponding left brackets and the total number
of right brackets should equal the number of left brackets (You do not need to consider the
interleaving of different bracket types). Your program should return the total number of each
bracket and a message indicating whether or not the file has balanced brackets.

Import os
Check if the file does not exist
    If so, inform the user
Else
    Read the file into a string variable
    Set up counter variables
    Set up total counter variables
    Check if each of the barackets are balanced
        If so, print results and inform which brackets are and are not balanced
        Inform user if the total brackets page is balanced or not
'''
# Import lib
import os

# Check for file and read in
filename = 'gaa_index_source.txt'
if not os.path.isfile(filename):
    # File does not exist error
    print('File' + filename + 'does not exist.')
else:
    # Else, open and read file
    fh1 = open('gaa_index_source.txt', 'r')
    data = fh1.read()

    # Close file
    fh1.close()
    #print(data)

    # Counter variables
    l_brack = data.count('<')
    r_brack = data.count('>')

    l_para = data.count('(')
    r_para = data.count(')')

    l_sq_brack = data.count('[')
    r_sq_brack = data.count(']')

    l_sq = data.count('{')
    r_sq = data.count('}')

    total_left = l_brack + l_para + l_sq_brack + l_sq
    total_right = r_brack + r_para + r_sq_brack + r_sq

# Return counts & if they are balanced
# Brackets:
print('# of <: ', l_brack)
print('# of <: ', r_brack)
# Check if left and right brackets are balanced
if l_brack == r_brack:
    # If so, return balanced
    print('< & > are Balanced')
else:
    # Else, not balanced
    print('< & > are NOT Balanced')

# Parentheses:
print('# of (): ', l_para)
print('# of ): ', r_para)
# Check if left and right parentheses are balanced
if l_para == r_para:
    # If so, return balanced
    print('( & ) are Balanced')
else:
    # Else, not balanced
    print('( & ) are NOT Balanced')

# Square Brackets:
print('# of [: ', l_sq_brack)
print('# of ]: ', r_sq_brack)
# Check if left and right sq brackets are balanced
if l_sq_brack == r_sq_brack:
    # If so, return balanced
    print('[ & ] are Balanced')
else:
    # Else, not balanced
    print('[ & ] are NOT Balanced')

# Curly Brackets:
print('# of {: ', l_sq)
print('# of }: ', r_sq)
# Check if left and right curly brackets are balanced
if l_sq == r_sq:
    # If so, return balanced
    print('{ & } are Balanced')
else:
    # Else, not balanced
    print('{ & } are NOT Balanced')

if total_left == total_right:
    print('Page Brackets are Balanced.')
else:
    print('Page Brackets are NOT Balanced')