import json

FILE_NAME = "data.json"


def load_books():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Save books to file
def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


def add_book():
    books = load_books()
    book_title = input("Enter your book title: ")
    book_author = input("Enter the author name: ")
    book_status = input("What is the status? (Reading/whitelisted/Completed): ")
    books.append({"title": book_title, "author": book_author, "status": book_status})
    save_books(books)
    print(f"\n{book_title.upper()} IS ADDED TO THE BOOKS LIST..\n")
    return True


def list_books():
    books = load_books()
    if not books:
        print("\nNo books in the list. Please add books\n")
        return True
    for idx, book in enumerate(books, start=1):
        print(
            f"\n{idx}. '{book['title']}' by '{book['author']}' ---- [Status : {book['status']}]\n"
        )
    return True


def remove_book():
    books = load_books()
    if not books:
        print("\nNo books found to be removed.\n")
        return True

    book_name = input("Enter the book name you want to remove: ").lower()

    updated_books = [book for book in books if book["title"].lower() != book_name]

    if len(updated_books) == len(books):
        print(f"\nNo book with the title '{book_name}' was found.\n")
        return True

    save_books(updated_books)
    print("\nBook removed successfully.\n")
    return True


def search_books():
    books = load_books()
    if not books:
        print("\nNo books found to be searched.\n")
        return True

    book_name = input("Enter the book name you want to search: ").lower()

    for book in books:
        if book["title"].lower() == book_name:
            print(
                f"\n'{book['title']}' by '{book['author']}' ---- [Status : {book['status']}]\n"
            )
            return True

    print(f"\nNo book with the title '{book_name}' was found.\n")
    return True


def display_statistics():
    books = load_books()
    if not books:
        print("\nNo books found to display statistics.\n")
        return True

    reading_books = []
    whitelisted_books = []
    completed_books = []

    for book in books:
        if book["status"] == "reading":
            reading_books.append(book)
        elif book["status"] == "whitelisted":
            whitelisted_books.append(book)
        elif book["status"] == "completed":
            completed_books.append(book)

    print(f"\nTotal books in the list: {len(books)}")
    print(f"\nTotal books reading: {len(reading_books)}")
    print(f"\nTotal books to be read: {len(whitelisted_books)}")
    print(f"\nTotal books completed reading: {len(completed_books)}\n")
    return True


def main():
    print("\nLibrary Management System\n")
    program = True
    while program:
        print("Select any of the actions:")
        print("1. Add Book.")
        print("2. Display All Books.")
        print("3. Remove Book")
        print("4. Search Books")
        print("5. Display Statistics")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")
            continue

        if choice == 1:
            add_book()

        elif choice == 2:
            list_books()
        elif choice == 3:
            remove_book()
        elif choice == 4:
            search_books()
        elif choice == 5:
            display_statistics()
        elif choice == 6:
            print("\nExiting The Program.......\n")
            break
        else:
            print("\nInvalid Action.\n")

        while True:
            continue_program = input(
                "\nDo you want to continue using the program? (Yes/No): "
            ).lower()
            if continue_program in ["yes", "no"]:
                break
            else:
                print("Invalid input, please enter Yes or No")

        if continue_program == "no":
            program = False
            print("\nExiting The Program.......\n")


if __name__ == "__main__":
    main()
