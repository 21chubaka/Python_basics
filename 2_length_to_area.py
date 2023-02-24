"""
A program that takes a user's input of a length (float) and calculates and prints out:
Area of a square
Area of a circle (using given length as radius)
Volume of a cube
Volume of a sphere
Volume of a cylinder (using given length as radius and side)
"""

import math

user_length = float(input('Enter a Length: '))

radius = user_length / 2.0

height = user_length

area_sq = user_length ** 2.0

vol_cube = user_length ** 3.0

area_cir = math.pi * (radius ** 2.0)

vol_sphere = (4.0 / 3.0) * math.pi * (radius ** 3.0)

vol_cylin = math.pi * (radius ** 2) * height

print('Length provided: ', user_length)
print('------------------------------')
print('Area of a Square: ', round(area_sq, 2))
print('Area of a Circle: ', round(area_cir, 2))
print('Volume of a Cube: ', vol_cube)
print('Volume of a Sphere: ', vol_sphere)
print('Volume of a Cylinder: ', vol_cylin)