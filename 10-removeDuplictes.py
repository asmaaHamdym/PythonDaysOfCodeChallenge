# Write a program to remove duplicates from a list.
def isValidList(arr):
    if not arr:
        print('Enter the elements')
    else:
        arr = set(arr)
        return list(arr)
        




arr = input('Please enter the numbers of the list separated by a space: ').strip().split()
print(f'The list after removing duplicates: {isValidList(arr)}')
