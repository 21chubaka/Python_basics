'''
Number Range Counter program:
Intialize user_input variable and series of number range count variables; all set to zero.
Inform user of rules of program.
While user_input is greater or equal to zero.
    Prompt user to enter number.
    Check if the user_input is negative, if so print out break out of while and print the analysis.
    Set up series of if checks for the number ranges. If number is in range increment that range counter by one.
        and inform user if it is in that range.
End while ends or breaks, print analysis statements
'''

user_input = 0
zero_count = 0
zero_20 = 0
count_40 = 0
count_60 = 0
count_80 = 0
count_100 = 0
over_100 = 0

print('I will keep asking you for an integer number.  And tell you what range the number falls in.')
print('If you enter a negative number the program will end.')
while user_input >= 0:
    user_input = int(input('Please enter a number: '))
    if user_input < 0:
        break
    if user_input == 0:
        zero_count += 1
        print(user_input, 'is zero.')
    if user_input > 0 and user_input <= 20:
        zero_20 += 1
        print(user_input, 'is greater than 0 and less than or equal to 20.')
    if user_input > 20 and user_input <= 40:
        count_40 += 1
        print(user_input, 'is greater than 20 and less than or equal to 40.')
    if user_input > 40 and user_input <= 60:
        count_60 += 1
        print(user_input, 'is greater than 40 and less than or equal to 60.')
    if user_input > 60 and user_input <= 80:
        count_80 += 1
        print(user_input, 'is greater than 60 and less than or equal to 80.')
    if user_input > 80 and user_input <= 100:
        count_100 += 1
        print(user_input, 'is greater than 80 and less than or equal to 100.')
    if user_input > 100:
        over_100 += 1
        print(user_input, 'is greater than 100.')

print('Analysis:')
print('Count of numbers equal to zero: ', zero_count)
print('Count of numbers 0 < X <= 20: ', zero_20)
print('Count of numbers 20 < X <= 40: ', count_40)
print('Count of numbers 40 < X <= 60: ', count_60)
print('Count of numbers 60 < X <= 80: ', count_80)
print('Count of numbers 80 < X <= 100: ', count_100)
print('Count of numbers 100 < X: ', over_100)