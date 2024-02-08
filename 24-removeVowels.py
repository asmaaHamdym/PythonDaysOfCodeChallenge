#Write a program to remove vowels from a given string.
vowels = set(['a', 'e', 'o', 'i', 'u'])


def removeVowels(phrase):
    
    for letter in phrase:
        if letter in vowels:
           phrase = phrase.replace(letter, '')   
    return phrase

def main():

    newPhrase = input('Enter the string: ').lower().strip()
    while not newPhrase:
        newPhrase = input('error! please enter a valid string: ')
    print(f'{newPhrase} after removing vowels: {removeVowels(newPhrase)}.')






if __name__ == "__main__":
    main()