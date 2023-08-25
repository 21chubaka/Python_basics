"""
A program that takes a user's input of a length (float) and calculates and prints out:
Area of a square
Area of a circle (using given length as radius)
Volume of a cube
Volume of a sphere
Volume of a cylinder (using given length as radius and side)
"""
# Import math lib
import math

# Prompt user for length as a float and assign it to length variable
user_length = float(input('Enter a Length as a non-negative number: '))

# Various calculations and variables
radius = user_length / 2.0
height = user_length
area_sq = user_length ** 2.0
vol_cube = user_length ** 3.0
area_cir = math.pi * (radius ** 2.0)
vol_sphere = (4.0 / 3.0) * math.pi * (radius ** 3.0)
vol_cylin = math.pi * (radius ** 2) * height

# Check if the user's length is greater or equal to zero
if user_length >= 0:
    # If so, return the calculations to the user
    print('Length provided: ', user_length)
    print('------------------------------')
    print('Area of a Square: ', str(round(area_sq, 2)))
    print('Area of a Circle: ', str(round(area_cir, 2)))
    print('Volume of a Cube: ', str(round(vol_cube, 2)))
    print('Volume of a Sphere: ', str(round(vol_sphere, 2)))
    print('Volume of a Cylinder: ', str(round(vol_cylin, 2)))
else:
    # Inform the user of error
    print('The Length you provide must be a non-negative number. Please try again.')