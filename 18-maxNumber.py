# Create a program to find the largest among three numbers.

def checkArr(arr):
    if not arr:
        print('Enter the numbers')
    else:
        try:
            arr = [float(element) for element in arr]
            return arr
        except:
            print('Enter three valid values')

while True:
    arr = input('Please enter the three numbers separated by a space: ').strip().split()
    arr = checkArr(arr)
    if arr:
        print(f"The largest number in {arr} is {max(arr)}")
        break
