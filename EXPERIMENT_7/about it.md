# File Handling and Exception Handling

## Overview
This project demonstrates the concepts of File Handling and Exception Handling in Python. It covers basic file operations such as creating, reading, writing, and appending data to files, along with handling runtime errors using exception handling techniques.

## Objectives
- Understand file handling operations.
- Learn how to read from and write to files.
- Implement exception handling to manage errors.
- Improve program reliability and robustness.

## File Handling
File handling enables a program to store and retrieve data from files.

### Common File Operations
1. Create a file
2. Open a file
3. Read data from a file
4. Write data to a file
5. Append data to a file
6. Close a file

### Example
file = open("sample.txt", "w")
file.write("Hello, World!")
file.close()

## Exception Handling
Exception handling is used to handle errors that occur during program execution and prevent the program from crashing unexpectedly.

### Common Exceptions
- FileNotFoundError
- PermissionError
- ValueError
- ZeroDivisionError
- IOError

### Example
try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")

## Features
- File creation and management
- Reading and writing data
- Appending content to files
- Handling file-related exceptions
- User-friendly error messages

## Requirements
- Python 3.x
- Any Python IDE or code editor (VS Code, PyCharm, etc.)

## How to Run
1. Clone the repository.
2. Open the project folder.
3. Run the Python file using:

python main.py

## Output
The program performs file operations and handles exceptions gracefully by displaying appropriate messages whenever an error occurs.

## Conclusion
This project provides a basic understanding of file handling and exception handling in Python. These concepts are essential for developing reliable and efficient applications.

## Author
Garv Bhatia
