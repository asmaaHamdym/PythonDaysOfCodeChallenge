#Create a program that removes the nth element from a list.
def main():
   
    while True:
        arr = input('Please enter the elements of the list separated by a space: ').strip().split()
        if arr:
            break
        print("That's an empty list!") 

    index = int(input("Please enter the number of element you want to remove: "))
    removedElement = arr[index -1]
    if index <= len(arr):
        arr.remove(arr[index -1])
        print(f"The result after removing '{removedElement}' is:   {arr}")
    else:
        print("This number is out of range!")
    
if __name__ == "__main__":
    main()