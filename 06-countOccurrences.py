# Write a program to count the occurrences of a specific character in a string.

def countOccurrences(word, c):
 
    return word.count(c)


newWord = input('Enter the word: ').lower().strip()
while not newWord.isalpha():
    newWord = input('error! please enter a valid string: ')

char = input('Enter the character: ').lower().strip()
while not char.isalpha():
    newWord = input('error! please enter a valid character: ')
    
print(f'Number of occurrences of "{char}" in "{newWord}" is {countOccurrences(newWord, char)}.')