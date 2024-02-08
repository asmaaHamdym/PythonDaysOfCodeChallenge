#Create a program to concatenate two lists.

def main():
    # making sure the first list is not empty!
    while True:
        arr1 = input('Please enter the elements of the first list separated by a space: ').strip().split()
        if arr1:
            break
        print("That's an empty list!")

    # making sure the second list is not empty!
    while True:
            arr2 = input('Please enter the elements of the second list separated by a space: ').strip().split()
            if arr2:
                break
            print("That's an empty list!")

    print(f"The result after concatenating {arr1} and {arr2} is:\n{arr1 + arr2}")

    
if __name__ == "__main__":
    main()