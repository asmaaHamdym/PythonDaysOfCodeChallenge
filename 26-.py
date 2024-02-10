#Create a program that uses a lambda function to square each element of a list.
def checkArr(arr):
    if not arr :
        return "That's an empty list!"
    
    try:
        for i in range(len(arr)):
            arr[i] = int(arr[i])
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
            print(f'The result after squaring all values in your list: {list(map(lambda x: x*x, arr))}')
            break



if __name__ == "__main__":
    main()