#Create a function that generates a random number between a given range.
import random

def randomGenerator(rMin,rMax):
    return random.randint(rMin, rMax)

def checkRange(start, end):
    if not start.isdigit() or not end.isdigit():
        return "These values are incorrect!"
    if int(start) > int(end):
        return "The start value cannot be greater than the end"
    return ''

def main():
    while True:
        numberRange = input("Enter the start and the end of the range separated by a space: ").strip().split()
        minVal, maxVal = numberRange
        errMsg = checkRange(minVal, maxVal) 
        if not errMsg:
            print(f'The random value is: {randomGenerator(int(minVal),int(maxVal))}.')
            break
        else:
            print(errMsg)



if __name__ == "__main__":
    main()