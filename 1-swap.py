def swap(val1, val2):
    print(f'Before swapping: {val1} {val2}')
    val1, val2 = val2, val1
    print(f'After swapping: {val1} {val2}')

var1 = input('Enter the first value: ')
var2 = input('Enter the second value: ')

swap(var1,var2)
