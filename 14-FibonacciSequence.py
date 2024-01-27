# Write a program to print the first n numbers of a Fibonacci sequence
def feb(n):
    if n <= 1 :
        return n
        
    return  feb(n - 1) + feb(n - 2) 

while True:
    number = input('Your number: ').strip()
    if number.isdigit() and int(number) > 0:
        number = int(number)
        break
    print("Enter a positive integer!")

febSequence = []
for i in range(number):
    febSequence.append(feb(i))
print(febSequence)