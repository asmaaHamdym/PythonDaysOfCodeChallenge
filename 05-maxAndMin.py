#Write a program to find the maximum and minimum values in a list.

def fixInput(arr):
    if not arr:
        print("Can't work with an empty list")
    else:
        try:
            arr = [float(element) for element in arr]
            return arr
        except:
            print('The list is not properly formatted')

while True:
    list = input('Please enter the numbers of the list separated by a space: ').strip().split()
    arr = fixInput(list)
    if arr:
        break

print(f'The input arr is {arr} \nThe maximum value is {max(arr)} \nThe minimum value is {min(arr)}')