#Create a program to find the second-largest element in a list.
def getSecondLargest(arr):
    largest = 0
    secondLargest = 0
    for i in arr:
        if i > largest:
            largest, secondLargest = i, largest
    return secondLargest
    

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
            print(f'The second largest number in your list is: {getSecondLargest(arr)}')
            break



if __name__ == "__main__":
    main()