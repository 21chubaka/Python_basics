"""
Vowel Counter:
Infrom user of the rules of the program
Prompt the user for a string
Update user input string to lowercase
Intialise vowel counter variables
Check if the user's input is not empty:
    for loop to iterate through user input:
        Check if the current letter is a vowel:
            Increment correct vowel counter variable
    Return counts of vowels to the user
Else:
    Exit program
"""
# Inform the user of the program rules
print('Provide a string and I will tell you how many vowels there is.')
print('Enter an empty string to exit the program.')

# Prompt the user for a string
user_input = input('Please enter a string: ')

# Convert the user's input to lowercase
low_user_input = user_input.lower()

# Intialize vowel counter variables
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

# Check that the users' input is not blank
if user_input != "":
    # Loop through the letters
    for letter in low_user_input:
        # Check if the vowel is present and increment the appropiate counter variable
        if letter == 'a':
            count_a += 1
        if letter == 'e':
            count_e += 1
        if letter == 'i':
            count_i += 1
        if letter == 'o':
            count_o += 1
        if letter == 'u':
            count_u += 1

    # Return the counts to the user
    print('Number of a\'s: ', count_a)
    print('Number of e\'s: ', count_e)
    print('Number of i\'s: ', count_i)
    print('Number of o\'s: ', count_o)
    print('Number of u\'s: ', count_u)
else:
    # Inform the user of empty string
    print('Empty string. Goodbye.')