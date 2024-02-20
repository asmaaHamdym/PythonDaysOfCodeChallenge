#Create a function that finds the second smallest element in a list.
def getSecondSmallest(arr):
    smallest = float('inf')
    secondSmallest = float('inf')
    
    for i in arr:
        if i < smallest:
            smallest, secondSmallest = i, smallest
        elif i < secondSmallest:
            secondSmallest = i
    return secondSmallest
    

def checkArr(arr):
    if not arr :
        return "That's an empty list!"
    
    try:
        for i in range(len(arr)):
            arr[i] = float(arr[i])
    except ValueError:
        return "The list contains non numeric values"

    return ""

def main():
        
    while True:
        arr = input('Please enter the elements of the list separated by a space: ').strip().split()
        errorMsg = checkArr(arr)
        if errorMsg:
            print(errorMsg)  
        else:  
            print(f'The second smallest number in your list is: {getSecondSmallest(arr)}')
            break



if __name__ == "__main__":
    main()