# Write a program to print the multiplication table of a given number.


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

for digit in range(1, int(number) + 1):
    print(f'{digit} x {number} = {int(number) * digit}')