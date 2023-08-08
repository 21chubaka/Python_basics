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

import os

filename = 'gaa_index_source.txt'
if not os.path.isfile(filename):
    print('File' + filename + 'does not exist.')
else:
    fh1 = open('gaa_index_source.txt', 'r')
    data = fh1.read()

    fh1.close()
    #print(data)
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