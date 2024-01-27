# Write a function that counts the frequency of each word in a sentence.
def countWord(keyword, wordArr):
    count = 0
    for word in wordArr:
        if keyword == word:
            count += 1
    return count

    
while True:
    sentence = input("Enter the sentence: ").lower()
    if sentence:
        break
    print("This can't be empty")

while True:
    word = input("Enter the word to count: ")
    if word:
        break
    print("This can't be empty")

print(f'The frequency of "{word}" in "{sentence}" is {countWord(word, sentence.split())}')