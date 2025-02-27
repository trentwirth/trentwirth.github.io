# Step 3

## Getting Python Set up in VS Code

> Note: If you haven't installed VSCode yet, go back to Step 1.

With VSCode installed, getting Python set up is fairly straight forward. 

- Open VSCode
- Click on the Extensions icon on the left side of the window (it looks like a square with a few smaller squares in it)
- Search for "Python" in the search bar
- Click the green "Install" button on the Python extension by Microsoft
- Once the extension is installed, click the green "Reload" button to activate the extension

## Jupyter Notebooks

You've already used a Jupyter Notebook without realizing it; all Google Colab Notebooks are Jupyter Notebooks! Jupyter Notebooks are a great way to write and run Python code in a more interactive way than a traditional script.

Jupyter compartments your code into "cells" that can be run independently of one another. This is great for debugging and testing code, as you can run a single cell to see if it works as expected.

There are many ways to create a new Jupyter Notebook file in VSCode, one of the easiest ways is to click `File > New File` and then either save the file with a `.ipynb` extension or `Jupyter Notebook` in the file type dropdown that pops up.

> Note: Any time you are prompted by VSCode to install a new package or extension relating to Python or Jupyter Notebooks, you should do so. These packages and extensions are what make Python and Jupyter Notebooks work in VSCode.

## Introduction to Python Data Types

Python has several built-in data types that are used to store different kinds of information. Here are some of the most common data types:

- **Integers**: Whole numbers, e.g., `1`, `42`, `-7`
- **Floats**: Decimal numbers, e.g., `3.14`, `0.001`, `-2.5`
- **Strings**: Text, e.g., `"hello"`, `"Python"`, `"123"`
- **Booleans**: True or False values, e.g., `True`, `False`

### Examples of Data Types

```python
# Integer
a = 10

# Float
b = 3.14

# String
c = "Hello, Python!"

# Boolean
d = True
```

## Variables in Python

Variables are used to store data that can be referenced and manipulated in a program. They act as containers for values.

### Variable Naming Conventions
- Variable names must start with a letter or an underscore (`_`), such as `_myVar` or `myVar`.
- The rest of the name can contain letters, numbers, or underscores, examples: `myVar`, `my_var`, `myVar123`.
- Variable names are case-sensitive (e.g., `myVar` and `myvar` are different).

!!! tip "Consistency is Key"
    When you start a project, try to pick a variable naming style and stick to that style throughout your code. This will make your code more readable and maintainable. There are a few styles commonly used in Python:

    - **Snake Case**: `my_variable_name` (**recommended for Python**, where all letters are lower case and spaces are replaced with underscores)
    - **Camel Case**: `myVariableName` (the first word is lowercase, and the subsequent words are capitalized, no spaces. This is commonly used in JavaScript and C#)
    - **Pascal Case**: `MyVariableName` (the first letter of each word is capitalized, no spaces. This is commonly used in C# and Java)

    If you choose to use something other than snake case for python, that's fine! But remember to be consistent.

### Assigning Values to Variables

You can assign values to variables using the assignment operator (`=`).

### Examples of Variable Assignments
```python
# Assigning values to variables
x = 5
y = 10.5
name = "Alice"
is_student = True
```

!!! Tip "Variable Reassignment"
    You can reassign a variable to a different value at any time. The new value can be of the same or a different data type - be careful when reassigning variables to avoid confusion!

### Type Checking

You can check the data type of a variable using the `type()` function.

```python
# Check the data type of a variable
x = 5
print(type(x))  # Output: <class 'int'>
```

If you run the code snippet above, you will see that the output is `<class 'int'>`, indicating that the variable `x` is an integer.
> Note: "class" here is a Python term that refers to the data type of the variable. Data classes are important, and we will learn more about them in the future.

Here are the different outputs for the different types we've covered in today's Path Step:

- `int` for integers
- `float` for floats
- `str` for strings
- `bool` for booleans

!!! Tip "Try it out!"
    Open up a new Collab Notebook and create a variable assigment. Then, in a subsequent cell, use the `type()` function to check the data type of the variable. Did it work the way you thought?

## Reflect

Why might there be different data types in programs? (Answer below)

??? Tip "Answer"
    There are a lot of reasons! But here are a few that I can come up with from the perspective of a scientific programmer:

    1. As scientists, we work with lots of different types of data - often at the same time. We might want to construct pipelines specifically designed for a particular data type; later on in our class we'll create functions. Some functions can be are type-specific, meaning they will only work if we supply that function with the correct data type. This is a good thing, because it means we can be sure that our functions are doing what we expect them to do.
    2. Different data types have different properties. For example, you can't add a string to an integer in the same way you can add two integers. This can be useful for controlling the flow of your program and ensuring that you're not doing something you didn't intend to do.
    3. Different properties allow you to control the flow of your program in different and nuanced ways. For example, you can use booleans to control whether or not a particular block of code is executed. This can be useful for debugging (fixing your code), or for ensuring that your code is running as expected - we will talk more about program flow in Step 5!
    

## Review

In this step, we learned about different data types in Python and how to work with variables. Understanding data types and variables is essential for writing code in Python. Here's a quick recap:

- **Data Types**: Python has several built-in data types, including integers, floats, strings, and booleans.
- **Variables**: Variables are used to store data in a program. They act as containers for values.
- **Variable Naming Conventions**: Follow naming conventions to make your code more readable and maintainable.
- **Type Checking**: You can check the data type of a variable using the `type()` function.

# Colab Exercise

Now that you've learned about data types and variables, it's time to practice! 

Open up [this Colab Notebook](https://colab.research.google.com/drive/1YVOsMUGVhWHfogyxWpdxous4Ne85Y7k0?usp=sharing) and work through the exercises to reinforce your understanding.