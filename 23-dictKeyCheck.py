#Write a program that checks if a key exists in a dictionary.

def searchDict(dict, key):
    if key in dict:
        return dict[key]
    else:
        return "The key does not exist!"

def main():
   books_dict = {
    "The Great Gatsby": "F. Scott Fitzgerald",
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "Pride and Prejudice": "Jane Austen",
    "The Catcher in the Rye": "J.D. Salinger",
    "Harry Potter and the Sorcerer's Stone": "J.K. Rowling",
    "The Lord of the Rings": "J.R.R. Tolkien",
    "The Da Vinci Code": "Dan Brown",
    "The Hunger Games": "Suzanne Collins",
    "The Alchemist": "Paulo Coelho"
}
   
   print(searchDict(books_dict, 'The Great Gatsby'))
   print(searchDict(books_dict, 'Gone with the Wind'))







if __name__ == "__main__":
    main()