# Personal Library Manager

This is a **CLI-based Personal Library Manager** written in Python that allows users to manage their personal book collection. It provides options to **add, list, and remove books** while storing the data in a JSON file.

## Features

✅ Add new books with title, author, and reading status  
✅ List all books with their details  
✅ Remove books by title  
✅ Store book data persistently in a JSON file  
✅ Simple and interactive command-line interface  

## Installation & Usage

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/personal-library-manager.git
cd personal-library-manager
```

### 2. Run the Program
Make sure you have Python installed.
```sh
python main.py
```

## How It Works

### 📌 Add a Book
When you select "Add Book", the program asks for:
- **Title** of the book
- **Author** name
- **Status** (Reading, Whitelisted, Completed)

Example:
```
Enter your book title: Atomic Habits
Enter the author name: James Clear
What is the status? (Reading/whitelisted/Completed): Reading

ATOMIC HABITS IS ADDED TO THE BOOKS LIST..
```

### 📌 List All Books
This displays all books stored in the library.json file.
```
1. 'Atomic Habits' by 'James Clear' ---- [Status : Reading]
```

### 📌 Remove a Book
You can remove a book by entering its title.
```
Enter the book name you want to remove: Atomic Habits
Book removed successfully.
```

## File Structure
```
📂 personal-library-manager
 ├── 📄 main.py  # Main Python script
 ├── 📄 data.json  # Stores book data (auto-created)
 ├── 📄 README.md  # Project documentation
```

## Contributing
Feel free to fork this project and submit pull requests with improvements!

## License
This project is open-source and free to use under the **MIT License**.
