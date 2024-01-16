# Write a program to check if a number is positive, negative, or zero

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

number = (input('Enter the number: ').strip())
while not is_float(number):
    number = input('Enter the number: ').strip()
if float(number) > 0 :
    print(f'Number {number} is positive')
elif float(number) < 0:
    print(f'Number {number} is negative')
else:
    print("That's a Zero!")



