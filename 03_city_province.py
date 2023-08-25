"""
A program that takes a user's input of a town/city from a small amount of town/cities from Ireland and
return what Province the town/city is located in if there is a match.
"""
# Prompt user for a Town/City input
user_input = input('Enter a Town or City(string): ')

# Convert user input to lowercase
user_input_low = user_input.lower()

# Check if user's input matches and of our towns/cities
if user_input_low == 'dublin':
    print('You entered', user_input, '.', user_input, 'is in Leinster.')
elif user_input_low == 'belfast':
    print('You entered', user_input, '.', user_input, 'is in Ulster.')
elif user_input_low == 'cork':
    print('You entered', user_input, '.', user_input, 'is in Munster.')
elif user_input_low == 'limerick':
    print('You entered', user_input, '.', user_input, 'is in Munster.')
elif user_input_low == 'derry':
    print('You entered', user_input, '.', user_input, 'is in Munster.')
elif user_input_low == 'galway':
    print('You entered', user_input, '.', user_input, 'is in Connacht.')
elif user_input_low == 'lisburn':
    print('You entered', user_input, '.', user_input, 'is in Ulster.')
elif user_input_low == 'kilkenny':
    print('You entered', user_input, '.', user_input, 'is in Leinster.')
elif user_input_low == 'waterford':
    print('You entered', user_input, '.', user_input, 'is in Munster.')
elif user_input_low == 'sligo':
    print('You entered', user_input, '.', user_input, 'is in Connacht.')
else:
    print('Sorry, I didn\'t recognize that name.')