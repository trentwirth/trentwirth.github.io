# Step 12

In Step 12, we will dive into two essential programming concepts: **Modular Programming** and **File I/O (Input/Output)**. These concepts allow you to break down your code into manageable pieces and interact with files, which are crucial in scientific programming for saving and loading data.

Up until now, we've focused on writing code in a single file. However, as your programs grow in complexity, it becomes challenging to manage everything in one place. Modular programming helps you organize your code into separate modules, making it easier to maintain and reuse.

!!! Tip "Using a `.py` File"
    Up until this point, we've been using python of "Jupyter" Notebooks (`.ipynb`), however, most python code is written inside of a file *without* predefined code blocks. Notebooks with codeblocks are incredibly useful for learning how to program and learn how functions work; it is a tool that you will always want in your belt! However, when you are writing a program that you want to run on its own (without you "pressing play"), you will want to write it in a `.py` file.

## Modular Programming

Modular programming refers to breaking down your code into smaller, reusable pieces called **modules**. This makes your code more organized, easier to maintain, and promotes reusability.

### Why Use Modular Programming?

- **Code Reusability**: Instead of writing the same code multiple times, you can write a function or a class once and use it across multiple programs or modules.
- **Maintainability**: By dividing the code into separate modules, it becomes easier to locate and fix bugs or add new features without affecting the entire program.
- **Readability**: Modular code is generally more readable and easier to follow, especially in large projects.

### Creating and Using Modules

In Python, a module is simply a file that contains Python code. You can create a module by saving functions, classes, or variables in a `.py` file and then importing it into another file. 

To be clear, this is not in a Jupyter Notebook, but in a `.py` file - you can create a new file in VSCode and save it as `math_operations.py` and then write your functions in that file, below.

#### Example: Creating and Importing a Module

Let's create a simple module called `math_operations.py` that contains a few basic mathematical functions.

**`math_operations.py`**:
```python
# This is a module that contains mathematical operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
```

Now, create a new python file in the same directory (folder). You can then import the `math_operations.py` module into this new Python file and use its functions:

**Using the `math_operations` module**:
```python
import math_operations

result_add = math_operations.add(10, 5)
result_divide = math_operations.divide(10, 2)

print(f"Addition Result: {result_add}")
print(f"Division Result: {result_divide}")
```

### Importing Specific Functions

You can also import specific functions from a module instead of the whole module.

```python
from math_operations import add, divide

result_add = add(10, 5)
result_divide = divide(10, 2)

print(f"Addition Result: {result_add}")
print(f"Division Result: {result_divide}")
```

### Exercises: Create and Import Modules
1. **Create a `string_operations.py` module**: 
    - Define functions like `count_vowels` and `reverse_string`.
2. **Import and use the module**:
    - Write a Python script to use the functions from `string_operations.py` to process some input text.

---

## File I/O (Input and Output)

File I/O refers to the process of reading from and writing to files. In Python, file handling is done using built-in functions like `open()`, `read()`, and `write()`.

### Working with Files

Python makes it easy to work with files using the `open()` function. When you open a file, you can choose different modes like:

- **'r'**: Read mode (default) – Opens a file for reading.
- **'w'**: Write mode – Opens a file for writing (creates a new file or overwrites an existing file).
- **'a'**: Append mode – Opens a file for appending (adds new data at the end of the file).
- **'r+'**: Read and write mode – Opens a file for both reading and writing.

### Reading from a File

The `read()` method reads the entire content of a file, and `readline()` reads one line at a time.

#### Example: Reading from a File

Suppose we have a file called `data.txt` with the following content:

**`data.txt`**:
```txt
Hello, this is a sample file.
It contains multiple lines.
Each line has some text.
```

We can read this file using Python:

!!! Tip "Check your Directory"
    Make sure the file you are trying to read is in the same directory as your Python script.

```python
# Open the file in read mode
file = open("data.txt", "r")

# Read the entire file
content = file.read()

# Close the file
file.close()

print(content)
```

### Writing to a File

The `write()` method allows you to write content to a file. Be careful when using the write mode (`'w'`) as it will overwrite any existing content in the file.

#### Example: Writing to a File

```python
# Open the file in write mode
file = open("output.txt", "w")

# Write to the file
file.write("This is the first line.\n")
file.write("This is the second line.\n")

# Close the file
file.close()
```

### Appending to a File

The append mode (`'a'`) allows you to add content to the end of the file without overwriting the existing content.

#### Example: Appending to a File

```python
# Open the file in append mode
file = open("output.txt", "a")

# Append to the file
file.write("This is an appended line.\n")

# Close the file
file.close()
```

### Using `with` to Handle Files

It's a good practice to use the `with` statement when working with files. This automatically closes the file after the block of code is executed, even if an error occurs.

#### Example: Using `with`

```python
# Using 'with' to open and read a file
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

The file will be automatically closed after the block of code inside `with` is executed.

### Exercises: Working with Files
1. **Read a file**: Create a file called `my_data.txt` and write a Python script to read and print its contents.
2. **Write to a file**: Write a Python script that writes user input to a file called `user_data.txt`.
3. **Append to a file**: Modify the script to append new user input to `user_data.txt` without overwriting the existing content.

---

## Reflect

Think about how modular programming and file I/O can help in scientific programming. Why might you want to break your code into modules? How could file I/O be useful in experiments or data analysis?

## Review

In this step, we covered two important topics:

- **Modular Programming**: Breaking down code into reusable modules and importing them into other files.
- **File I/O**: Reading from and writing to files in Python.

These concepts are essential for organizing your code and handling data efficiently in larger programming projects.