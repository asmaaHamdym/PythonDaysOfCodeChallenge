# Write a program to reverse a given string.
def reverseString(s):
    return s[::-1]

word = input('Enter the string to be reversed: ').strip()
print(f"Reversed string: '{reverseString(word)}'")
