# Write a function to calculate the factorial of a number.

def fact(n):
    if n <= 1 :
        return 1
    else:
        return n * fact(n-1)
    
while True:
    number = input('Your number: ').strip()
    try:
        number = int(number)
        break
    except :
        print("Enter a valid integer!")

print(F"Factorial of {number} is {fact(number)}")
