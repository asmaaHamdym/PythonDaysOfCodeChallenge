# Write a program to shuffle the elements of a list randomly.
import random

def shuffleList(arr):

    for i in range(len(arr)):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

while True:
    arr = input('Please enter the elements of the arr separated by a space: ').strip().split()
    if arr:
        print(shuffleList(arr))
        break
    print("That's an empty list!")