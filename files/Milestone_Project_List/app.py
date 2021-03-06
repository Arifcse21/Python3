from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd to delete a book
- 'q' to quit

Your Choice: """


def menu():
    user_inp = input(USER_CHOICE)
    while user_inp != 'q':
        if user_inp == 'a':
            prompt_add_book()
        elif user_inp == 'l':
            list_book()
        elif user_inp == 'r':
            prompt_read_book()
        elif user_inp == 'd':
            prompt_delete_book()
        else:
            print("Unknown command! Please try again")

        user_inp = input(USER_CHOICE)


def prompt_add_book():
    name = input("Enter the new book name: ")
    author = input("Enter the new book author: ")

    database.add_book(name, author)


def list_book():
    books = database.get_all_books()
    for book in books:
        read = "YES" if book["read"] else "No"
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():
    name = input("Enter the name of book you just finished reading: ")
    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter the name of ook you wish to delete: ")
    database.delete_book(name)


menu()














    
    
    


