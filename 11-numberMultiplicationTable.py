# Write a program to print the multiplication table of a given number.


# from curses.ascii import isdigit


while True:
    number = input('Your number: ').strip()
    if number.isdigit():
        break
    print("Enter a valid integer!")

for digit in range(1, int(number) + 1):
    print(f'{digit} x {number} = {int(number) * digit}')