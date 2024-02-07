#Create a program to remove a specific element from a set.
def removeElement(elementsSet, element):
    if element in elementsSet:
        elementsSet.remove(element)
    else:
        print("This element does not exist!")





def main():
        
    while True:
        arr = input('Please enter the elements of the set separated by a space: ').strip().split()
        if arr:
            elementsSet = set(arr)
            break
        print("This is an empty set!")  
       
    while True:
        element = input('Enter the element to remove: ').strip()
        if element:
            removeElement(elementsSet, element)
            print(f"{element} has been removed from your set\nThe set after removing: {elementsSet}")
            break
        print("This can't be empty!")




if __name__ == "__main__":
    main()