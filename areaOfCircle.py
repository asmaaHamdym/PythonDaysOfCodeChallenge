import math

def calculateCircleArea(r):
    return math.pi * (r**2)


radius = int(input('Please Enter the radius of your circle? '))
area =  calculateCircleArea(radius)
print(f'The area of a circle with radius of {radius}  is {area}')