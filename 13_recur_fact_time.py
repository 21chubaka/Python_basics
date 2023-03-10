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