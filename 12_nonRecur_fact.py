'''
Non-Recursive Factorial Time Track program:
Import time tracking libs
Intialize user_input variable and set it to zero.
Intialize a total variable and set it to one.
Inform the user of the rules of the program.
While user_input is greater or equal to zero:
    Prompt the user to enter a positive integer
    For i in the range of one to user_input + 1
        Update total to total * i
    Return the factorial to the user
    Reset total to one
Else, inform the user it is a negative number
'''
from timeit import default_timer as timer
from datetime import timedelta

start = timer()

user_input = 0
total = 1

print('I will keep asking for positive interger numbers and telling you the Factorial of your number.')
print('A negative number will end the program.')

user_input = int(input('Please enter a positive number: '))
for i in range(1, user_input + 1):
    total = total * i
print('The Factorial of', user_input, 'is', total)
total = 1

end = timer()
print(timedelta(seconds=end-start))