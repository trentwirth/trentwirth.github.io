# Step 13

In step 12, you were introduced to modular programming and file I/O (input/output) operations. In Step 13, we will continue to explore **Modules and File Operations** by combining them in a cohesive manner. We’ll expand our knowledge of file handling, delve into advanced file operations, and use Python's built-in modules to work with both CSV and JSON formats. You’ll also learn how to handle errors that may occur during file processing, ensuring your programs run smoothly.

---

## 1. Introduction to Modules and File Operations

In behavioral science and psychology, data collection is key. Working with datasets efficiently requires tools that let you organize and manage your code and data. **Modules** allow you to break down your code into reusable components, and **File Operations** enable you to save, retrieve, and process data stored in files.

In this step, we’ll combine modular programming with file operations, ensuring that your programs are well-structured and can handle data in multiple formats, such as **CSV** and **JSON**.

---

## 2. Importing Built-in Modules

Python provides various built-in modules that simplify tasks like interacting with files and directories. Let’s start with the `os` module for working with your system’s file structure.

### The `os` Module

The `os` module provides functions for interacting with the operating system. You can use it to navigate directories, check if files exist, and even remove or rename files.

#### Example: Using `os` to Work with Files and Directories

Here’s how you can use the `os` module to interact with files and directories:

```python
import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# List all files in the current directory
files = os.listdir(current_directory)
print(f"Files: {files}")

# Check if a file exists
if os.path.exists("data.txt"):
    print("The file 'data.txt' exists.")
else:
    print("The file 'data.txt' does not exist.")
```

### Exercise: Use `os` to Check if a File Exists
- Write a Python script that checks if a file called `experiment_data.txt` exists in the current directory. If the file exists, read its contents; if not, print a message saying the file is missing.

---

## 3. Working with CSV Files

In the behavioral sciences, data often comes in **CSV (Comma Separated Values)** format. The `csv` module in Python makes it easy to write (create) and read (work with) CSV files. 

CSV files are often used because they are simple, human-readable, and compatible with many data processing tools, such as Excel.

### Writing to a CSV File

You can write data to a CSV file using the `csv.writer()` method. Here’s how:

```python
import csv

# Data to write
data = [
    ['Name', 'Age', 'Occupation'],
    ['Alice', '29', 'Therapist'],
    ['Bob', '34', 'Psychologist']
]

# Open a CSV file for writing
with open('occupation_data.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    
    # Write each row to the CSV file
    csv_writer.writerows(data)
```

### Reading from a CSV File

To read data from a CSV file, use the `csv.reader()` function:

```python
import csv

# Open the CSV file
with open('occupation_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Loop through the rows in the CSV
    for row in csv_reader:
        print(row)
```

---

## 4. Working with JSON Files

**JSON (JavaScript Object Notation)** is another popular format for storing structured data. It’s easy to read and write, and closely resembles Python dictionaries. JSON is commonly used for storing data in web applications and APIs.

### Writing and Reading JSON Files

You can use the `json` module to write and read JSON files.

#### Example: Writing and Reading JSON
```python
import json

# Writing to a JSON file
data = {"name": "Alice", "age": 30, "occupation": "Therapist"}
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading from a JSON file
with open("data.json", "r") as file:
    data_loaded = json.load(file)
    print(data_loaded)
```

---

## 5. Handling File Exceptions

When working with files, errors such as a missing file or permission issues can occur. It’s important to handle these exceptions to prevent your code from crashing.

### Example: Handling File Errors
```python
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
```

---

## Final Exercise: Bringing It All Together

Now that you've learned how to work with both CSV and JSON files, and handle file errors, let's put everything together. 

### Instructions:

1. **Create a Custom Module for File Operations**:
    - Create a `file_utils.py` file that contains functions for reading/writing both CSV and JSON files.
    - Include error handling in this module to manage missing or corrupted files.

2. **Create a Class System for Data Collection**:
    - Create a Python script that defines two classes: `User` and `Survey`.
        - The `User` class should have attributes for `name`, `age`, and `profession`.
        - The `Survey` class should manage a collection of `User` objects and provide methods for writing the data to both CSV and JSON formats.

3. **File Operations**:
    - Collect user data and save it to **both** a CSV and a JSON file using your `file_utils.py` functions.
    - Implement a function to load the saved data back into your program from either format (CSV or JSON) and print it to the console.

4. **Exception Handling**:
    - Ensure that your program handles errors gracefully if the file does not exist or is corrupted.
    - If the program fails to load the CSV or JSON file, it should print a user-friendly error message.

!!! Tip "Practice for your Written Assessment"
    To practice for the written assessment, outline how you would solve this problem before you start your implementation. You can write out your solution on a piece of paper or in your text editor of choice (Google/Word Doc, etc.). Be as detailed as you can manage. Once you're done with this, then use your outline to implement the solution - how close were you? What did you forget? Answering these questions will help you prepare for the written assessment!

??? Tip "Potential Solution"
    1. **file_utils.py**:
    ```python
    import os
    import csv
    import json

    def file_exists(file_path):
        return os.path.exists(file_path)

    def read_json(file_path):
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")
        except json.JSONDecodeError:
            print(f"Error: Could not decode {file_path}.")

    def write_json(file_path, data):
        with open(file_path, "w") as file:
            json.dump(data, file)

    def read_csv(file_path):
        try:
            with open(file_path, "r") as file:
                return list(csv.reader(file))
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")

    def write_csv(file_path, data):
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
    ```

    2. **survey.py**:
    ```python
    from file_utils import write_csv, write_json

    class User:
        def __init__(self, name, age, profession):
            self.name = name
            self.age = age
            self.profession = profession

    class Survey:
        def __init__(self):
            self.users = []

        def add_user(self, user):
            self.users.append(user)

        def save_data(self, csv_file, json_file):
            data = [[user.name, user.age, user.profession] for user in self.users]
            write_csv(csv_file, data)
            write_json(json_file, data)

    survey = Survey()
    user1 = User('Alice', 29, 'Therapist')
    user2 = User('Bob', 34, 'Psychologist')
    survey.add_user(user1)
    survey.add_user(user2)
    survey.save_data('user_data.csv', 'user_data.json')
    ```

---

## Reflect and Review

At this point, you should understand how to combine **modular programming** and **file operations** to handle data in CSV and JSON formats. You’ve also learned how to handle file-related errors to ensure your program runs smoothly even when issues arise.

Reflect on how you can apply these skills in real-world behavioral science research. Handling data in various formats is crucial for data analysis and collaboration. Moreover, using **modular programming** makes your code more maintainable, reusable, and easier to debug.