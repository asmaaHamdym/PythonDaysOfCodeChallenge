import math

def calculateCircleArea(r):
    return math.pi * (r**2)

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
while True:
    radius = input('Please Enter the radius of your circle? ').strip()
    
    if is_float(radius):
        break
    print("Enter a valid value!")

area=  round(calculateCircleArea(float(radius)) , 2)
print(f'The area of a circle with radius of {radius}  is {area}')
