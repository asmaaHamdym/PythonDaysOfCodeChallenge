#Create a program that sorts a list of strings alphabetically.

def main():
        
    while True:
        arr = input('Please enter the elements of the list separated by a space: ').strip().split()
        if not arr :
            return "That's an empty list!"
        else:  
            print(f'The result after sorting all values alphabetically: {sorted(arr,key=str.lower)}')
            break



if __name__ == "__main__":
    main()