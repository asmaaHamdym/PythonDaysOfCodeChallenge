# Write a program to find the sum of all elements in a list


list = input('Please enter the numbers of the list separated by a space: ').strip().split()
if not list:
    print('Enter the elements')
else:
    try:
        list = [int(element) for i, element in enumerate(list)]
        print(f'The sum of all elements is {sum(list)}')
    except:
        print('The list has invalid values')

