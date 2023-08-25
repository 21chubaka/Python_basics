"""
Password Checking 3 times program:

Assign a password to password variable.
Prompt a user to enter their password.
Check if the user input matches the password, if so tell the user they
have successfully logged in. Else notify the user the password if wrong and
prompt the user to enter their password three times. Check if all three
inputs match the password. If so, notify user they have successfully
logged in. If not notify they have been denied access.

"""
# Password variable
password = 'PythonRocks!'

# Prompt user for password
user_input = input('Please enter your password: ')

# Checks if user input matches password
if user_input == password:
    print('You have successfully logged in.')

# Prompts user to enter correct password 3 times
else:
    # Informs user of incorrect password path
    print('You have entered an incorrect password. Please enter your password three times.')
    first_user_inpt = input('Please enter your password: ')
    sec_user_inpt = input('Please enter your password: ')
    third_user_inpt = input('Please enter your password: ')

    # Checks if three inputs match password
    if first_user_inpt == password and sec_user_inpt == password and third_user_inpt == password:
        print('You have successfully logged in.')
    else:
        # Inform user they are denied
        print('You have been denied access.')