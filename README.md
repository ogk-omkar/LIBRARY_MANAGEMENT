Library Management System
A simple command-line Library Management System developed in Python using Object-Oriented Programming (OOP).
The program allows users to view books, search for books, borrow books, return books, and exit the system.
1. Project Overview
This project is designed as a beginner-friendly Python application for managing a small library.
The system stores:
- Book ID
- Book title
- Author name
- Borrowing information
- Student name
- Student ID
The project runs completely in the command line/terminal and does not require a graphical interface or database.
2. Features
1. Display Books
   - Shows all books in the library.
   - Displays whether each book is available or borrowed.
2. Search Book
   - Searches for a book using its title or author.
   - Search is not case-sensitive.
3. Borrow Book
   - Allows a student to borrow an available book.
   - Takes the student's name and ID.
   - Prevents a book from being borrowed twice.
4. Return Book
   - Allows a borrowed book to be returned.
   - Checks whether the book exists.
   - Checks whether the book is currently borrowed.
5. Exit
   - Closes the application.
3. Technologies Used
- Programming Language: Python
- Programming Concept: Object-Oriented Programming (OOP)
- Interface: Command Line / Terminal
- Data Storage: Python dictionaries
- External Libraries: None
4. Requirements
Before running the project, make sure Python is installed.
Required
- Python 3.8 or later
- Command Prompt, PowerShell, Terminal, or any Python-supported IDE
No additional Python packages are required.
5. Project Structure
Library-Management-System/
│
├── library.py
└── README.md
Files
library.py
Contains the complete Python source code for the Library Management System.
README.md
Contains the project description, setup instructions, usage instructions, and other project information.
6. Installation and Setup
Step 1: Install Python
Install Python 3 on your computer.
On Windows, make sure to select:
Add Python to PATH
After installation, open Command Prompt and check the Python version:
python --version
You should see something similar to:
Python 3.x.x
If python does not work on your system, try:
py --version
7. Download or Clone the Project
If the project is available on a Git repository, clone it using:
git clone <repository-url>
Then move into the project folder:
cd Library-Management-System
If you downloaded the project as a ZIP file, extract it and open a terminal inside the extracted project folder.
8. Dependencies
This project does not require any external Python packages.
It only uses Python's built-in features such as:
- Classes
- Dictionaries
- Loops
- Conditional statements
- Functions
- User input
- Standard output
Therefore, you do not need to run pip install.
9. Configuration
No configuration file, database, API key, password, or environment variable is required.
The initial books are added directly inside the Python program.
Example:
librar.books["101"] = Book(
    "101",
    "The Hobbit",
    "J.R.R Tolkien"
)
You can add or remove books by editing the book entries in library.py.
10. Running the Project
Open a terminal in the project directory.
Run the program using:
python library.py
On some Windows systems, you can also use:
py library.py
The program will display the main menu:
Library Management
1.Display books
2.Search book
3.Borrow book
4.Return book
5.Exit

enter your choice
11. Example Usage
Display Books
Select:
1
Example output:
all books
101 The Hobbit J.R.R Tolkien available
102 1984 George Orwell available
103 Harry Potter J.K Rowling available
104 Wings of Fire APJ Abdul Kalam available
105 INDIA 2020 APJ Abdul Kalam available
Search for a Book
Select:
2
Enter a title or author:
enter author apj
Example output:
104 Wings of Fire APJ Abdul Kalam available
105 INDIA 2020 APJ Abdul Kalam available
The search also works with part of a title or author name.
For example:
hobbit
can find:
The Hobbit
Borrow a Book
Select:
3
Enter the book ID:
enter book id to borrow 101
Then enter the student information:
enter your name Omkar
enter your id 23
Example output:
book borrowed
The program stores the borrower's name and student ID for that book.
If another user tries to borrow the same book, the program prevents the book from being borrowed again.
Return a Book
Select:
4
Enter the book ID:
enter book id to return: 101
Example output:
book returned
The book will become available again.
Exit
Select:
5
Output:
thank you
The program then closes.
12. How the Program Works
The project uses two main classes.
Book Class
The Book class represents an individual book.
It stores:
- Book ID
- Title
- Author
Library Class
The Library class manages the collection of books.
It contains two dictionaries:
self.books = {}
self.borrowed = {}
self.books stores the details of all books.
self.borrowed stores information about books that are currently borrowed.
For example:
self.borrowed["101"] = {
    "name": "Omkar",
    "student_id": "23"
}
This means that book 101 is currently borrowed by the student with the given name and ID.
13. Data Storage
The project currently stores data in memory using Python dictionaries.
This means:
- No database is required.
- No internet connection is required.
- Data is available while the program is running.
- Borrowing information is lost when the program is closed.
14. Error Handling
The program checks several common situations.
Invalid Book ID
If a user enters a book ID that does not exist:
book not found
Already Borrowed Book
If a user tries to borrow a book that is already borrowed:
book borrowed
Returning an Available Book
If a user tries to return a book that has not been borrowed:
book already available
Invalid Menu Choice
If the user enters a menu option other than 1–5:
invalid choice
15. Limitations
This is a simple command-line project, so it has some limitations:
- Data is not permanently saved.
- There is no database.
- There is no login system.
- There is no graphical interface.
- Only the predefined books are initially available.
- Borrowing information is cleared when the program closes.
16. Possible Future Improvements
The project can be extended by adding:
- Add new books
- Delete books
- Update book information
- Student registration
- Permanent data storage using files
- SQLite database
- Due dates
- Fine calculation
- Multiple library users
- Login system
- Graphical user interface
- Book issue history
17. Running Without Internet
Once Python is installed and the project files are available, the program can run completely offline.
No internet connection or external service is required.
18. License
This project is created for educational and learning purposes.
You are free to modify the code and extend the project for academic use.
