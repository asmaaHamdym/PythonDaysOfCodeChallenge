# Create a program that capitalizes the first letter of each word in a sentence

def titleCase(wordsArr):
    for i in range(len(wordsArr)):
        wordsArr[i] = wordsArr[i].capitalize()
    
    return " ".join(wordsArr)
   
while True:
    sentence = input("Enter the sentence: ").strip()
    if sentence:
        break
    print("This can't be empty")
    
print(titleCase(sentence.split()))