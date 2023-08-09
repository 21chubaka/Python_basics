# Python_basics
Basic Python Skills

0_hello.py:<br>
Hello World<br>
Simple program that a variable the concatenation of "Hello, " and "world".
The program wil then print out the variable.

01_currency_exchange.py:<br>
Currency Exchange<br>
Simple program to take one currency as a float and converts it to another currency as a float
For this example will be using an amount in US Dollars to be converted into Canadian Dollars

02_length_to_area.py:<br>
Length to Area<br>
A program that takes a user's input of a length (float) and checks if the length is an acceptable length (non-negative),
then calculates and prints out:<br>
Area of a square<br>
Area of a circle (using given length as radius)<br>
Volume of a cube<br>
Volume of a sphere<br>
Volume of a cylinder (using given length as radius and side)

03_city_province.py:<br>
Province of City/Town<br>
A program that takes a user's input of a town/city from a small amount of town/cities from Ireland and
return what Province the town/city is located in if there is a match.

04_password.py:<br>
Password Checker<br>
A program that asks the user to enter a password and if it is correct that sends a succesful login message.  
If incorrect sends an incorrect message, then ask the user to input the correct password three times.  
If the user correct inputs the password it will be a succesful login, if not, access will be denied.

05_int_divis_counter.py:<br>
Integer Divisible Counter<br>
A program that sums the integers from 1-10,000, that are divisisble by 3 or 5. The program utilises a while loop.

06_int_series_range_count.py:<br>
Integer Range Counter<br>
A program that utilises a while loop to prompt the user to give a series of integers.  It checks is what range the number belongs:<br>
Number equal to 0<br>
Greater than 0 and less than or equal to 20<br>
Greater than 20 and less than or equal to 40<br>
Greater than 40 and less than or equal to 60<br>
Greater than 60 and less than or equal to 80<br>
Greater than 80 and less than or equal to 100<br>
Greater than 100<br>
The program will count the number of numbers that fall in each range.  The program is ended by the user entering a negative number.  
When ended it returns the number of numbers in each range to the user.

07_pizza_combos.py:<br>
Pizza Combinations<br>
A program for the manager (user) of a pizza company, that will tell the manager the number of combinations of pizza toppings when
given the number of toppings that day and the number of topping on the standard pizza that day.  The program will exit when complete
or if the user gives a negative number. Combinations are calculated using: n! / (k!(n - k)!)

08_vowel_counter.py:<br>
Vowel Counter<br>
A program that counts the vowels in each string the user provides.  The program exits when given an empty string.

09_fibonacci.py:<br>
Fibonacci Series<br>
A program that prompts the user to provide an integer and utilises a while loop to calculate that number of terms of the Fibonacci Series.

10_aprox_sq_root.py:<br>
Aproximate Square Root<br>
A program that prompts a user to provide a positive number and positive tolerance and uses a square root function to return the aproximate 
square root to the user.

11_recur_fact.py:<br>
Recursive Factorial<br>
Prompts the user for a positive integer and uses a recursive function to calculate the factorial of that number and return case results of the 
factorial as it works up to the user number.

--Comparing Non-Recursive and Recursive Factorial Programs--<br>
For the next two programs there will be time tracking elements in the program to compare the performances of a Non-Recursive and Recursive Factorial Program.  Results of increasing larger sized inputs recorded in text file and below.<br>

12_nonRecur_fact.py:<br>
Non-recursive Factorial<br>
A program that a positive integer is given and iteratively calculates its Factorial.  It also records the time it took to run and returns that time to the user.

13_recur_fact_time.py:<br>
Recursive Factorial Time Results<br>
A program that a positive integer is given and recursively calculates its Factorial.  It also records the time it took to run and returns that time to the user.

14_nonRecur_Recur_timeResults.txt:<br>
Recursive/Non-recursive Factorial Time Results<br>
Results of time performance between Non-Recursive and Recursive Factorial programs with increasing inputs given.<br>

--Example Results--<br>
Time Elapsed:<br>
Input 5:<br>
Recursive: 0:00:01.084537<br>
Non-Recursive: 0:00:01.458487<br>

Input 666:<br>
Recursive: 0:00:03.551164<br>
Non-Recursive: 0:00:03.149220<br>

Input 2500:<br>
Recursive: RecursionError: maximum recursion depth exceeded in comparison<br>
Non-Recursive: 0:00:03.954985<br>

15_recur_input_func.py:<br>
Recursive Function<br>
A program using a recursive function that takes a single argument as an integer greater or equal to zero and prints
out that number of terms from a function. A negative number ends the program.

16_common_divis_prog.py:<br>
Common Divisors<br>
A program that takes two positive integers from a user and returns all common divisors of the two numbers and the sum of the common divisors.

17_perfect_num.py:<br>
Perfect Numbers<br>
A program that takes a positive integer from a user and returns all the perfect numbers up to and including the number given.  A perfect number
is a positive integer that is equal to the sum of its proper factors.

18_palindrome.py:<br>
Palindrome<br>
A program that takes a string from a user and returns if it is a palindrome.  The program exits with an empty string.

19_webPage_counter.py:<br>
Web Page Bracket Counter<br>
A program that takes a web page and counts the occurrences of left angle brackets (<), right angle brackets (>), newlines, the lowercase
letter e, the string <!-- and the string --> and prints out the results to a file results.txt.  The program will check if a results file exists
and if it does it will not print out the results.  For this program the web page is set to: gaa_index_source.txt.

20_webPage_bracket_counter.py:<br>
Web Page Bracket Balance<br>
A program that takes a web page and counts the occurrences of brackets and detrimines if the brackets are balanced.  For this program the web page is set to: gaa_index_source.txt.