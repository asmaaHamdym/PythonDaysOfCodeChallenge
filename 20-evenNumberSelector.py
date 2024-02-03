#Write a function that takes a list of numbers and returns a new list containing only the even numbers.

def evenNumberSelector(arr):
    evenNumbersArr = []
    for element in arr :
        if (element % 2) == 0:
             evenNumbersArr.append(element)
    return evenNumbersArr

def checkArr(arr):
    if not arr :
        return "That's an empty list!"
    for i in range(len(arr)):
        if not arr[i].isdigit():
            return "The list contains non numeric values"
        else:
            arr[i] = int(arr[i])

    return ""

    
while True:
    arr = input('Please enter the elements of the list separated by a space: ').strip().split()
    errorMsg = checkArr(arr)
    if errorMsg:
        print(errorMsg)  
    else:  
        print(f'The even numbers in your list are: {evenNumberSelector(arr)}')
        break