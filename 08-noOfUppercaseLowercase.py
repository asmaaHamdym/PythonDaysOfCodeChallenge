#Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it
def caseCounter(word):
    upperCount, lowerCount = 0, 0

    for letter in word:
        if letter.islower():
            upperCount += 1
        else:
            lowerCount += 1
    
    return [lowerCount, upperCount]

while True:
    newWord = input('Enter the word: ').strip()
    if newWord.isalpha():
        break
    newWord = print('error! please enter a valid string!')


print(f'Number of lower case letters in {newWord} is {caseCounter(newWord)[0]}.')

print(f'Number of upper case letters in {newWord} is {caseCounter(newWord)[1]}.')