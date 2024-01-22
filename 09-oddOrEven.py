# Write a program to check if a integer is even or odd.


while True:
    number = input('Your number: ').strip()
    if number.isdigit():
        break
    print("Enter a valid integer!")

if int(number) % 2 :
    print(f'Number {number} is odd')
else:
    print(f'Number {number} is even')
   
