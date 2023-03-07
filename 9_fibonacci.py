'''
Fibonacci Series program:
Prompt user to provide a positive integer
Intialize three variables (0, 1, 2)
Check if user_input is less than or equal to zero:
    If so, Inform user to enter pos integer
Else, if user_input equals one:
    Return a
    Else, print a & b
    While count is less than user_input:
        Update c to a + b
        Return c
        Update a to b
        Update b to c
        Increment count by one
'''
user_input = int(input('Please enter a positive integer: '))

a = 0
b = 1
count = 2

if user_input <= 0:
    print("Enter a positive integer. Please try again.")
else:
    if user_input == 1:
        print(a)
    else:
        print(a)
        print(b)
        while count < user_input:
            c = a + b
            print(c)
            a = b
            b = c
            count += 1