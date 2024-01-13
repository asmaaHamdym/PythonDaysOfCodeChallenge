# Write a function to count the number of vowels in a given string

vowels = set(['a', 'e', 'o', 'i', 'u'])

def noOfVowels(word):
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    
    return count

newWord = input('Enter the word: ')
print(f'Number of vowels in {newWord} is {noOfVowels(newWord)}.')