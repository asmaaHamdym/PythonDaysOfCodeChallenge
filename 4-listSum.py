# Write a program to find the sum of all elements in a list
def listSum(arr):
    if not arr:
        print('Enter the elements')
    else:
        try:
            arr = [float(element) for element in arr]
            print(f'The sum of all elements is {sum(arr)}')
        except:
            print('The list has invalid values')


list = input('Please enter the numbers of the list separated by a space: ').strip().split()
listSum(list)
