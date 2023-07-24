'''
Sum of 1-10000; divisble by 3 or 5 program:

Create a counter variable and set it to 10000. Create a total variable
and set it to 0. Create a while loop that continues until it is zero.
Inside the while loop check if the counter is divisble by 3 or 5. If so,
increment the total variable by counter then decrement counter by one. If not,
just decrement the counter by one. Outside the while loop print the sum of the
integers divisble by 3 or 5 in the range of 1-10000 using the total variable.
'''

counter = 10000
total = 0

# While loop until counter is not 0
while counter != 0:
    # Checks if current integer if divisible by 3 or 5
    if counter % 3 == 0 or counter % 5 == 0:
        total += counter
        counter -= 1
    else:
        counter -= 1

print('The sum of integers divisble by 3 or 5 in the range of 1-10,000:', total)