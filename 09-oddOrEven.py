# Write a program to check if a integer is even or odd.

def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


while True:
    number = input('Your number: ').strip()
    if is_int(number):
        break
    print("Enter a valid integer!")

if int(number) % 2 :
    print(f'Number {number} is odd')
else:
    print(f'Number {number} is even')
   
