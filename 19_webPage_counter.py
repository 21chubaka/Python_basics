'''
Web Page Specific Char Counter program:
Uses gaa_index_source.txt
Write a program that takes a page (eg the source of a Web page that you have saved), counts
the occurrences of left angle brackets (<), right angle brackets (>), newlines, the lowercase
letter e, the string <!-- and the string --> and prints out the results to a file results.txt.
Your program should make appropriate checks regarding the existence of the input and output
files

Import os
Check if the file does not exist
    If so, inform the user
Else
    Read the file into a string variable
    Set up counter variables
    Check if the results file does not exist
        If not, create a results file and write the results to it
    Else, inform user results file already exists
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
    newline = data.count('\\n')
    e = data.count('e')
    s_comment = data.count('<!--')
    e_comment = data.count('-->')

    if not os.path.isfile('results.txt'):
        fhand = open('results.txt', 'w')

        fhand.write("Num of 'e': " + str(e) + '\n')
        fhand.write("Num of '\\n': " + str(newline) + '\n')
        fhand.write("Num of '<': " + str(l_brack) + '\n')
        fhand.write("Num of '>': " + str(r_brack) + '\n')
        fhand.write("Num of '<!--': " + str(s_comment) + '\n')
        fhand.write("Num of '-->': " + str(e_comment) + '\n')

        fhand.close()
        print('Results of program have been printed out to the file results.txt')
    else:
        print('The results file already exists.')