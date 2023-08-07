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