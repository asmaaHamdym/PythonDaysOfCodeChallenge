import math

def calculateCircleArea(r):
    return math.pi * (r**2)


radius = float(input('Please Enter the radius of your circle? '))
area =  round(calculateCircleArea(radius) , 2)
print(f'The area of a circle with radius of {radius}  is {area}')
