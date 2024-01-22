# Write a program to find the sum of all elements in a arr
def arrSum(arr):
    if not arr:
        print('Enter the elements')
    else:
        try:
            arr = [float(element) for element in arr]
            print(f'The sum of all elements is {sum(arr)}')
        except:
            print('The arr has invalid values')


arr = input('Please enter the numbers of the arr separated by a space: ').strip().split()
arrSum(arr)
