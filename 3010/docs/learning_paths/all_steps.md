# Step 1

## Some Basic Concepts

### **What is a Computer?**

If you think about it, you computer is a magic rock (aren't we all?)! It's a rock that can do math, remember things, and even talk to other rocks!

Your computer is composed of two main components: Hardware and Software.

The hardware is the physical parts of the computer - the things you can touch and see. This includes things like the monitor, keyboard, mouse, and the computer itself.

The software is the programs that run on the computer. This includes things like the operating system (Windows, Mac OS, Linux), web browsers, and the programs you use to do things like write documents, create spreadsheets, and play games.

In order for software to operate, it needs to know where to find the data it needs to run. This is where the file system comes in.

The file system is the way that data is stored on your computer. Think of the filing system like addresses on a street. Each file on your computer has an address, and the file system is the way that the computer knows where to find the data it needs.

To further understand the basics of the file system, we need to know what a "directory" and a "file" are.

### **What is a "Directory"?**

A directory is a place where files are stored. Think of a directory like a folder on your computer (for all intents and purposes, directory == folder). A directory can contain other directories, as well as files.

Directories are important because this allows us to provide distinct and organized "addresses" for our files. Keeping files organized, particularly for programming projects, is very important for scalability, and reproducability.

!!! Tip "Scientific Programming"
    File cleanliness and organization is particularly important in scientific programming. This is because we often need to share our code with others, or come back to it after a long period of time. If our code is not organized, it can be very difficult for us - or anyone else! - to understand what is going on.

### **What is a "File" and "File Extension"?**

A file is a collection of data that is stored on your computer. Files can contain text, images, videos, or any other type of data. Files are stored in directories, and each file has a name that is unique within the directory.

Files can be combined to create applications - think "apps". Applications are made up of many files that work together to provide specific functions. Examples of applications include web browsers, word processors, and games.

A file extension is a series of characters that are added to the end of a file name to indicate what type of file it is. For example, a file with the extension " `.txt`" is a text file, while a file with the extension "`.jpg`" is an image file. File extensions are important because they tell the computer what type of data is in the file, and how to open it. 

I'm a huge fan of the `.md` file extension, which is a markdown file - it's a great, non-proprietary way to write and format text.

??? Tip "Markdown"
    Markdown is a lightweight markup language that you can use to format text. It is often used to write documentation, README files, and other types of text that need to be formatted. Markdown is easy to learn, and you can use it to create headings, lists, links, and other types of formatting. 

    You can learn more about Markdown [here](https://www.markdownguide.org/).


## Tools we'll be using throughout this learning path:

### **Google Colab**

Google Colab, or "Colab Notebooks" is a completely free tool that allows you to write and execute Python code in your web browser. It is a great tool for learning Python, as it allows you to write and run code without having to install anything on your computer. It is also a great tool for sharing code with others, as you can easily share a link to your notebook with others, and they can view and run your code without having to install anything on their computer.

For a lot of the work we will be doing in our class, we will be using Google Colab. You can access Google Colab [here](https://colab.research.google.com/), and assignments will often be shared with you as a link to a Google Colab notebook.

### **VSCode**

Visual Studio Code (very often referred to as "VSCode") is a free code editor that is available for Windows, Mac, and Linux. It built and supported by Microsoft, and is a very powerful tool that can be customized to fit your needs. For the purposes of our class, we will most often be using Google Colab, but having VSCode installed on your machine will enable you to work on your code locally - this will be an optional path that you can take if you want to work on your code outside of Google Colab!

You can download VSCode [here](https://code.visualstudio.com/).

> Note: You do not want to download Visual Studio, which is a different product. Make sure you are downloading **Visual Studio Code** (VSCode).


### **GitHub**

GitHub is a website that allows you to store and share your code with others. It is a great tool for collaborating on code with others, and for sharing your code with the world.

The primary reason I'd like us to have access to GitHub - in the long term - is the integration of VSCode with their AI tool, GitHub Copilot. In my testing, I've found that GitHub Copilot is one of the best available coding AI tools out there - and as students at UC (or any other University), you have access to it for free!

## Exercises
1. Install VSCode on your computer (follow the link above in the `VSCode` section). We wont use this immediately, but we'll use it later!
2. Open and walk through your first [Google Colab Notebook](https://colab.research.google.com/drive/1PM0hFyBbP6k9TjMW8kVIz9_i_w9n4hCQ?usp=sharing) to get a taste of programming in Python!.
    - In this excercise you will:
        - learn how to run code in a Google Colab Notebook.
        - run your first "Hello World" program using a Colab Cell.
        - learn about comments and why they're important, especially for scientific programming.
        - be introduced to the concept of "variables" in programming.

# Step 2

In step 2, we have two objectives:

1. Get familiar with the VSCode interface, including the file explorer, terminal, and editor.
2. Introduce ourselves to the building blocks of Python, including environments, libraries, syntax, and programming terminology.

## Exercise: Intro to VSCode

### **Visually navigating VSCode**

Visual Studio Code (VSCode) is a powerful code editor. If you didn't install it yet, go back to `Step 1` and follow the instructions.

Here's a quick overview of its main components:

- **Activity Bar**: Located on the far left, it lets you switch between views and gives you access to different features.
- **Side Bar**: Shows different views like the Explorer, Search, Source Control, etc.
- **Editor**: The main area where you edit your files.
- **Panel**: Located at the bottom, it shows output, terminal, problems, etc.
- **Status Bar**: Displays information about the opened project and the current file.

### **Open up a new terminal**

1. **Open the Terminal**: 

    - Go to the top menu and select `Terminal > New Terminal`.
    - In the future, you can use the shortcut that is shown near `New Terminal`. Shortcuts are great!
    - If you toggle open the pannel (using the pannel button in the top right corner of the terminal), you can also create a new terminal from there by pushing the big `+` button.

2. **Print your current directory path**:
Use the `pwd` command to print the path of your current directory:
     ```sh
     pwd
     ```
This will show you the path to your current directory, remember this is like the "address" of where you are in your computer. When we create files and folders (new directories!) we will be doing so in this location.

!!! Tip "Code Blocks"
    Above, you'll notice a gray box with text inside. This is a code block. You can copy the text inside the block with the "copy" button on the far right of the box, and paste it into your terminal to run the command.
    
3. **Get to know your directory structure in the terminal**:
Use the `ls` command to list the contents of your current directory:
     ```sh
     ls
     ```

4. **Create a new directory called `a_folder_is_a_directory`**:
Use the `mkdir` command:
     ```sh
     mkdir a_folder_is_a_directory
     ```
> `mkdir` stands for "make directory" and is used to create new directories (or, "folders").

5. **Create a new directory called `a_folder_is_a_directory/this_is_a_directory_within_a_directory`**:
Use the `mkdir` command again:
     ```sh
     mkdir a_folder_is_a_directory/this_is_a_directory_within_a_directory
     ```
> This creates a directory within a directory, also known as a subdirectory.

6. **Create a file called `test_1.md` in the `this_is_a_directory_within_a_directory` directory**:
Use the `New-Item` command:
     ```sh
     New-Item -Name "test_1.md" -ItemType File
     ```
> `New-Item` is a command that tells the computer we want to make a new file. `-Name` and `-ItemType` are both parameters that you need to feed the `New-Item` command in order for it to work. In this case, we feed each parameter an "argument" in the space after it is presented, where "test_1.md" is the argument for the parameter `-Name` that specifies the file name.
>
> By default, this will create the file in your current directory. You can add an input parameter called "`-Path`" if you want to create a file in a particular location, like this: -Path `"C:\Users\wirthtd\downloads"`  

### **Navigate to the `a_folder_is_a_directory` directory in the VSCode file explorer**

1. **Open the Explorer**:

You should be able to see the directory/folder structure in the file explorer on the left side of the VSCode window. If you can't see it:

- Click on the Explorer icon in the Activity Bar (double-page icon in the top left of VSCode) or use the shortcut: `Ctrl + Shift + E` (`Cmd + Shift + E` on Mac).



2. **Navigate to the directory**:

    - Click on the `a_folder_is_a_directory` folder to expand it.
    - Then, click on the `this_is_a_directory_within_a_directory`.
    > Note: because there is *only* one directory within `a_folder_is_a_directory`, the two directories might appear stacked on a single line. If we added more content to `a_folder_is_a_directory`, it would open up in a way that appears more "normal". There are settings to change this behavior, but we won't worry about that right now.

### **Open the `test_1.md` file in the VSCode editor**

1. **Open the file**:
   - Double-click on `test_1.md` to open it in the editor.
   - This is a markdown (`.md`) file, you can learn more about markdown [here](https://www.markdownguide.org/)

## Intro to Python

Python is a high-level, interpreted programming language known for its readability and versatility. It's widely used in various fields, including web development, data analysis, artificial intelligence, and scientific computing.

### **Python Environment**

A *Python environment* is a setup that includes the Python interpreter, libraries, and other tools necessary to run Python scripts. Understanding and setting up a Python environment is crucial for ensuring that your Python projects run smoothly and are well-organized.

#### Components of a Python Environment

1. **Python Interpreter**: The core component that reads and executes Python code, telling your hardware what to do.
2. **Libraries and Packages**: Collections of pre-written code that perform common tasks, such as NumPy for numerical operations and Pandas for data manipulation. Think of these as special-purpose tools that you can use to build your projects. We'll go over some examples of libraries further down.
3. **Virtual Environment**: A self-contained directory that includes a specific version of Python and a set of libraries. This helps isolate projects from each other, preventing conflicts between dependencies.

#### Benefits of Using a Python Environment

- **Isolation**: Each project can have its own dependencies, avoiding conflicts with other projects.
- **Reproducibility**: Ensures that the code runs consistently across different machines.
- **Organization**: Keeps projects clean and manageable.

Using Python Environments on a project-to-project basis is a good practice to get into early on, and it is a critical concept in scientific software development!
> Reflect: Why might this be important in scientific software development?

### Python "Libraries"

Python has a rich ecosystem of "libraries" that extend its capabilities - this is one of the greatest advantages of Python, and is a result of it being the largest free and open source programming language in the world. 

*Remember*, a library is a collection of pre-written code that performs common tasks. Libraries are a critical component of your Python environment.

Here are some Python Libraries that are particularly common in scientific computing:

#### [*NumPy*](https://numpy.org/)

NumPy is a library for numerical computing in Python. It provides support for arrays, matrices, and many mathematical functions.

#### [*Pandas*](https://pandas.pydata.org/)

Pandas is a library for data manipulation and analysis. It provides data structures like DataFrames, which are essential for handling structured data.

#### [*Matplotlib*](https://matplotlib.org/)

Matplotlib is a plotting library for creating static, animated, and interactive visualizations in Python.

### **Some more basic programming terminology**

#### *Syntax*

Syntax refers to the set of rules that define the structure of a programming language - in other words, *syntax tells you the necessary rules for writing code*. 

In Python, syntax is designed to be readable and straightforward.

#### *Variables*

Variables are used to store data that can be referenced and manipulated in a program. You got a taste of variables in Exercise 1.

In Python, you can create a variable by assigning a value to it:

```python
x = 10
```

## Exercise
Go to [this Google Colab Notebook](https://colab.research.google.com/drive/1YJDwmEiYFeDrfHM_-xMiwwymplbkpe3R?usp=sharing) and work through importing a Python library, and exploring some Python syntax & variables.

### Bonus

??? Tip "Setting Up a Python Environment"
     > This is a bit advanced - we'll do this together eventually, but if you want to play around with environment set up you should go ahead!!

     1. **Install Python**: Download and install Python [from the official website](https://www.python.org/downloads/).

     2. **Create a Virtual Environment**:

          - Open your terminal or command prompt.
          - Navigate to your project directory.
          - Run `python -m venv env` (where `env` is the name of your environment).

     3. **Activate the Virtual Environment**:

          - On Windows: `.\env\Scripts\activate`
          - On macOS/Linux: `source env/bin/activate`

     4. **Install Libraries**: Use `pip install <library_name>` to add necessary libraries.

     *Example*

     ```bash
     # Create a virtual environment
     python -m venv myenv

     # Activate the virtual environment
     source myenv/bin/activate  # On macOS/Linux
     .\myenv\Scripts\activate  # On Windows

     # Install a library
     pip install numpy
     ```

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

# Step 4

In Step 4, we will dive into operators and expressions in Python. Operators allow us to perform various operations on data, and expressions combine variables and operators to produce new values. Understanding these concepts is crucial for writing effective and efficient code.

## Operators in Python

Python provides several types of operators that you can use to perform different operations on data. Here are the main types of operators:

### Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

- **Addition (`+`)**: Adds two numbers.
- **Subtraction (`-`)**: Subtracts the second number from the first.
- **Multiplication (`*`)**: Multiplies two numbers.
- **Division (`/`)**: Divides the first number by the second.
- **Modulus (`%`)**: Returns the remainder of the division.
- **Exponentiation (`**`)**: Raises the first number to the power of the second.

#### Examples of Arithmetic Operators
> You can run any of these examples in an `.ipynb` inside of VSCode, or in a Colab notebook.
??? tip "What's an `.ipynb`?"
    An `.ipynb` file is a "Jupyter Notebook" file that allows you to run Python code in a cell-by-cell format. You've already been working with these in Google Colab! You can create a new `.ipynb` file in VSCode by clicking on the `New File` button in the file explorer and selecting `Python 3` as the kernel. If you want to try this out, go for it! Ask a chatbot or your professor if you get confused.

```python
# Addition
result = 5 + 3
print("5 + 3 =", result)

# Subtraction
result = 10 - 4
print("10 - 4 =", result)

# Multiplication
result = 7 * 2
print("7 * 2 =", result)

# Division
result = 15 / 3
print("15 / 3 =", result)

# Modulus
result = 10 % 3
print("10 % 3 =", result)

# Exponentiation
result = 2 ** 3
print("2 ** 3 =", result)
```

### Comparison Operators

Comparison operators are used to compare two values and return a boolean result (`True` or `False`).

- **Equal to (`==`)**: Checks if two values are equal.
- **Not equal to (`!=`)**: Checks if two values are not equal.
- **Greater than (`>`)**: Checks if the first value is greater than the second.
- **Less than (`<`)**: Checks if the first value is less than the second.
- **Greater than or equal to (`>=`)**: Checks if the first value is greater than or equal to the second.
- **Less than or equal to (`<=`)**: Checks if the first value is less than or equal to the second.

#### Examples of Comparison Operators
> You can run any of these examples in an `.ipynb` inside of VSCode, or in a Colab notebook.

```python
# Equal to
print(5 == 5)  # True

# Not equal to
print(5 != 3)  # True

# Greater than
print(7 > 4)  # True

# Less than
print(3 < 8)  # True

# Greater than or equal to
print(6 >= 6)  # True

# Less than or equal to
print(2 <= 5)  # True
```

### Logical Operators

Logical operators are used to combine conditional statements.

- **AND (`and`)**: Returns `True` if both statements are true.
- **OR (`or`)**: Returns `True` if at least one statement is true.
- **NOT (`not`)**: Reverses the result, returns `False` if the result is true.

#### Examples of Logical Operators
> You can run any of these examples in an `.ipynb` inside of VSCode, or in a Colab notebook.

```python
# AND
print(True and True)  # True
print(True and False)  # False

# OR
print(True or False)  # True
print(False or False)  # False

# NOT
print(not True)  # False
print(not False)  # True
```

## Expressions in Python

Expressions are combinations of variables, operators, and values that produce a result. They are the building blocks of any Python program.

### Combining Variables and Operators

You can combine variables and operators to create expressions. Here are some examples:
> You can run any of these examples in an `.ipynb` inside of VSCode, or in a Colab notebook.

```python
# Arithmetic expression
x = 5
y = 3
result = x + y
print("x + y =", result)

# Comparison expression
is_greater = x > y
print("x > y:", is_greater)

# Logical expression
is_true = (x > y) and (y > 0)
print("(x > y) and (y > 0):", is_true)
```
## Exercise: Working with Operators and Expressions

Now it's time to practice using operators and creating expressions. You can do this your own Colab Notebook, in an `.ipynb` file in VSCode, or in a Python file in VSCode (we haven't done this last one yet - if you'd like to try,ask a chatbot or your professor!).

Try the following exercises:

### Exercise 1: Arithmetic Operators

Write a Python program that performs the following operations and prints the results:

1. Add two numbers.
2. Subtract one number from another.
3. Multiply two numbers.
4. Divide one number by another.
5. Find the remainder of the division of two numbers.
6. Raise one number to the power of another.

### Exercise 2: Comparison Operators

Write a Python program that compares two numbers using each of the comparison operators and prints the results.

### Exercise 3: Logical Operators

Write a Python program that uses logical operators to combine multiple conditions and prints the results.

### Exercise 4: Creating Expressions

Write a Python program that combines variables and operators to create expressions. Use arithmetic, comparison, and logical operators in your expressions.

## Reflect

Think about the different types of operators and expressions you've learned. How might you use them in your own programs? What are some real-world scenarios where these concepts might be useful?

## Review

In this step, we learned about different types of operators and expressions in Python. Here's a quick recap:

- **Arithmetic Operators**: Used to perform mathematical operations.
- **Comparison Operators**: Used to compare two values and return a boolean result.
- **Logical Operators**: Used to combine conditional statements.
- **Expressions**: Combinations of variables, operators, and values that produce a result.

Understanding these concepts is essential for writing effective and efficient code in Python.

# Step 5

In Step 5, we will explore control structures in Python, specifically focusing on making decisions using conditional statements. Control structures allow us to control the flow of our programs, making them more dynamic and responsive to different inputs and conditions.

!!! Tip "Write as you Go"
    As you work through this step, try writing code snippets in your own Notebook either in VSCode or Google Colab. This will help you practice and reinforce what you're learning.

## Indentations in Python

Indentation is a crucial aspect of Python syntax. Unlike many other programming languages that use braces `{}` to define code blocks, Python uses indentation to determine the grouping of statements. This means that the level of indentation (spaces or tabs) is used to define the structure and flow of your code.

!!! Tip "How to make an indentation?"
    In VSCode and Google Colab, you can create an indentation by pressing the `Tab` key on your keyboard. You can also use the `Shift` + `Tab` key to remove/reverse an indentation.

    *Weirdly*, in Python, the "prefered" way to indent is to use 4 spaces. This is because it is easier to read and is more consistent across different editors and platforms - because typically, when you press `Tab`, it creates a character `\t`. HOWEVER, most IDEs like VSCode will automatically convert tabs to 4 spaces for you - for the purposes of this class, you should be fine to use the `Tab` key.

### Why Indentation Matters

Indentation is not just for readability; it is a *fundamental part* of Python's syntax (remember, "syntax" is a way of saying "the way the program is written to be understood by the machine"). Incorrect indentation can lead to syntax errors or unexpected behavior in your code.

### Rules for Indentation

1. **Consistent Indentation**: Use the same number of spaces or tabs for each level of indentation. Mixing spaces and tabs can cause errors. Most 
2. **Standard Practice**: The standard practice is to use 4 spaces for each level of indentation. Most Python editors and IDEs (like VSCode) are configured to use 4 spaces by default.
3. **Indentation Levels**: Each level of indentation represents a new block of code. For example, the code inside an `if` statement or a loop must be indented.

### Example

We will learn about `if` statements in the next section below, but here's an example to illustrate the importance of indentation. This might make more sense after you learn what an `if` statement is, but for now think of an `if` statement as a way to check if a condition is true or false.

```python
x = 10
if x > 5:
    print("x is greater than 5")
    if x > 8:
        print("x is also greater than 8")
print("This line is outside the if statement")
```

In this example:

- The first `print` statement is indented once, so it is part of the `if x > 5` block.
- The second `print` statement is indented twice, so it is part of the `if x > 8` block, which is nested inside the first `if` block.
- The final `print` statement is not indented, so it is outside of the `if` block and will always be executed.

So, remember to pay attention to your indentation when writing Python code! It changes the way the code will be executed. Now, onto more fun things!

## Conditional Statements

Conditional statements are used to perform different actions based on different conditions. The most common conditional statements in Python are `if`, `elif`, and `else`.

### The `if` Statement

The `if` statement is used to test a condition. If the condition is true, the code block inside the `if` statement is executed.

!!! Tip "Recall: Boolean Operators"
    Remember that conditional statements rely on boolean expressions to determine whether a condition is true or false. We went over boolean operators in Step 4, but here's a quick refresher:
    
    A boolean expression is an expression that evaluates to either `True` or `False`. We can make the variable `condition` in the `if` statement is a boolean expression by setting it equal to to either `True` or `False` before we run the code. You can experiment with this in your own Notebook, printing out a value within the conditional statement to see how it changes.

#### Syntax

```python
if condition:
    # code block to be executed if the condition is true
```

#### Example

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

### The `elif` Statement

The `elif` statement is short for "else if". It allows us to check multiple conditions.

#### Syntax

```python
if condition1:
    # code block to be executed if condition1 is true
elif condition2:
    # code block to be executed if condition2 is true
```

#### Example

```python
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
```

### The `else` Statement

The `else` statement catches anything that isn't caught by the preceding conditions.

#### Syntax

```python
if condition1:
    # code block to be executed if condition1 is true
elif condition2:
    # code block to be executed if condition2 is true
else:
    # code block to be executed if none of the conditions are true
```

#### Example

```python
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is 5 or less")
```

!!! Tip "Play with it!"
    In a notebook, copy and paste the code above. Then try changing the value of `x` in the example above to see how the output changes based on the conditions.

## Exercise: Making Decisions with Conditional Statements

Now it's time to practice using conditional statements. You can do this in your own Colab Notebook, in an `.ipynb` file in VSCode, or in a Python file in VSCode.

### Exercise 1: Basic `if` Statement

Write a Python program that checks if a number is positive, negative, or zero and prints the result.

??? Tip "Solution"

    Here's a simple solution to the basic `if` statement problem:

    ```python
    x = 10
    if x > 0:
        print("x is positive")
    elif x < 0:
        print("x is negative")
    else:
        print("x is zero")
    ```

### Exercise 2: Using `elif` and `else`

Write a Python program that checks the grade of a student based on their score and prints the corresponding grade (A, B, C, D, or F).

??? Tip "Solution"

    Here's a simple solution to the grade-checking problem:

    ```python
    score = 85
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
    ```

## Reflect

Think about how conditional statements can be used to control the flow of a program. What are some real-world scenarios where these concepts might be useful?

??? Tip "Sorting Data"
    Conditional statements can be used to sort data, filter out unwanted information, or make decisions based on specific criteria. For example, you might use conditional statements to categorize products based on their price, filter out invalid user inputs, or determine the eligibility of a customer for a discount.

## Review

In this step, we learned about conditional statements in Python. Here's a quick recap:

- **`if` Statement**: Used to test a condition and execute a code block if the condition is true.
- **`elif` Statement**: Allows us to check multiple conditions.
- **`else` Statement**: Catches anything that isn't caught by the preceding conditions.

Understanding these concepts is essential for writing dynamic and responsive programs in Python.

# Step 6

In Step 6, we will focus on problem-solving using control structures. This step will build on the concepts of conditional statements and introduce loops, which are essential for creating dynamic and efficient programs.

## Problem-Solving with Control Structures

Control structures allow us to control the flow of our programs, making them more dynamic and responsive to different inputs and conditions. In this step, we will explore how to use control structures to solve problems.

### Loops in Python

Loops are used to execute a block of code repeatedly. Python provides two types of loops: `for` loops and `while` loops.

### The `for` Loop

The `for` loop is used to iterate over a sequence of numbers and execute a block of code for each number.

!!! Tip "`list`s in Python"
    A `list` is a collection of items that can be of different types. You can create a list by placing the items inside square brackets `[]`, separated by commas. For example:

    ```python
    numbers_list = [1, 2, 3, 4, 5]
    ```

    Lists are iterable, meaning you can loop over the items in a list using a `for` loop. Python makes great use of lists and other iterable objects to simplify programming tasks!

#### Syntax

```python
numbers_list = [1, 2, 3, 4, 5]

for number in numbers_list:
    # code block to be executed for each number in the list
```
#### Example

```python
numbers_list = [1, 2, 3, 4, 5]
for number in numbers_list:
    print(number)
```

??? Tip "The `range()` Function"
    The `range()` function is commonly used with `for` loops to generate a sequence of numbers. It takes three arguments: `start`, `stop`, and `step`. For example, `range(1, 6, 2)` generates the sequence `1, 3, 5`.

    You can also use `range()` with a single argument to generate a sequence starting from 0. For example, `range(5)` generates the sequence `0, 1, 2, 3, 4`. 

    You can use the `range()` function to iterate over a specific range of numbers in a `for` loop, like this: 

    ```python
    for i in range(1, 6):
        print(i)
    ```

#### Another Example

Just like you can loop over a list of numbers, you can loop over a string in Python. When you feed in a string to a `for` loop, it will iterate over each character in the string.

```python
for character in "This will print vertically":
    print(character)
```

### The `while` Loop

The `while` loop is used to execute a block of code as long as a condition is true.

#### Syntax

```python
while condition:
    # code block to be executed as long as the condition is true
```

#### Example

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

!!! Tip "The `+=` Operator"
    The `+=` operator is used to increment (add) the value of a variable. This is a shorter way to write 
    ```python
    variable = variable + 1
    ```
    
    `-=` can be used to decrement (subtract) the value of a variable, as well as `*=`, `/=`, and `**=` for multiplication, division, and exponentiation, respectively.

### Combining Loops and Conditional Statements

You can combine loops and conditional statements to create more complex control structures.

#### Example

```python
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers_list:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
```

## Exercise: Problem-Solving with Control Structures

Now it's time to practice using loops and conditional statements to solve problems. You can do this in your own Colab Notebook, in an `.ipynb` file in VSCode, or in a Python file in VSCode.

### Exercise 1: Simple Loops

Write a Python program that prints the numbers from 1 to 5 using a `for` loop, then do it again for a `while` loop.

??? Tip "Solution"
    Here's a simple solution to the simple loops problem:
    
    ```python
    # Using a for loop
    numbers_list = [1, 2, 3, 4, 5]
    for i in numbers_list:
        print(i)
    ```

    ```python
    # Using a while loop
    count = 1
    while count < 6:
        print(count)
        count += 1
    ```

### Exercise 2: Sum of Numbers

Write a Python program that calculates the sum of numbers from 1 to 10.

??? Tip "Hint"
    You can use a `for` loop combined with the `range()` function to iterate over the numbers from 1 to 10 and calculate the sum. You could also implement the `+=` operator to increment the sum for each number.

??? Tip "Solution"
    Here's a simple solution to the sum of numbers problem:
    
    ```python
    total = 0
    for i in range(1, 11):
        total += i
    print(f"The sum of numbers from 1 to 10 is: {total}")
    ```

### Exercise 3: FizzBuzz

Write a Python program that prints the numbers from 1 to 20. For multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

??? Tip "Solution"
    Here's a simple solution to the FizzBuzz problem:
    
    ```python
    for i in range(1, 21):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    ```
### Exercise 4: Counting Vowels

Write a Python program that counts the number of vowels in a given string.

??? Tip "Hint" 
    You can use a for loop to iterate over each character in the string and a conditional statement to check if the character is a vowel.

??? Tip "Solution" 
    Here is one solution to the problem:
    ```python
    string = "This is a sample string"
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    print(f"The number of vowels in the string is: {count}")
    ```

### Exercise 5: Reverse a String

Write a Python program that reverses a given string using a for loop.

??? Tip "Hint" 
    You can use a for loop to iterate over the string in reverse order and build a new string.

??? Tip "Solution" 
    Here's a possible solution:
    ```python
    string = "Hello, World!"
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    print(f"The reversed string is: {reversed_string}")
    ```

    *Think*: Why does this solution work?

### Exercise 6: Multiplication Table with F-Strings

Write a Python program that generates a multiplication table for numbers 1-5, using f-strings.

??? Tip "Hint" 
    You can use nested `for` loops to generate the multiplication table for numbers 1-5.

??? Tip "Solution"
    Here's a possible solution:
    ```python
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i} x {j} = {i * j}") # Print a new line after each row
    ```

    This solution uses nested `for` loops to generate the multiplication table for numbers 1-5. The outer loop iterates over the numbers 1-5 for the first multiplier, and the inner loop iterates over the numbers 1-5 again for the second number, generating a table of all multiplication results.

## Reflect

Think about how loops and conditional statements can be used to solve problems. What are some real-world scenarios where these concepts might be useful?

??? Tip "Automating Repetitive Tasks"
    Loops and conditional statements are essential for automating repetitive tasks and handling different conditions in programs. For example, you can use loops to process large datasets, iterate over files in a directory, or perform calculations based on specific conditions. Conditional statements can be used to control the flow of a program, handle user inputs, or make decisions based on certain criteria.

    Another tool, `functions`, can also be used to automate repetitive tasks. We'll learn about functions in the next step!

## Review

In this step, we learned about loops and how to use them in combination with conditional statements to solve problems. Here's a quick recap:

- **`for` Loop**: Used to iterate over a sequence of numbers and execute a block of code for each number.
- **`while` Loop**: Used to execute a block of code as long as a condition is true.
- **Combining Loops and Conditional Statements**: Allows for more complex control structures and problem-solving.

Understanding these concepts is essential for writing dynamic and efficient programs in Python.

# Step 7

In Step 7, we will explore functions in Python. Functions are reusable blocks of code that perform a specific task. They help us organize our code, make it more readable, and avoid repetition.

## Defining Functions

To define a function in Python, we use the `def` keyword (short for "define") followed by the function name and parentheses `()`. 

Inside the parentheses, we can specify parameters, or "inputs", that the function can accept. The function body is indented and contains the code that will be executed when the function is called.

### Syntax

```python
def function_name(parameters):
    # code block to be executed
```

### Example

```python
def greet(name):
    print(f"Hello, {name}!")
```

In this example, `greet` is the function name, and `name` is a parameter. The function prints a greeting message using the provided name.

## Calling Functions

To call a function, we use the function name followed by parentheses `()`. If the function accepts parameters, we pass the arguments inside the parentheses.

### Example

```python
greet("Alice")
```

This will output:

``` 
Hello, Alice!
```


## Return Statement

Functions can return a value using the `return` statement. This allows us to capture the result of a function and use it in other parts of our code.

### Example

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

This will output:

```
8
```

## Default Parameters

We can define default values for parameters in a function. If an argument is not provided when the function is called, the default value will be used.

### Example

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()
```

This will output:

```
Hello, World!
```

by default, the function uses "World" as the name. If we call the function without providing a name, it will use the default value, like this:

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet("Alice")

```

This will output:

``` 
Hello, Alice!
```

Try it yourself!


## Keyword Arguments

We can more flexibly use functions by telling the function what we want to use as input when we call that function.

Let's imagine a scenario where we have a "describe_pet" function that takes two parameters: "animal_type" and "pet_name", the function might look like this:

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")
```

We can specify the inputs, or "arguments", when we call the function by setting them equal to the parameter names. 

!!! Tip "Parameters & Arguments"
    The parameter is the name we give to the input in the function definition, and the argument is the actual value we pass to the function.

Here is an example of specifying that I have a dog named Rufus:
```python

describe_pet(animal_type="dog", pet_name="Rufus")
```

Note that when I specify the arguments (inputs), I can change the order and the function will work just fine:

```python
describe_pet(pet_name="Django", animal_type="dog")
```

So, in the code below, I can define the function and use the function twice in a row, changing the order of the arguments:

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type="dog", pet_name="Sherlock")
describe_pet(pet_name="Watson", animal_type="cat")
```

This will output:

```
I have a dog named Sherlock. I have a cat named Watson.
```


## Exercises

1. **Define a Function**: Write a function called `square` that takes a number as a parameter and returns its square.

    ??? Tip "Solution"
        ```python
        def square(number):
            return number * number

        result = square(5)
        print(result)
        ```

2. **Call a Function**: Write a function called `multiply` that takes two numbers as parameters and returns their product. Call the function with different arguments and print the results.

    ??? Tip "Solution"
        ```python
        def multiply(a, b):
            return a * b

        result1 = multiply(3, 4)
        result2 = multiply(5, 2)
        print(result1)
        print(result2)
        ```

3. **Default Parameters**: Write a function called `greet_user` that takes a name as a parameter and prints a greeting message. If no name is provided, it should use "User" as the default name.

    ??? Tip "Solution"
        ```python
        def greet_user(name="User"):
            print(f"Hello, {name}!")

        greet_user("Alice")
        greet_user()
        ```

4. **Keyword Arguments**: Write a function called `make_sandwich` that takes a list of ingredients and prints a message describing the sandwich. Call the function using keyword arguments to specify the ingredients in different orders.

    ??? Tip "Solution"
        ```python
        def make_sandwich(ingredients):
            print("Sandwich with:")
            for ingredient in ingredients:
                print(f"- {ingredient}")

        make_sandwich(ingredients=["bread", "cheese", "tomato"])
        make_sandwich(ingredients=["tomato", "bread", "cheese"])
        ```

## Reflect

Think about how functions can help you organize your code and make it more reusable. What are some real-world scenarios where you might use functions?

## Review

In this step, we learned about functions in Python. Here's a quick recap:

- **Defining Functions**: Use the `def` keyword to define a function.
- **Calling Functions**: Use the function name followed by parentheses to call a function.
- **Return Statement**: Use the `return` statement to return a value from a function.
- **Default Parameters**: Define default values for parameters in a function.
- **Keyword Arguments**: Specify arguments using parameter names when calling a function.

Understanding these concepts is essential for writing organized and reusable code in Python.

# Step 8

In Step 8, we will reinforce our understanding of functions by combining them with loops, conditionals, and type hints. This step will provide opportunities to practice and see how these concepts work together.

## Simple Function

Let's start with a simple function that adds two numbers.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

In this example, `add` is a function that takes two parameters `a` and `b`, and returns their sum.

## Using a Function in a Loop

Now, let's see how we can use this function in a loop to add numbers from a list.

```python
def add(a, b):
    return a + b

numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total = add(total, number)

print(total)
```

In this example, we use the `add` function in a `for` loop to sum all the numbers in the list.

## Functions with Various Data Types

Functions can work with different data types and return various outputs. Let's see some examples.

### Example 1: Concatenating Strings

```python
def concatenate(str1, str2):
    return str1 + " " + str2

result = concatenate("Hello", "World")
print(result)
```

### Example 2: Checking Even or Odd

```python
def is_even(number):
    if number == 0:
        return False # Zero is not considered even or odd, it is an "edge case"
                     # so we'll take care of it first.
    else:
        return number % 2 == 0 # Now that zero is taken care of, 
                               # this will work fine.

result = is_even(4)
print(result)
```

### Example 3: Finding the Maximum Value

```python
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

result = find_max(10, 20)
print(result)
```

## Introducing Type Hints

Type hints allow you to specify the expected data types of function parameters and return values. They do not enforce the types but provide useful information for code readability. 

### Syntax

Below is a template for how a functino with type hints would work, note, these are not real types:

```python
def function_name(parameter: type) -> return_type:
    # code block
```

??? Tip "Why Type Hints are Important"

    Type hints improve code readability and help others understand what types of arguments a function expects and what it returns. They also assist in catching type-related errors during development.

Note, we are not changing anything about the function here. All we're doing is being *more communicative* about how the function should be used.

Below are some examples of functions with type hints.

#### Example 1: Adding Integers

```python
def add(a: int, b: int) -> int:
    return a + b

result = add(3, 5)
print(result)
```

This function is pretty simple, it takes two integers, adds them together, and returns an integer.

#### Example 2: Concatenating Strings

```python
def concatenate(str1: str, str2: str) -> str:
    return str1 + " " + str2

result = concatenate("Hello", "World")
print(result)
```

"Concatenate" means to join two things together. In this case, two strings.

This function takes two strings and returns a new string that is the concatenation of the two input strings.

??? Tip "String Concatenation"

    [You can follow this link](https://www.w3schools.com/python/python_strings_concatenate.asp) to see more about string concatenation in Python.

#### Example 3: Checking Even or Odd

```python
def is_even(number: int) -> bool:
    if number == 0:
        return False 
    else:
        return number % 2 == 0

result = is_even(4)
print(result)

```
Note, we used this function before, all we've changes is that we now have type hints!

### What when we feed a function the wrong type?

```python
def add(a: int, b: int) -> int:
    return a + b

result = add("3", 5)  # This will produce an error...
```

This will raise a `TypeError` because we are trying to add a string and an integer, which is not allowed based on the type hints. In this case, it will also functionally break the code.

The type error will look like this:
```
TypeError: can only concatenate str (not "int") to str
```

Note, if you fed the `add()` function a *float*, even though it breaks the Type Hint, the code will still run. This is because Python is a "dynamically typed language", and it will try to do the operation you're asking it to do and only break if it can't.

So, Type Hints are not a "hard rule" in Python, but they are a great idea to follow because **code is read more often than it is written**.

## Using a Loop within a Function

You can use loops within functions to perform repetitive tasks.

### Example: Summing Numbers

```python
def sum_numbers(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

result = sum_numbers(10)
print(result)
```

The example above takes in an integer `n` and returns the sum of all numbers from 1 to `n`. It uses the range function to generate a sequence of numbers from 1 to `n` - remember that range doesn't include the last number, so we add 1 to `n` + 1 so that we include `n` in the sum.

## Combining Functions with Conditionals

You can combine functions with conditionals to perform different actions based on conditions.

### Example: Filtering Even Numbers

> NOTE: For the function below, `is_even` is a function that we defined earlier in this document. That means if you've run the `is_even` function in your `.ipynb` already, then this code will work just fine. If you haven't, you'll need to run the code block containing `is_even` function before you run this code.

```python
def filter_even(numbers: list[int]) -> list[int]:
    even_numbers = []
    for number in numbers:
        if is_even(number):
            even_numbers.append(number)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_even(numbers)
print(result)
```

This above function is great! It contains a loop that iterates over a list of numbers and uses the `is_even` function to check if each number is even. If the number is even (here, we use a conditional!), it is added to a new list called `even_numbers`, which is then returned.

This function combines a lot of what we've learned so far!

## Review

In this step, we reinforced our understanding of functions by exploring:

- **Simple Function**: Creating and using a basic function.
- **Using a Function in a Loop**: Applying a function within a loop.
- **Functions with Various Data Types**: Working with different data types and return values.
- **Introducing Type Hints**: Specifying expected data types for function parameters and return values.
- **Using a Loop within a Function**: Performing repetitive tasks within a function.
- **Combining Functions with Conditionals**: Using conditionals within functions to perform different actions.

Understanding these concepts is essential for writing robust and flexible code in Python.

## Exercises

> Rememeber: The solutions I provide are only one way to solve the problem. There are many ways to solve most coding problems! You should feel free to experiment and try different approaches.

1. **Type Hints**: Write a function called `concat` that takes two strings as parameters and returns their concatenation. Use type hints to specify the parameter and return types.

    ??? Tip "Solution"
        ```python
        def concat(str1: str, str2: str) -> str:
            return str1 + " " + str2

        result = concat("Hello", "World")
        print(result)
        ```

2. **Sum of Squares**: Write a function called `sum_of_squares` that takes an integer `n` and returns the sum of the squares of all numbers from 1 to `n`.

    ??? Tip "Solution"
        ```python
        def sum_of_squares(n: int) -> int:
            total = 0
            for i in range(1, n + 1):
                total += i ** 2
            return total

        result = sum_of_squares(5)
        print(result)
        ```

3. **Count Vowels**: Write a function called `count_vowels` that takes a string as a parameter and returns the number of vowels in the string. Use a loop to iterate over the string and count the vowels.

    ??? Tip "Solution"

        ```python
        def count_vowels(s: str) -> int:
            vowels = "aeiouAEIOU"
            count = 0
            for char in s:
                if char in vowels:
                    count += 1
            return count

        result = count_vowels("Hello, World!")
        print(result)
        ```

4. **Find Minimum**: Write a function called `find_min` that takes a list of integers and returns the smallest number in the list. Use a loop to iterate over the list and find the minimum value.


    ??? Tip "Solution"
        ```python
        def find_min(numbers: list[int]) -> int:
            min_number = numbers[0]
            for number in numbers:
                if number < min_number:
                    min_number = number
            return min_number

        numbers = [5, 3, 8, 1, 9, 2]
        result = find_min(numbers)
        print(result)
        ```

5. **Palindrome Check**: Write a function called `is_palindrome` that takes a string and returns `True` if the string is a palindrome (reads the same forwards and backwards) and `False` otherwise. Use a loop to check the characters.

    ??? Tip "Solution"

        ```python
        def is_palindrome(input_string: str) -> bool:
            input_string = input_string.lower() # This line makes it so we don't have to worry about capital letters.
            reversed_input_string = input_string[::-1]
            return input_string == reversed_input_string

        result1 = is_palindrome("radar")
        result2 = is_palindrome("hello")
        print(result1)
        print(result2)
        ```

## Bonus: Lambda Functions (One-Line Functions)

Lambda functions are small functions defined using the `lambda` keyword. They are often used for short, simple operations.

These are called "anonymous functions" because they don't have a name, we don't define ("`def`") them. They are useful when you need a simple function for a short period of time.

### Syntax

Note, the text below is a template, not real code:
```python
lambda parameters: expression
```

### Example: Squaring a Number

```python
square = lambda x: x * x
print(square(5))
```

### Example: Using Lambda with `filter`

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
```
of course, the above code has the 0 edge case... but hopefully this gives you an idea.

## Bonus Excercise: Using Lambda Functions

1. **Filtering Odd Numbers**: Use a lambda function with the `filter` function to filter out odd numbers from a list of integers.

    ??? Tip "Solution"

        ```python
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
        print(odd_numbers)
        ```

2. **Adding "1"**: With a super simple lambda function, add 1 to a number.

    ??? Tip "Solution"

        ```python
        add_one = lambda x: x + 1
        print(add_one(5))
        ```

# Step 9

In Step 9, we will focus on debugging Python code using Visual Studio Code (VSCode) and Jupyter Notebooks (`.ipynb` files). Debugging is an essential skill for any programmer, as it helps identify and fix errors in the code.

> Note: This is the kind of thing that it really helps to watch someone demonstrate what debugging looks like. I've done my best to include images, but attending class and asking questions is uniquely important for this Step.

## Introduction to Debugging

Debugging is the process of finding and fixing errors or "bugs" in your code. Bugs can be syntax errors, runtime errors, or logical errors. Understanding how to debug effectively will save you time and frustration.

??? Tip "Why "bug"?"
    The term "bug" originated in the early days of computing when an actual insect (a moth) caused a malfunction in a computer. Since then, the term has been used to describe any unexpected behavior in software.

### Types of Errors

1. **Syntax Errors**: These occur when the code is not written correctly according to the language's rules. For example, missing a colon at the end of an `if` statement (Trent does this all the time...).
2. **Runtime Errors**: These occur when the code is executed and something goes wrong, such as dividing by zero.
3. **Logical Errors**: These occur when the code runs without crashing - in other words, telling you that something is wrong - but produces incorrect results. These are often the hardest to find.

## Debugging in VSCode

VSCode provides powerful tools for debugging Python code, including support for Jupyter Notebooks. Here are the steps to debug a `.ipynb` file in VSCode.

### Setting Up the Debugger

1. **Open VSCode**: Make sure you have VSCode installed and open it.
2. **Install Python Extension**: If you haven't already, install the Python extension for VSCode.
3. **Open Your Notebook**: Open the `.ipynb` file you want to debug.

### Using Breakpoints

Breakpoints allow you to pause the execution of your code at specific lines, so you can inspect the state of your program.

1. **Set a Breakpoint**: Click in the gutter (the space to the left of the line numbers) next to the line where you want to set a breakpoint. A red dot will appear.

    - The "Gutter" is the region to the left of the line numbers in the editor.
    ![alt text](../images/gutter.png)

    - Hover your mouse over the gutter to see the breakpoint icon.
    ![alt text](../images/break_point_appears.png)

    - Click the dimmed breakpoint icon to set a breakpoint.
    ![alt text](../images/break_point_made.png)

    - Click the down arrow near the play button for the cell, and you will see the option to "Debug Cell"
    ![alt text](../images/debug_cell.png)

    - When you see the line highlighted in yellow, you have successfully set a breakpoint and you're now in debug mode!
    ![alt text](../images/debug_mode.png)

2. **Start Debugging**: Now, you can walk through your code line by line. You can use the buttons in the debug toolbar to continue, step into, over, out, restart, or disconnect the debugger (symbols from left to right in image above).

    - The "Continue" button will run the code until the next breakpoint.
    - The "Step Over" button will run the next line of code.
    - The "Step Into" button will go into the next function call.
    - The "Step Out" button will run until the current function returns.
    - The "Restart" button will restart the debugger.
    - The "Disconnect" button will stop the debugger.

3. **Inspect Variables**: When the code execution pauses at a breakpoint, you can hover over variables to see their current values or use the Variables pane to inspect them.

    - To the left of the notebook, you will see the "Variables" tab. Click on it to see the variables in the current scope.
    - Note: in a Jupyter Notebook, the first time you run through the cell, your variables wont be identified yet, but they will be after the first run through. This means that if your code relies on a variable that is defined in a specific sequence, you'll need to restart the kernel and run the cell again.
    ![alt text](../images/variable_space.png)

    - You can also check variables and test code in the debug console (located at the bottom of VSCode). This is a great and useful way to test code without having to run the entire cell again or update your notebook.
    ![alt text](../images/debug_console.png)

### Reading Error Outputs

When an error occurs, VSCode will display an error message in the terminal or output pane. Understanding these messages is crucial for debugging.

1. **Error Message**: The error message will tell you what went wrong and where it happened. For example, `ZeroDivisionError: division by zero` indicates that you tried to divide a number by zero.
2. **Traceback**: The traceback shows the sequence of function calls that led to the error. This can help you pinpoint where the error occurred in your code.

## Exercises

Now, let's practice debugging with some exercises. Each exercise contains code with intentional errors. Your task is to find and fix the errors.

### Exercise 1: Syntax Error
Goal: Find and fix the syntax error.

```python
def greet(name)
    print(f"Hello, {name}!")
    
greet("Alice")
```

??? Tip "Hint" 
    Look for missing punctuation.

### Exercise 2: Runtime Error
Goal: Read and understand the error.

```python
def divide(a, b):
    return a / b

result = divide(10, 0)
print(result)
```

??? Tip "Hint" 
    Think about what happens when you divide by zero.

### Exercise 3: Logical Error
Goal: Fix the logical error in the code.

```python
def is_even(number):
    return number % 2 == 1

result = is_even(4)
print(f"Is 4 even? {result}")
```

??? Tip "Hint" 
    This code functions, but isn't working properly. 

    Check the logic used to determine if a number is even - does this make sense?

### Exercise 4: Using Breakpoints
Goal: Practice setting breakpoints and inspecting variables.

```python
def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)
print(f"The sum of the list is: {result}")
```

??? Tip "Hint"
    Set a breakpoint inside the loop and inspect the value of `total` at each iteration.

    You've likely funtionally done this with print statements before, but this is a more efficient and less permanent way to do it.

### Exercise 5: Reading Error Outputs
Goal: Read, understand, and fix the (new) error.

```python
def get_item(lst, index):
    return lst[index]

my_list = [1, 2, 3]
result = get_item(my_list, 5)
print(result)
```

??? Tip "Hint" 
    Carefully read the error message and traceback to understand what went wrong. If you don't understand the error, try asking Microsoft Copilot what the error means :) If that doesn't help, ask the professor!

## Reflect

Think about how debugging can help you understand your code better and improve your problem-solving skills. What strategies can you use to debug more effectively?

## Review

In this step, we learned about:

- Different types of errors: syntax, runtime, and logical errors.
- Setting up the debugger in VSCode.
- Using breakpoints to pause code execution and inspect variables.
- Reading and understanding error outputs.

Understanding these concepts is essential for becoming a proficient programmer and writing reliable code.


# Step 10: OOP - Introduction to Classes and Objects

Welcome to Step 10, where we take a significant conceptual leap into **Object-Oriented Programming (OOP)**. So far, you've been learning how to write Python code using variables, functions, loops, and control structures. Now, we will explore a new way of organizing and structuring your code: by using **classes** and **objects**.

## What is Object-Oriented Programming (OOP)?

Object-Oriented Programming (OOP) is a programming paradigm (a style or way of programming) based on the concept of "objects." An **object** is an instance of a **class**, and a class defines the blueprint for that object.

OOP focuses on using **objects** that have both **data** (also called attributes) and **behaviors** (also called methods). This is different from procedural programming, where you write sequences of instructions for the computer to follow.

!!! Tip "What is an instance?"
    An instance is an individual object created from a class. When you define a class, you're creating a blueprint, but when you create an instance, you're making an actual object based on that blueprint.

    Instancing also happens when you define a variable, or a function. So when you assign a namespace to a class, you're creating an instance of that class.


### Why OOP?

OOP allows us to:

- **Model real-world entities**: You can represent things like students, books, or even psychology experiments as objects in your code.
- **Organize and reuse code**: Classes let us write modular and reusable code. Once you write a class, you can create multiple objects from it, each with its own unique data.
- **Structure complex systems**: As projects grow larger, OOP makes it easier to manage and structure the code.

## The Key Concepts of OOP

There are four fundamental concepts in OOP:

1. **Classes**: A blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
2. **Objects**: An instance of a class. Each object can have its own data (attributes) and can perform actions (methods).
3. **Attributes**: Data stored in an object. Think of these as characteristics of the object.
4. **Methods**: Functions that belong to a class. These are actions the object can perform.

!!! Tip "Louder for the people in the back, what are Methods?"
    It's written above - but methods are simply class specific functions. This is useful because you might want functions that reference attributes of the class. There will be demonstrations of this later on.

## Classes and Objects in Python

In Python, you define a class using the `class` keyword, and you create objects from that class by calling it like a function. Let’s take a look at an example:

### Defining a Class and Creating an Object

```python
# Defining a simple class called 'Person'
class Person:
    # Constructor method (__init__) to initialize attributes
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age  # Attribute

    # Method to display information about the person
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Creating an object of the Person class
person1 = Person("Alice", 30)

# Using the object’s method
person1.introduce()
```

### What’s Happening in the Code?

- **class Person**: This defines a new class called `Person`.
- **\_\_init\_\_ method**: This is a special method (also called a **constructor**) that runs when a new object is created. It initializes the object’s attributes (`name` and `age`).
- **self**: Refers to the current instance of the class. It allows the object to reference its own attributes and methods.
- **person1 = Person("Alice", 30)**: This creates an object (an **instance**) of the `Person` class with the name "Alice" and age 30.
- **person1.introduce()**: Calls the method `introduce()` on the `person1` object, which prints out a message.

## Key Concepts in OOP: Attributes and Methods

### Attributes

Attributes are variables that belong to an object. They hold information about the object, and each object can have different values for its attributes.

In the previous example, `name` and `age` are attributes of the `Person` class.

### Methods

Methods are functions that belong to an object. They define the behaviors of the object. For example, the `introduce` method is a behavior of the `Person` class, which allows the object to introduce itself.

## Let’s Build More Complex Classes

### Adding More Attributes and Methods

Let’s create a class that represents a **Car**, with attributes for its **brand**, **model**, and **year**, and methods to **start** and **stop** the car.

```python
# Defining a Car class
class Car:
    # Constructor method to initialize attributes
    def __init__(self, brand, model, year):
        self.brand = brand  # Attribute
        self.model = model  # Attribute
        self.year = year  # Attribute
        self.is_running = False  # Attribute to track if the car is running

    # Method to start the car
    def start(self):
        self.is_running = True
        print(f"The {self.year} {self.brand} {self.model} has started.")

    # Method to stop the car
    def stop(self):
        self.is_running = False
        print(f"The {self.year} {self.brand} {self.model} has stopped.")

# Creating an object of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Starting the car
my_car.start()

# Stopping the car
my_car.stop()
```

## Practice: Create Your Own Class

Now it’s your turn! Create a class to represent something from your daily life. It could be a **Book**, **Laptop**, or even a **Pet**. Your class should have:

- At least 3 attributes
- At least 2 methods

### Example Exercise:

1. Define a class `Book` with attributes for **title**, **author**, and **year**.
2. Add methods to **display information about the book** and **check if it’s available**.

Here’s a starting point:

```python
# Your Task: Define a Book class and create objects from it

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def display_info(self):
        print(f"'{self.title}' by {self.author} ({self.year})")

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is not available.")

    def return_book(self):
        self.is_available = True
        print(f"'{self.title}' has been returned.")

# Example usage:
book1 = Book("1984", "George Orwell", 1949)
book1.display_info()
book1.check_out()
book1.return_book()
```

## Reflection: Why OOP Matters

OOP is a powerful way to write code that models real-world objects and systems. It makes your code more modular, easier to maintain, and helps you think in terms of **objects and actions** rather than just **sequences of instructions**.

As you move forward, keep practicing by identifying real-world objects you can model with classes and objects. This will help you internalize the concepts of OOP and become more comfortable with this new way of thinking about code!

## Review

- **Classes** are blueprints for creating objects.
- **Objects** are instances of classes.
- **Attributes** are characteristics of objects, while **methods** are actions that objects can perform.
- OOP helps model real-world entities and organize code more effectively.

# Step 11

Welcome back! In Step 10, we introduced the fundamental concepts of Object-Oriented Programming (OOP) with Python classes and objects. In Step 11, we will dive deeper into these concepts to solidify your understanding and practical skills in OOP.

## Review of Python Classes and Objects

### Revisiting the `__init__` Method

The `__init__` method is crucial in Python as it serves as the constructor for a class. It initializes the instance of the class with specific attributes. Let's revisit how to use `__init__` with different attributes.

```
class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
```

## Practical Exercises

### Exercise 1: Creating a Person Class

Create a `Person` class with attributes `name`, `age`, and `location`. Initialize these attributes using the `__init__` method.

### Exercise 2: Adding Methods to the Person Class

Enhance the `Person` class by adding a method `update_location` to change the person's location and a method `display_profile` to print the person's information.

??? Tip "Solution"
    ```python
    class Person:
        def __init__(self, name, age, location):
            self.name = name
            self.age = age
            self.location = location

        def update_location(self, new_location):
            self.location = new_location

        def display_profile(self):
            print(f"Name: {self.name}, Age: {self.age}, Location: {self.location}")
    ```

## Understanding and Managing Class and Instance Attributes

Let's discuss the difference between class attributes, which are shared across all instances, and instance attributes, which are unique to each instance.

### Exercise 3: Class Attribute Example

Add a class attribute `population` to the `Person` class to keep count of all person instances created.

??? Tip "Solution"
    ```python
    class Person:
        population = 0

        def __init__(self, name, age, location):
            self.name = name
            self.age = age
            self.location = location
            Person.population += 1
    ```

## Simple Methods in Classes

Instance methods are functions defined inside a class and are used to define the behaviors of an instance.

### Exercise 4: Writing an Instance Method

Write an instance method in the `Person` class that increments the person's age by one to celebrate their birthday (a `celebrate_birthday` method).

??? Tip "Solution"
    ```python
    class Person:
        def __init__(self, name, age, location):
            self.name = name
            self.age = age
            self.location = location

        def celebrate_birthday(self):
            self.age += 1
            print(f"Happy Birthday {self.name}, you are now {self.age}!")
    ```

You would call the `celebrate_birthday` method on a `Person` object to increment their age, like so:

```python
# Create a Person object
alice = Person("Candice", 25, "Cincinnati Ohio")

# Celebrate Alice's birthday
alice.celebrate_birthday()
```

## Introduction to Simple Exception Handling within Methods

Proper error handling is essential to prevent and manage exceptions in Python programs effectively.

You can handle errors using the `try` and `except` blocks to catch exceptions and provide appropriate responses.

Example in a "toy" function:

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The result of the division is: {result}")
```

`try` and `except` blocks are used to catch exceptions. If an exception occurs within the `try` block, the code within the `except` block is executed. Implementing exception handling in class methods is similar to the example above, and we'll practice that in the exercise below.

### Exercise 5: Exception Handling in Method

Implement a method in the `Person` class to set the person's age, which handles exceptions if a non-integer value is passed.

??? Tip "Potential Solution"
    ```python
    class Person:
        def set_age(self, age):
            try:
                self.age = int(age)
            except ValueError:
                print("Please enter a valid integer for age.")
    ```

## Class Composition

### What is Class Composition?
Class composition is a fundamental concept in Object-Oriented Programming where a class is formed using references to one or more objects of other classes in order to build more complex functionalities. This is often described as a “has-a” relationship between the composite class and the component class. For example, a `Library` has a list of `Books`.

### Why Use Class Composition?
Using class composition allows you to combine simple objects to create more complex structures. It’s a powerful method to manage complexity by breaking down problems into smaller, more manageable parts. Composition also helps in reusing code and keeping changes localized, as updating the behavior of composed objects can be done independently.

## Exercise 6: Creating a Family Class Using Composition

Now that you understand what class composition involves, let’s put this into practice. You will create a `Family` class that demonstrates class composition by including multiple `Person` objects. Think of a family as a group of people; this is the relationship you’ll model where a `Family` object will contain several `Person` objects.

### Task Description

- **Person Class**
  - Attributes: `name`, `age`
  - Methods:
    - A method to display person's details.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
```

- **Family Class**
  - Attributes: `members` (a list that will store instances of the `Person` class)
  - Methods:
    - `add_member`: Adds a new person to the family.
    - `display_family`: Shows the information of all family members.

Your task is to define the `Family` class using the `Person` class as described above. Here’s how you might start:

```python
class Family:
    def __init__(self):
        self.members = []

    def add_member(self, person):
        self.members.append(person)
        print(f"Added: {person.display_info()}")

    def display_family(self):
        print("Family Members:")
        for member in self.members:
            member.display_info()
```

### Explanation

- **Person Class**: This class represents an individual person with basic attributes like `name` and `age`.
- **Family Class**: This class uses composition by having a list of `Person` objects. It represents a family where each member is a `Person` instance. You can add members to the family and display all members' details.

This exercise will help you understand how to use class composition to structure your Python code effectively, representing real-world relationships within your programs.

## Wrap-Up and Review

We've covered a lot today! From enhancing our understanding of the `__init__` method to handling exceptions within class methods. It's crucial to get comfortable with these OOP basics as they form the foundation of more complex software development concepts.

## Reflect

Consider how these OOP principles can be applied to other programming tasks. Perhaps think about a small project where you could use classes to organize your code better.

## Further Reading and Resources

Look for online resources or books that delve deeper into Python OOP to expand your understanding and skills.

Thank you for participating in today's session. Keep practicing, and don't hesitate to reach out with any questions as you continue your journey in Python programming!

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

# Step 14

In Step 14, we will explore four of the most common data structures in Python: **Lists**, **Tuples**, **Dictionaries**, and **Sets**. These data structures are essential for organizing and storing data efficiently, and you will frequently encounter them in any kind of data analysis, especially in behavioral science research.

Let’s dive into each one and understand how to use them in Python!

---

## 1. Introduction to Python Data Structures

Python offers a variety of ways to store and organize data. Each structure has its own use cases and advantages. In this step, we will cover:

- **Lists**: Ordered, mutable collections of items.
- **Tuples**: Ordered, immutable collections of items.
- **Dictionaries**: Key-value pairs for efficient data lookup.
- **Sets**: Unordered collections of unique elements.

We’ll discuss each one in detail, provide code examples, and give you exercises to help solidify your understanding.

---

## 2. Working with Lists

### What Are Lists?

A **list** is an ordered collection of items (elements). Lists are **mutable**, which means that the elements can be changed after the list is created. You can add, remove, and modify elements in a list.

### Example: Creating and Modifying Lists

```python
# Creating a list of participants
participants = ["Alice", "Bob", "Charlie", "David"]

# Accessing elements in a list
print(participants[0])  # Output: Alice

# Modifying elements in a list
participants[1] = "Barbara"
print(participants)  # Output: ['Alice', 'Barbara', 'Charlie', 'David']

# Adding new elements to the list
participants.append("Eve")
print(participants)  # Output: ['Alice', 'Barbara', 'Charlie', 'David', 'Eve']

# Removing an element from the list
participants.remove("Charlie")
print(participants)  # Output: ['Alice', 'Barbara', 'David', 'Eve']
```

### List Methods

Here are a few useful methods you can use with lists:
- **`append()`**: Adds an element to the end of the list.
- **`remove()`**: Removes the first occurrence of an element from the list.
- **`sort()`**: Sorts the list in place.
- **`len()`**: Returns the length of the list.

### Exercise: Working with Lists
1. **Create a List**: Create a list of 5 favorite hobbies.
2. **Modify the List**: Add a new hobby to the list, then remove the second hobby from the list.
3. **Print and Sort**: Print the final list and sort it alphabetically.

---

## 3. Working with Tuples

### What Are Tuples?

A **tuple** is similar to a list, but it is **immutable**, meaning that once a tuple is created, its elements cannot be changed. Tuples are useful when you want to store a collection of items that should not be modified.

### Example: Creating and Accessing Tuples

```python
# Creating a tuple
coordinates = (10, 20)

# Accessing elements in a tuple
print(coordinates[0])  # Output: 10

# Tuples are immutable, so you cannot modify them
# The following line would raise an error:
# coordinates[0] = 15  # Uncommenting this will raise a TypeError

# You can create a tuple with a single element by adding a comma at the end
single_element_tuple = (42,)
print(single_element_tuple)  # Output: (42,)
```

!!! Tip "Tuple Syntax"
    Notice that Tuples are created using parentheses `()` and elements are separated by commas, where as Lists are created using square brackets `[]`. This distinction is important to remember when working with these data structures!

### When to Use Tuples

- Use a **tuple** when you have a collection of items that should not change.
- Tuples are often used to represent fixed collections, such as geographical coordinates or RGB color values.

### Exercise: Working with Tuples
1. **Create a Tuple**: Create a tuple that contains your birthdate (day, month, year).
2. **Access Elements**: Print the day, month, and year individually by accessing the tuple elements.
3. **Experiment**: Try modifying the tuple (and note why it doesn’t work).

---

## 4. Working with Dictionaries

### What Are Dictionaries?

A **dictionary** is a collection of **key-value pairs**. Each key is associated with a value, and you can use the key to quickly access the corresponding value. Dictionaries are **mutable**, so you can change the values associated with keys after the dictionary is created.

### Example: Creating and Using Dictionaries

```python
# Creating a dictionary to store survey responses
survey_responses = {
    "Alice": 5,
    "Bob": 7,
    "Charlie": 6
}

# Accessing a value by its key
print(survey_responses["Bob"])  # Output: 7

# Modifying a value
survey_responses["Bob"] = 8
print(survey_responses)  # Output: {'Alice': 5, 'Bob': 8, 'Charlie': 6}

# Adding a new key-value pair
survey_responses["David"] = 9
print(survey_responses)  # Output: {'Alice': 5, 'Bob': 8, 'Charlie': 6, 'David': 9}

# Removing a key-value pair
del survey_responses["Charlie"]
print(survey_responses)  # Output: {'Alice': 5, 'Bob': 8, 'David': 9}
```

### Dictionary Methods

- **`keys()`**: Returns a list of all keys in the dictionary.
- **`values()`**: Returns a list of all values in the dictionary.
- **`items()`**: Returns a list of key-value pairs (tuples).

#### Example: Using Dictionary Methods

```python
# Getting all keys in the dictionary
print(survey_responses.keys())  # Output: dict_keys(['Alice', 'Bob', 'David'])

# Getting all values in the dictionary
print(survey_responses.values())  # Output: dict_values([5, 8, 9])

# Getting key-value pairs as tuples
print(survey_responses.items())  # Output: dict_items([('Alice', 5), ('Bob', 8), ('David', 9)])
```

### Exercise: Working with Dictionaries
1. **Create a Dictionary**: Create a dictionary with the names of three friends and their favorite colors.
2. **Modify the Dictionary**: Change one friend's favorite color and add a new friend with their favorite color.
> Hint, use the [`update()` method (this is a clickable link)](https://www.w3schools.com/python/ref_dictionary_update.asp) to add a new key-value pair to the dictionary as well as to update an existing key-value pair.
3. **Print and Access**: Print the dictionary and access the favorite color of one of your friends.

---

## 5. Working with Sets

### What Are Sets?

A **set** is an unordered collection of **unique elements**. Sets are useful when you want to store items without duplicates and don't care about the order of the elements. Sets are **mutable**, but you cannot access elements by index like in lists.

> Online resource for sets can be found [here](https://www.w3schools.com/python/python_sets.asp)

### Example: Creating and Using Sets

```python
# Creating a set of participants
participants = {"Alice", "Bob", "Charlie", "David"}

# Adding a new element to the set
participants.add("Eve")
print(participants)  # Output: {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}

# Trying to add a duplicate element (it will have no effect)
participants.add("Alice")
print(participants)  # Output: {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}

# Removing an element from the set
participants.remove("David")
print(participants)  # Output: {'Alice', 'Bob', 'Charlie', 'Eve'}
```

### Set Operations

- **`add()`**: Adds an element to the set.
- **`remove()`**: Removes an element from the set.
- **`union()`**: Returns a new set containing all elements from two sets (without duplicates).
- **`intersection()`**: Returns a new set containing only elements found in both sets.

### Exercise: Working with Sets
1. **Create a Set**: Create a set of favorite fruits.
2. **Add Elements**: Add a new fruit to the set and attempt to add a duplicate fruit.
3. **Perform Set Operations**: Create a second set of fruits and find the **union** and **intersection** of the two sets.

---

## 6. Final Exercise: Working with Data Structures

Now that you’ve learned about lists, tuples, dictionaries, and sets, let's wrap up with a final exercise that brings these concepts together.

### Instructions:

1. **Create a Class System for Participants**:
    - Create a `Participant` class that stores the name, age, and favorite hobby of each participant.
    - Use a **list** to store a collection of `Participant` objects.

2. **Store Data in a Dictionary**:
    - Create a dictionary where the keys are participant names and the values are tuples containing their age and favorite hobby.

3. **Use a Set for Unique Hobbies**:
    - Extract all unique hobbies from the participants and store them in a **set**.

4. **Final Output**:
    - Print the list of participants.
    - Print the dictionary mapping names to participant details.
    - Print the set of unique hobbies.

!!! Tip "Practice for your Written Assessment"
    To practice for the written assessment, outline how you would solve this problem before you start your implementation. You can write out your solution on a piece of paper or in your text editor of choice (Google/Word Doc, etc.). Be as detailed as you can manage. Once you're done with this, then use your outline to implement the solution - how close were you? What did you forget? Answering these questions will help you prepare for the written assessment!

??? Tip "Potential Solution"

    ```python
    class Participant:
        def __init__(self, name, age, hobby):
            self.name = name
            self.age = age
            self.hobby = hobby

    # List to store participants
    participants = [
        Participant("Alice", 29, "Reading"),
        Participant("Bob", 34, "Cycling"),
        Participant("Charlie", 27, "Reading"),
        Participant("David", 31, "Swimming")
    ]

    # Dictionary to map participant names to their age and hobby
    participant_dict = {p.name: (p.age, p.hobby) for p in participants}
    print(participant_dict)
    ```

    ```python
    # Set to store unique hobbies
    unique_hobbies = {p.hobby for p in participants}
    print(unique_hobbies)
    
    #Expected Output:
    # {'Reading', 'Cycling', 'Swimming'}
    ```
    
---

## 7. Reflect and Review

In this step, we covered four essential Python data structures:

- **Lists**: Ordered, mutable collections of items, which are ideal for managing an ordered set of data that might need to be modified.
- **Tuples**: Ordered but immutable collections, useful for fixed data that should not be changed once defined.
- **Dictionaries**: Unordered collections of key-value pairs, which are excellent for mapping relationships, such as names to data.
- **Sets**: Unordered collections of unique items, great for ensuring no duplicates and for performing mathematical set operations such as unions and intersections.

### Why Are These Data Structures Important?

These data structures help organize, store, and access data efficiently in Python programs, especially in scenarios where datasets are large or need to be processed in various ways. Understanding the strengths and limitations of each type of data structure is crucial for writing effective and optimized Python code.

Think about how you might apply these structures in real-world projects:

- **Lists** for managing ordered collections like participant data or survey responses.
- **Tuples** for grouping related but unchangeable data, like coordinates or fixed settings.
- **Dictionaries** for looking up information quickly, such as mapping survey participants to their answers.
- **Sets** for managing collections where uniqueness is required, such as lists of unique hobbies or tags.

Having a strong grasp of Python’s core data structures will help you organize and manipulate data more effectively in future projects.

---

# Step 15

In Step 14, we introduced the four most common data structures in Python: **Lists**, **Tuples**, **Dictionaries**, and **Sets**. Now that you have a basic understanding of these structures, it's time to practice manipulating them. Data manipulation is essential in research and real-world projects, as it allows you to prepare, clean, and transform data for analysis.

### 1. Working with Lists

Lists are mutable, meaning you can change their elements after they've been created. Let’s explore some ways to manipulate lists.

#### Adding Elements

You can add new elements to a list using the `append()` and `insert()` methods.

```python
# Example: Append vs Insert
my_list = [1, 2, 3]
my_list.append(4)  # Adds 4 to the end
my_list.insert(1, "inserted")  # Inserts at index 1

print(my_list)
```

- **`append()`** adds the element to the **end** of the list.
- **`insert()`** allows you to add an element at a specific position in the list. The first argument is the **index** where you want to insert the element.

#### Removing Elements

To remove elements, you can use the `remove()` method or the `pop()` method.

- **`remove()`** deletes the first occurrence of a value.
- **`pop()`** removes an element by **index**, which means it removes the element at a specific position in the list, rather than searching for the value itself. Every item in a list has an index that represents its position in the list, starting with 0 for the first item.

For example, in the list `['apple', 'banana', 'cherry']`, 'apple' has index 0, 'banana' has index 1, and 'cherry' has index 2. If you use `pop(1)`, it will remove 'banana' because it's at index 1.

```python
# Example: Remove vs Pop
my_list.remove(2)  # Removes the first occurrence of 2
my_list.pop(1)  # Removes the element at index 1, which is "inserted"

print(my_list)
```

### 2. Working with Tuples

Tuples are immutable, meaning you cannot change their contents after creation. However, you can perform operations like slicing and **unpacking**.

#### Unpacking Tuples

"Unpacking" means assigning the elements of a tuple to individual variables. This allows you to break the tuple into its components and work with each one separately. For example:

```python
# Example: Tuple Unpacking
my_tuple = (10, 20, 30)
a, b, c = my_tuple  # Unpacks the values into a, b, c

print(a, b, c)
```

- In this example, the values 10, 20, and 30 are "unpacked" from the tuple and assigned to the variables `a`, `b`, and `c`. This technique is useful when you need to work with individual components of a tuple.

If the number of variables on the left doesn’t match the number of elements in the tuple, Python will raise an error.

### 3. Manipulating Dictionaries

Dictionaries allow you to store key-value pairs. You can add, update, and delete key-value pairs easily.

#### Adding and Updating Elements

You can add new key-value pairs or update existing ones by assigning a value to a key.

```python
# Example: Add and Update Dictionary
my_dict = {"name": "Alice", "age": 25}
my_dict["age"] = 26  # Update existing key
my_dict["city"] = "New York"  # Add new key-value pair

print(my_dict)
```

#### Removing Elements

To remove an element, use the `del` statement or the `pop()` method.

```python
# Example: Delete vs Pop
del my_dict["city"]  # Deletes the key-value pair for 'city'
my_dict.pop("age")  # Removes 'age' key and returns its value

print(my_dict)
```

#### Looping Through a Dictionary

You can loop through a dictionary to access its keys and values, allowing you to manipulate or analyze its data.

```python
# Example: Looping through a dictionary
my_dict = {"name": "Alice", "age": 26, "city": "New York"}

for key, value in my_dict.items():
    print(f"The key is {key} and the value is {value}")
```

- `my_dict.items()` returns each key-value pair as a tuple, and you can unpack it into `key` and `value` as shown in the example. This is useful for iterating over all the entries in a dictionary to access or modify the data.


### 4. Set Operations

Sets are unordered collections of unique elements. They support mathematical operations like **union**, **intersection**, and **difference**, which are helpful when comparing sets of data.

#### Adding and Removing Elements

```python
# Example: Add and Remove in Set
my_set = {1, 2, 3}
my_set.add(4)  # Adds 4 to the set
my_set.remove(2)  # Removes 2 from the set

print(my_set)
```

#### Set Operations: Union, Intersection, Difference

- **Union** combines all unique elements from two sets.
- **Intersection** returns only the elements that are present in both sets.
- **Difference** returns the elements that are in one set but not in the other.

```python
# Example: Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)  # Union of two sets
intersection_set = set1.intersection(set2)  # Intersection of two sets
difference_set = set1.difference(set2)  # Elements in set1 but not in set2

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
```

- **Union**: `{1, 2, 3}` and `{3, 4, 5}` together become `{1, 2, 3, 4, 5}` because all elements are included but duplicates are removed.
- **Intersection**: Only the number `3` appears in both sets, so the result is `{3}`.
- **Difference**: In the difference operation, the result is `{1, 2}` because these are the elements in `set1` that are not in `set2`.

### Exercises

1. **Create a list of your favorite fruits** and perform the following operations:
    - Add a new fruit to the end.
    - Insert a fruit at the second position.
    - Remove one fruit by its value.

    ??? Tip "Solution"
        ```python
        fruits = ["apple", "banana", "cherry"]
        fruits.append("orange")  # Add orange to the end
        fruits.insert(1, "grape")  # Insert grape at the second position
        fruits.remove("banana")  # Remove banana by value

        print(fruits)
        ```

2. **Create a dictionary** that contains the names of 3 countries and their capitals. Then:
    - Update the capital of one country.
    - Add a new country-capital pair.
    - Remove one country from the dictionary.

    ??? Tip "Solution"
        ```python
        capitals = {"France": "Paris", "Japan": "Tokyo", "USA": "Washington D.C."}
        capitals["USA"] = "Cincinnati"  # Update capital of USA
        capitals["Germany"] = "Berlin"  # Add new country-capital pair
        capitals.pop("USA")  # Remove USA from the dictionary

        print(capitals)
        ```

3. Create a tuple of 3-4 numbers. **Given a tuple of numbers**, unpack it into individual variables and print them.

    ??? Tip "Solution"
        ```python
        numbers = (100, 200, 300)
        x, y, z = numbers  # Unpack the tuple into x, y, z

        print(x, y, z)
        ```

4. **Create two sets of integers** and:
    - Perform union, intersection, and difference operations.

    ??? Tip "Solution"
        ```python
        set1 = {10, 20, 30, 40}
        set2 = {30, 40, 50, 60}

        union_set = set1.union(set2)  # Union
        intersection_set = set1.intersection(set2)  # Intersection
        difference_set = set1.difference(set2)  # Difference

        print("Union:", union_set)
        print("Intersection:", intersection_set)
        print("Difference:", difference_set)
        ```

# Step 16

## Introduction to Data Visualization

In this step, we'll start exploring **data visualization** using Python, specifically with the [`matplotlib` library](https://matplotlib.org/) and [`numpy`](https://numpy.org/) for data creation. Data visualization is an essential tool in data analysis—it allows you to better understand your data by uncovering patterns, trends, and outliers. In scientific research, visualizing data is especially valuable, helping to interpret experiment results, compare groups, and communicate findings effectively.

We'll cover a few essential plot types: **line plots**, **bar plots**, **histograms**, and **scatter plots**. These visualizations are foundational, and you’ll likely use them to analyze data in future projects.

### Getting Started: Setting Up Matplotlib and Numpy

To start, make sure you have `matplotlib` installed. If you haven’t installed it yet, you can install it by running:
```python
!pip install matplotlib
```
!!! Tip "The `!`"
    The `!` at the beginning of the command is used in Jupyter notebooks to things like installation commands - this will install matplotlib if it's not already installed.

Import `matplotlib` and `numpy` with the following aliases:
```python
import matplotlib.pyplot as plt
import numpy as np
```

### 1. Line Plot

#### Use Case
Line plots are great for visualizing changes over time or across experimental trials. Let’s start by creating a basic line plot with synthetic data.

#### Creating a Basic Line Plot
We’ll create an array of data points and visualize them:

```python
# Generate data
x = np.arange(0, 10, 1)  # x-axis: from 0 to 9
y = np.random.randint(1, 10, size=10)  # y-axis: random integers

# Create line plot
plt.plot(x, y, label="Random Data", color="blue", linestyle="--", marker="o")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Basic Line Plot")
plt.legend()
plt.show()
```

!!! Tip "Plots a as a Debugging Tool"
    Just like when you use a print statement, when you run `plt.show()`, you should see the plot appear in your notebook - this is great for instantaneous feedback.

    Think about how you can use this to debug your *data* - if you're not getting the results you expect, you can visualize your data to visually inspect it, and see if something's wrong. As scientists, we build up intuitions for the "shape" of our data, and visualizing it can help us understand what's going on.

#### Breaking it down:
- `plt.plot(x, y)`: This function creates a line plot with `x` on the x-axis and `y` on the y-axis.
- `plt.xlabel()`: Sets the label for the x-axis.
- `plt.ylabel()`: Sets the label for the y-axis.
- `plt.title()`: Sets the title of the plot.
- `plt.legend()`: Displays the legend on the plot.
- `plt.show()`: Displays the plot.

You can check out the `plot` documentation for matplotlib [here](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html).

#### Customizing the Line Plot
Try adjusting colors, line styles, and adding markers to make the plot more informative.

[Here is a web link to the named colors of matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html), it can be a lot of fun and very useful to experiment with different colors.

!!! Tip "Colors from Hex Codes"
    You can also use hex codes to specify colors in matplotlib. For example, `color="#FF5733"` would give you a specific shade of orange.

    Something that I personally love to do to find unique combinations of hex code colors is to use PokePalettes, a website that generates color palettes based on Pokemon. [Check it out here!](https://pokepalettes.com/)

    To replace a color in a plot with a hex code, you can use the following syntax:
    ```python
    plt.plot(x, y, color="#FF5733")
    ```

### 2. Bar Plot

#### Use Case
Bar plots are useful for comparing categorical data, like response counts across different participant groups.

#### Creating a Basic Bar Plot
Here, we’ll create a bar plot with categorical labels on the x-axis:

```python
# Data
categories = ["Group A", "Group B", "Group C"]
values = [15, 35, 25]

# Create bar plot
plt.bar(categories, values, color="green")
plt.xlabel("Groups")
plt.ylabel("Values")
plt.title("Bar Plot of Categorical Data")
plt.show()
```

You can see the `bar` documentation for matplotlib [here](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html).

#### Customizing the Bar Plot
Experiment with changing colors, adjusting bar width, and adding values on top of each bar to emphasize comparisons.

!!! Tip "Fun Example"
    You can change the way the bars are displayed, their orientation, and other properties. For example, you can create a horizontal bar plot by using `plt.barh()` instead of `plt.bar()`.

    ```python
    plt.barh(categories, values, color="green")
    ```

### 3. Histogram

#### Use Case
Histograms are ideal for visualizing the distribution of a dataset, such as reaction times or score distributions.

#### Creating a Basic Histogram
Using Numpy, we’ll generate a normal distribution and plot it as a histogram.

```python
# Generate data with a normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)

# Create histogram
plt.hist(data, bins=30, color="purple", edgecolor="black")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Normally Distributed Data")
plt.show()
```

#### Importance of Bin Size
Histograms are great data visualization tools, but it's important to understand how the bin size can be adjusted to change the level of detail in the plot, sometimes altering the interpretation of the data.

You can adjust the number of bins by changing the `bins` parameter in the `hist()` function. Functionally, the number of bins determines the number of intervals (or groups) the data is divided into, the more bins, the more detailed the histogram.

### Customizing the Histogram
Experiment with changing colors, adjusting the number of bins, and adding labels to make the histogram more informative.

### 4. Scatter Plot

#### Use Case
Scatter plots are useful for showing relationships between two continuous variables, like age and reaction time.

#### Creating a Basic Scatter Plot
Here, we’ll create two correlated datasets and plot them against each other.

```python
# Generate data
x = np.random.rand(100)
y = x * 2 + np.random.normal(0, 0.1, 100)

# Create scatter plot
plt.scatter(x, y, color="red", s=20, label="Data Points")
plt.xlabel("X Variable")
plt.ylabel("Y Variable")
plt.title("Scatter Plot Example")
plt.legend()
plt.show()
```

#### Customizing the Scatter Plot
Change point size, colors, and add legends to enhance interpretability.

!!! Tip "Fun Example"
    You can change the shape of the markers in a scatter plot. For example, you can use triangles instead of circles by specifying `marker="^"`.

    ```python
    plt.scatter(x, y, color="red", s=20, label="Data Points", marker="^")
    ```

    This is particularly useful when you have multiple datasets on the same plot and want to differentiate them.

### 5. Combining Multiple Plots in a Single Figure

#### Use Case
Sometimes, it’s useful to compare multiple visualizations side-by-side. Using subplots, you can arrange multiple plots in one figure.

#### Creating Subplots
Below is an example of creating a line plot and a histogram in a 1x2 grid layout.

```python
# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Scatter Plot
axes[0].scatter(x, y, color="blue", label="Scatter Plot")
axes[0].set_title("Scatter Plot")
axes[0].set_xlabel("X-axis")
axes[0].set_ylabel("Y-axis")
axes[0].legend()

# Histogram
axes[1].hist(data, bins=20, color="orange", edgecolor="black")
axes[1].set_title("Histogram")
axes[1].set_xlabel("Value")
axes[1].set_ylabel("Frequency")

# Adjust layout
plt.tight_layout()
plt.show()
```

Notice how `axes[0]` and `axes[1]` are used to access the individual subplots. This allows you to customize each subplot independently.

## A quick note on the importance of clear labels

When creating visualizations, it's crucial to provide clear labels for the axes, titles, and legends. These labels help viewers understand the data being presented and the context of the visualization. Always ensure that your visualizations are labeled appropriately to convey the intended message effectively.

Your goal should be for the plot to make sense independent of the context; such that if you were to show a data visualization depicting the relationship between age and reaction time, someone who had never seen the data before could understand what the plot is showing by reading the labels, axes, and title.

## Coding Exercise: Custom Visualizations

In this exercise, you’ll work with a dataset generated using `numpy`. Your goal is to explore different ways to visualize this data and think about what insights each visualization type can reveal. You’ll create at least **two different visualizations** of the dataset, using different plot types.

### A. Generate the Data

Run the code below to generate a synthetic (fake) dataset. This dataset simulates reaction times and accuracy scores from a fictional psychology experiment with 200 participants.

```python
import numpy as np

# Setting random seed for reproducibility
np.random.seed(42)

# Generate participant IDs (1 through 200)
participant_ids = np.arange(1, 201)

# Generate random reaction times (in milliseconds) with a mean of 500 ms and std deviation of 50 ms
reaction_times = np.random.normal(loc=500, scale=50, size=200)

# Generate random accuracy scores (out of 100) with a mean of 75 and std deviation of 10
accuracy_scores = np.random.normal(loc=75, scale=10, size=200)

# Print first few values for each array
print("Participant IDs:", participant_ids[:5])
print("Reaction Times:", reaction_times[:5])
print("Accuracy Scores:", accuracy_scores[:5])
```

### B. Review your data visualization options

1. **Line Plot**: Consider visualizing reaction times across participants to see how response times vary.
2. **Histogram**: A histogram of reaction times or accuracy scores can help show the distribution of these values.
3. **Scatter Plot**: A scatter plot of accuracy vs. reaction time can show any correlation between speed and accuracy.
4. **Bar Plot**: You could create a bar plot of average reaction times or accuracy for groups of participants (e.g., participants 1–50, 51–100).

### C. Create Your Visualizations

Using `matplotlib`, create at least **two different visualizations** of the data. Use the examples above or come up with your own! Think about:
- What insights does each plot type reveal?
- How can you customize your plots to make them more informative?

??? Tip "Example Starter Code"
    Below is an example of how you might start with a histogram. Remember to create your own additional plot(s) and customize as needed!

    ```python
    import matplotlib.pyplot as plt

    # Example Histogram for Reaction Times
    plt.hist(reaction_times, bins=20, color="skyblue", edgecolor="black")
    plt.xlabel("Reaction Time (ms)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Reaction Times")
    plt.show()

    # Continue with your own visualizations!
    ```

### D. Reflect

After creating your visualizations, reflect on the following:
- What insights did each visualization reveal about the data?
- Which visualization do you think was most effective, and​⬤

## Review

In this step, you learned:
- How to create and customize **line plots**, **bar plots**, **histograms**, and **scatter plots**.
- Basic customization techniques to make plots more readable and informative.
- How to use **subplots** to compare multiple visualizations side-by-side.

Data visualization is a powerful skill that will help you analyze and interpret data effectively in your research and academic work.

# Step 17

## Interactive Data Visualization with ipywidgets

In this step, we’ll enhance our data visualizations by adding **interactivity** using the `ipywidgets` library. `ipywidgets` allows us to add interactive controls, such as sliders and dropdowns, that let you modify visualization parameters in real-time.

### Why Use ipywidgets?

Interactive visualizations are especially useful for exploring data dynamically. Rather than generating a new plot for every change, you can use widgets to modify aspects of the plot—like adjusting data ranges, selecting data subsets, or changing visual elements—right from the notebook.

!!! Tip "Note - only for Notebooks!"
    `ipywidgets` is designed for use in Jupyter notebooks like Google Colab and VSCode. If you want to develop interactive visualizations for web applications, you might consider using libraries `Plotly`.

### Getting Started with ipywidgets

To start, make sure `ipywidgets` is installed. You can install it by running:
```python
!pip install ipywidgets
```

Then, import the widgets and display functionality:
```python
import ipywidgets as widgets
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np
```

### 1. Basic Interactive Plot with a Slider

To introduce `ipywidgets`, let’s create an interactive line plot using a slider. This slider will control the number of data points displayed in the plot.

#### Creating Interactive Line Plot

We’ll generate data with `numpy` and then use the `interact` function to link a slider to the number of data points.

```python
# Generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Define plot function
def plot_sine(num_points):
    plt.plot(x[:num_points], y[:num_points], color="blue")
    plt.xlabel("X-axis")
    plt.ylabel("Sine of X")
    plt.title(f"Sine Wave with {num_points} Points")
    plt.show()

# Create slider with interact
interact(plot_sine, 
         num_points=widgets.IntSlider(min=10, 
                                      max=100, 
                                      step=10, 
                                      value=50))
```

#### Explanation
The `plot_sine` function generates the plot, and the `interact` function links the `num_points` argument to the slider widget. Now, try moving the slider to see how it affects the plot!

### 2. Creating Interactive Scatter Plots with Dropdowns

Next, we’ll add more complexity by allowing users to choose between different datasets. For example, this could be useful for comparing the relationship between different experimental variables.

#### Generate Sample Data

We’ll create two sets of data for our scatter plot: a **linear** relationship and a **quadratic** relationship.

```python
# Sample data for two relationships
x_data = np.linspace(0, 10, 100)
linear_y = 2 * x_data + np.random.normal(0, 1, 100)  # Linear relationship
quadratic_y = x_data**2 + np.random.normal(0, 5, 100)  # Quadratic relationship

# Define plot function
def plot_scatter(relation_type):
    plt.scatter(x_data, linear_y if relation_type == "Linear" else quadratic_y, color="red", s=20)
    plt.xlabel("X Variable")
    plt.ylabel("Y Variable")
    plt.title(f"{relation_type} Relationship")
    plt.show()

# Create dropdown with interact
interact(plot_scatter, relation_type=widgets.Dropdown(options=["Linear", "Quadratic"], value="Linear", description="Relationship Type"))
```

#### Explanation
The `plot_scatter` function adjusts the `y` values depending on the chosen relationship type. The dropdown menu lets users choose between the linear and quadratic datasets, updating the plot accordingly.

### 3. Combining Multiple Widgets: Slider and Dropdown

Now, let’s create an interactive histogram where users can:
- Adjust the number of bins with a slider.
- Select the dataset to visualize with a dropdown.

#### Creating Data and Function

We’ll generate two datasets: one with a **normal distribution** and one with a **uniform distribution**.

```python
# Sample datasets
normal_data = np.random.normal(0, 1, 1000)
uniform_data = np.random.uniform(-3, 3, 1000)

# Define histogram plot function
def plot_histogram(dist_type, bins):
    data = normal_data if dist_type == "Normal" else uniform_data
    plt.hist(data, bins=bins, color="green", edgecolor="black")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title(f"{dist_type} Distribution with {bins} Bins")
    plt.show()

# Create interactive widgets
interact(plot_histogram, 
         dist_type=widgets.Dropdown(options=["Normal", "Uniform"], value="Normal", description="Distribution"),
         bins=widgets.IntSlider(min=5, max=50, step=5, value=20))
```

#### Explanation
This function combines a dropdown (for dataset selection) and a slider (for number of bins) to create a more interactive histogram, allowing users to explore both distribution shapes and bin adjustments.

### Reflect and Practice

After experimenting with the examples above, create your own interactive visualization:

1. **Choose a dataset**: Use `numpy` to generate a dataset (or modify one of the provided datasets, you can even use the data from `Step 16`).
2. **Select a widget**: Decide which widget(s) would be useful to control the data or visualization.
3. **Customize**: Modify the appearance or functionality to make the visualization more insightful.

### Review

In this step, you learned:
- How to create interactive plots using `ipywidgets`.
- Basic widgets, like sliders and dropdowns, to control plot parameters.
- How to combine multiple widgets to create rich, interactive visualizations.

Adding interactivity to data visualization lets you explore data more deeply, helping you to uncover trends and patterns more easily. You can apply these techniques to create interactive visualizations for research and data exploration, making it easier to gain insights from your data.

# Step 18: Conducting Experiments Online and Basic Web Development

Up until this point, our course has focused on learning Python. While Python absolutely could be used to build an online research study, as we will see in this Step of the learning path, there are tools better suited to conducting online research.

In this step, we will explore how behavioral science experiments can be conducted on the web. We’ll look at a few web technologies that make this possible, such as `jsPsych`, HTML, CSS, and JavaScript, and provide you with code examples you can try out. We will also introduce tools that allow for online research without requiring any coding (Google Forms).

> Note: This step is meant to conceptually introduce you to a different programming language, specifically JavaScript and web development lanugages (HTML and CSS). We will take a slightly deeper dive into JavaScript in Step 20 when we look at `jsPsych`!

---

## 1. Experiments on the Web

Conducting experiments online allows researchers to reach a broader audience and collect data efficiently. While programming tools like `PsychoPy` (Python) can be used to design experiments, another accessible tool, **`jsPsych`**, simplifies the process of running experiments directly in a web browser.

### What is `jsPsych`?

`jsPsych` is a JavaScript library specifically designed for creating experiments that participants can complete online. It’s flexible, widely used in psychology research, and makes it easier to control and collect data from web-based studies.

### What is JavaScript?

**JavaScript** is a programming language used to create interactive elements on web pages. It’s essential for building dynamic websites and web applications. JavaScript can handle user interactions, animations, and data processing in real-time. 

Have you ever noticed a button change color on a website, or text appear when you hover over an image? These are examples of JavaScript in action!

JavaScript is incredibly versitile for all things on the web, and can be used to create interactive elements, animations, and more. One of my favorite uses of JavaScript is called "ThreeJS" which is a library that allows you to create 3D graphics in the browser! You can check out some examples [here](https://threejs.org/).

---

## 2. Basics of Web Development: HTML, CSS, and JavaScript

To understand how `jsPsych` functions, we’ll cover some core components of web development. Below, we’ll explore HTML, CSS, and JavaScript and provide examples you can try in **VSCode**.

??? Tip "Web Development?"
    Web development can be defined as the process of building websites and web applications. It involves writing code in languages like HTML, CSS, and JavaScript to create interactive and visually appealing web pages. These technologies work together to structure content, style elements, and add interactivity to web pages.

### 2.1. Install Live Server in VSCode

   In the Extensions sidebar, search for **Live Server** and install it. We'll use this extension to run our HTML files in a live server.

---

### 2.2. HTML (HyperText Markup Language)

HTML is the standard language for creating web pages. It allows you to structure content using "tags." A "tag" is a keyword surrounded by angle brackets, like `<tag>`. Tags are used to define elements such as headings, paragraphs, images, and links. A sample of a common tag is `<h1>`, which defines a top-level heading. To close a tag, use a forward slash, like `</h1>`.


Here’s a basic HTML structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Experiment</title>
</head>
<body>
    <h1>Welcome to My Experiment!</h1>
    <p>This is an experiment example using HTML, CSS, and JavaScript.</p>
</body>
</html>
```

> Notice the tags like `<html>`, `<head>`, `<title>`, `<body>`, `<h1>`, and `<p>`. These tags structure the content and define the appearance of the webpage. `<h1>` is a top-level heading, and `<p>` is a paragraph.

This code creates a basic webpage with a title and heading. Copy and paste this code into a new file with an `.html` extension, calling the file `index.html`.

You can open this file in VSCode and use the **Live Server** extension to view it in your browser. To do so, right-click on the HTML file and select **Open with Live Server**.

This will open up a new tab in your browser displaying the HTML content!

---

### 2.3. CSS (Cascading Style Sheets)

CSS styles your HTML content, making it look visually appealing. You can add color, align elements, and much more.

Add the following CSS to your HTML file within a `<style>` tag in the `<head>` section:

```html
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f8ff;
        text-align: center;
    }
    h1 {
        color: #4682b4;
    }
    p {
        color: #2f4f4f;
    }
</style>
```

??? Tip "The full HTML file should now look like this:"
    ```html
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Web Experiment</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                text-align: center;
            }
            h1 {
                color: #4682b4;
            }
            p {
                color: #2f4f4f;
            }
        </style>
        
    </head>
    <body>
        <h1>Welcome to My Experiment!</h1>
        <p>This is an experiment example using HTML, CSS, and JavaScript.</p>
    </body>

    </html>
    ```

This CSS changes the background color, centers the text, and applies colors to the heading and paragraph.

---

### 2.4. JavaScript

JavaScript adds interactivity to your webpage, such as reacting to user inputs or displaying alerts.

Include this script inside your HTML file’s `<body>` or `<head>` tags:

```html
<script>
    function showAlert() {
        alert("Welcome to the experiment!");
    }
</script>

<button onclick="showAlert()">Click Me</button>
```

This code adds a button that, when clicked, shows an alert message.


??? Tip "Your full HTML file should now look like this:"
    ```html
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Web Experiment</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                text-align: center;
            }
            h1 {
                color: #4682b4;
            }
            p {
                color: #2f4f4f;
            }
        </style>

        <script>
            function showAlert() {
                alert("Welcome to the experiment!");
            }
        </script>

        <button onclick="showAlert()">Click Me</button>


    </head>
    <body>
        <h1>Welcome to My Experiment!</h1>
        <p>This is an experiment example using HTML, CSS, and JavaScript.</p>
    </body>

    </html>
    ```

---

## 3. Play with Web Development Tools

Now that you've seen the basics of HTML, CSS, and JavaScript, let’s practice combining them to create a simple interactive page.

*Try out the coding exercise below to experiment with web development tools.*

#### 3.1 **Create an HTML file** in VSCode and add the following code:
  
   - This code has HTML, CSS, and JavaScript sections, all within the same file.
   - Run the code using **Live Server** to see the results immediately in your browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Web Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f3f3f3;
            text-align: center;
        }
        h1 {
            color: #4CAF50;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Play with Web Development!</h1>
    <p>Click the button to see a message.</p>
    <button onclick="displayMessage()">Click Me!</button>
    <p id="message"></p>

    <script>
        function displayMessage() {
            document.getElementById("message").innerHTML = "Hello, you're interacting with JavaScript!";
        }
    </script>
</body>
</html>
```


#### 3.2 **Experiment** by changing the following elements:

   - **CSS Colors**: Adjust colors in the CSS styles for `h1`, `body`, or `button`.
   - **Message Text**: Modify the message text in the JavaScript function `displayMessage()`.

This gives you a chance to experiment with the main elements of web development in one file. By changing CSS properties, HTML structure, and JavaScript functions, you’ll start to see how these tools work together.

!!! Tip "`jsPsych` in Step 20"
    When we get to Step 20, we'll take a look of `jsPsych` - but this is a good enough intro for now!

---

## 4. Using Non-Programming Tools for Online Research

For researchers who prefer not to code, tools like **Google Forms** are useful for creating and distributing online surveys. These tools are widely used in psychological and behavioral research to gather self-report data or feedback from participants.

### Designing Effective User Surveys

A **user survey** is a structured way of gathering data about participants' thoughts, behaviors, or experiences. Well-designed surveys can reveal valuable insights into how people feel or think about a topic.

To learn more about designing surveys, visit [How to Design a UX Research Survey](https://dscout.com/people-nerds/how-to-design-a-ux-research-survey), which covers practical tips and best practices for creating effective surveys.

---

## Summary

- **HTML, CSS, and JavaScript** allow us to create and style web-based experiments.
- **Playing with web development tools** helps you learn through hands-on practice, experimenting with colors, structure, and interactivity.
- **Google Forms** and other no-code tools provide options for collecting data without needing to write code.
- **Survey design** is crucial in psychology and UX research to capture reliable and meaningful data from participants.

This step gives you the tools to start exploring web-based research and consider how online experiments can expand your reach and capabilities in behavioral science research.


# Step 19

In this step, we’ll explore **Pandas**, a powerful Python library for data manipulation and analysis. Pandas provides tools to explore, manipulate, and analyze datasets efficiently, which is essential for behavioral scientists working with real-world data.

We’ll use a CSV file named `happiness correlation data-2.csv`, which you can download below. Each row represents data from one participant, with columns capturing various aspects like age, work hours, GPA, life satisfaction, and more.

## 0. Download the Dataset

[Click this link to donload the data](<files/happiness correlation data-2.csv>)

!!! Tip "Familiar?"
    This data was pulled from Stats 2002, a course at UC. If this data is familiar, it's probably because you've seen this before!

**IMPORTANT**: Make sure to place the downloaded CSV file in the same directory as your notebook or script!

## 1. Getting Started with Pandas

### Installing and Importing Pandas
To use Pandas, ensure it’s installed in your Python environment. You can install it by running:

```python
!pip install pandas
```

!!! Tip "`%pip install`"
    If the code above doesn't work, try using `%pip install` instead of `!pip install`.

Then, import Pandas at the beginning of your notebook or script:

```python
import pandas as pd
```

### Loading the Data
Load the CSV file into a DataFrame, which is Pandas’ primary data structure for handling data tables.

```python
# Load the data from the your directory
file_path = 'happiness correlation data-2.csv'
df = pd.read_csv(file_path)
```

### Viewing the Data
Use `head()` to see the first few rows and get a feel for the structure.

```python
df.head()
```

---

## 2. Exploring the Dataset

This dataset has columns capturing the following participant information:

- **age**: Participant's age
- **hours_work_week**: Hours worked per week
- **gpa**: Participant's GPA
- **life_satisfaction**: Self-reported life satisfaction score
- **desire_to_achieve**: Self-reported desire to achieve
- **number_drinks**: Number of alcoholic drinks consumed per week
- **stress**: Self-reported stress level

### Basic Data Information

To get a quick summary of the dataset, including column names, data types, and any missing values:

```python
df.info()
```

To get basic descriptive statistics (mean, median, etc.) for each column:

```python
df.describe()
```

---

## 3. Analyzing Specific Columns

### Calculating the Mean Age of Participants
Let’s calculate the average age of participants.

```python
mean_age = df['age'].mean()
print("Average Age:", mean_age)
```

### Distribution of Life Satisfaction Scores
To understand the distribution of `life_satisfaction` scores, we can use Pandas to plot a histogram (requires `matplotlib` library).

```python
import matplotlib.pyplot as plt

df['life_satisfaction'].plot(kind='hist', title='Life Satisfaction Distribution')
plt.xlabel('Life Satisfaction')
plt.show()
```

### Exploring Correlations
We may want to see how different variables relate to each other. For example, are work hours correlated with stress?

```python
correlation = df[['hours_work_week', 'stress']].corr()
print("Correlation between hours worked and stress:\n", correlation)
```

### Grouping Data
We can group data to find insights, such as average Stress level by different levels of `desire_to_achieve`.

```python
avg_stress_by_achievement = df.groupby('desire_to_achieve')['stress'].mean()
print("Stress by Desire to Achieve:\n", avg_stress_by_achievement)
```

---

## 4. Data Cleaning and Manipulation

### Calculating Letter Grades
Add a new column to the dataset that calculates the letter grade for each student's GPA:

```python
def calculate_letter_grade(gpa):
    if gpa >= 3.7:
        return 'A'
    elif gpa >= 3.0:
        return 'B'
    elif gpa >= 2.0:
        return 'C'
    elif gpa >= 1.0:
        return 'D'
    else:
        return 'F'

df['letter_grade'] = df['gpa'].apply(calculate_letter_grade)
```

### Create a Bar Graph of Letter Grades 

To visualize the distribution of letter grades, we can create a bar graph:

```python
grade_counts = df['letter_grade'].value_counts()
grade_counts.plot(kind='bar', title='Letter Grade Distribution')
plt.xlabel('Letter Grade')
plt.ylabel('Count')
plt.show()
```

---

## 5. Saving Processed Data

After adding a new column, it’s often useful to save the processed dataset. Here’s how to save it to a new CSV file:

```python
df.to_csv('letter_grades_added_happiness_data.csv', index=False)
```

---

## Summary

In this step, you learned:

- **Loading** a CSV file into a Pandas DataFrame
- **Exploring** the data using basic summary and statistical methods
- **Analyzing** specific columns and relationships between them
- **Cleaning** data by handling missing values
- **Saving** processed data to a new CSV file

Pandas is a powerful tool for data analysis in Python, allowing you to work with datasets efficiently and discover meaningful insights.

# Step 20

In this step, we’ll break down the components of the `reaction-time.html` file used to create a reaction time experiment that you will participate in for class! Then in step 21, we'll use Pandas to analyze the data we collect.

The reaction time experiment is implemented in JavaScript using the [jsPsych library](https://www.jspsych.org/), designed to help researchers conduct behavioral science experiments in a web browser.

[Click this link to download the `reaction-time.html` file](<files/reaction-time.html>){:download="reaction-time.html"}

In order to read this file, you'll want to move it to a folder in VSCode, and open it there.

Throughout this step, **I don't expect you to be learning JavaScript or jsPsych**. Instead, I want you to see how the principles you've learned in Python programming apply to other languages and tools. By examining the experiment’s structure and components, you’ll see how programming concepts you’ve learned in Python are used in a different context.

We'll also need to cover some basic concepts of experimental design, we'll do that before we dive into the code.

## General Principles of Experimental Design

Let's take a moment to recall (or learn for the first time!) the concepts of the Independent Variable and Dependent Variables in an experiment.

### Independent Variable (IV)

The indepdent variable in the experiment is the thing that is being man**I**pulated - I personally remember this by thinking of the "I" in IV. In the reaction time experiement, the independent variable is the color of the circle that is displayed, which requires a specific key press response from the participant depending on the color of the circle.

### Dependent Variable (DV)

The dependent variable in the experiment is the thing that is being measured - in other words, the thing that *depends* on the manipulated (independent variable). In the reaction time experiment, the dependent variable is the time it takes for the participant to press the correct key after the circle is displayed.

### Control Variables

Control variables are variables that are kept constant throughout the experiment. In the reaction time experiment, the control variables include the size of the circle, the position of the circle on the screen, and the key press that is required for each color.

### Data Collection

When programming an experiment, it's critical to think about how you're collecting your data. We'll look at how the data is collected in the reaction time experiment in the code breakdown.

### Random and Blocked Designs

In the reaction time experiment, there are two different trial types, trials where the circle is blue and trials where the circle is orange. These trials are presented in randomized order, which is a common design in psychology experiments to prevent participants from anticipating the next stimulus.

If you wanted to understand how color similarity might make people respond more slowly, you could have an additional "block" of trials within the experiment where blue and - let's say, a blue-ish purple - are presented as competing colors. This would allow you to examine the difference in reaction time between the two color pairs of blue and purple, and blue and orange.

## Jumping into the JavaScript

> Important code blocks will be highlighted in the following sections, but feel free to explore the entire file! If you want to know how the entire code block works, you give the file to ChatGPT or Copilot and ask the chatbot to explain it to you!

Many of the decisions for the experiment are made *outside* of the code. For example, in this experiment, the colors were chosen to be blue and orange. While we will load images into the experiment to show these colors to the participant when we want to display them, the actual color of the circle is not defined in the code. This is a design decision that was made before the experiment was programmed.

Similarly, it's not written into the code that the color is the IV, and that reaction time is the DV. These are concepts that are understood by the researcher before the experiment is programmed.

Now we'll dive into the pieces of the code that make the experiment run.

### Test Procedure

Below is a block of code within the `JavaScript` called "`test_procedure`", let's break it down:

```javascript
var test_procedure = {
  timeline: [fixation, test],
  timeline_variables: test_stimuli,
  repetitions: 25,
  randomize_order: true
};
```

- `timeline`
    - The `timeline` parameter is an array of objects that represent the sequence of events in the experiment. Here, the `test_procedure` consists of two components: `fixation` and `test`. The `fixation` object displays a fixation cross, while the `test` object presents the colored circle for the participant to respond to.
- `timeline_variables`
    - The `timeline_variables` parameter specifies the stimuli to be used in the experiment. In this case, `test_stimuli` is an array of objects containing the *color of the circle* and the correct response key for each trial.
- `repetitions`
    - The `repetitions` parameter determines how many times the `test_procedure` is repeated. With 25 repetitions, it tells the experiment to show the orange and blue circles 25 times each, meaning that there will be 50 trials in total.
- `randomize_order`
    - The `randomize_order` parameter specifies whether the order of trials should be randomized. When set to `true`, the order of trials is randomized to prevent participants from anticipating the next stimulus.

### Loading Images

This experiment uses two images, preloaded at the start to prevent delays during trials. Preloading is crucial when images need to display instantly. Other designs, like experiments requiring many images or complex visuals, may benefit from a more dynamic image-loading approach.

```javascript
var preload = {
  type: jsPsychPreload,
  images: ['images/blue.png', 'images/orange.png']
};
timeline.push(preload);
```

In simpler terms, this code gets the images ready to be shown at a moment's notice. The `jsPsychPreload` function is used to preload the images, ensuring they are ready for display when needed.

### Data Storage and CSV Export

Data in this experiment is stored in memory by jsPsych, including response accuracy and reaction times. At the experiment’s end, participants see a summary with accuracy and average reaction time. The `jsPsych.data.get().csv()` method then generates a CSV file of the collected data, downloadable via a button.

```javascript
var jsPsych = initJsPsych({
  on_finish: function() {
    jsPsych.data.displayData();
    document.getElementById('download-csv').style.display = 'block';
    document.getElementById('download-csv').onclick = function() {
      var csv = jsPsych.data.get().csv();
      var blob = new Blob([csv], { type: 'text/csv' });
      var url = window.URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'reaction_time_data.csv';
      a.click();
      window.URL.revokeObjectURL(url);
    };
  }
});
```

Let's break down the significant parts of the code block above:

- `jsPsych.data.displayData()`
    - This function displays the data collected during the experiment, showing participants their accuracy and average reaction time.
- `var csv = jsPsych.data.get().csv();`
    - This line generates a CSV file containing the data collected during the experiment.
- `var blob = new Blob([csv], { type: 'text/csv' });`
    - This code block creates a Blob object, which is a file-like object of raw data. In this case, it's a CSV file. A "Blob" is a way to store data that can be downloaded as a file.
- `a.download = 'reaction_time_data.csv';`
    - This line sets the `download` attribute of the anchor element to the desired filename for the downloaded CSV file. This allows the participant to download the data as a CSV file named `reaction_time_data.csv`.

## Connecting JavaScript and jsPsych to Python Principles

This experiment may be in JavaScript, but it uses many programming concepts you've learned in Python, let's think through them:

- **Functions and Initialization**: The function `initJsPsych()` initializes the experiment, just as you've used Python functions to set up programs and prepare data structures.
- **Control Structures (Loops and Conditions)**: The timeline configuration is structured similarly to Python dictionaries and lists. jsPsych uses objects to store multiple settings (analogous to Python’s dictionaries). Loops and conditional logic, like `randomize_order: true`, create flexible procedures, just as you’ve seen in Python loops and conditionals.
- **Trial Data Collection**: The way trial data is collected and stored in `jsPsych.data.get()` is similar to Python data management libraries (like `Pandas`), where you collect, process, and export data. Here, we export as CSV, a format you’ve worked with for storing and analyzing data in Python.
- **Parameter Setting and Modularity**: Each `timeline` component is modular and configured with specific parameters, similar to defining functions with arguments in Python. This modularity in design is essential for scalability and reusability in behavioral science programming.

In summary, although this experiment is in JavaScript, it reinforces core programming concepts: initializing structures, using loops and conditions to control flow, collecting data, and organizing code modularly. 

These are skills you’ll carry into any programming language, allowing you to adapt tools like jsPsych confidently for experimental design.

## Looking for more?

Check out the jsPSych documentation website to learn more about how to use jsPsych for your own experiments: [https://www.jspsych.org/](https://www.jspsych.org/). 

# Step 21

In this step, we will process and visualize the reaction time data we collected in `Step 20` using Pandas! We will get this data from a zip file containing many `.csv` files, where each file contains data from a participant in a reaction time experiment. 

You will learn to:

1. Load a zip file of data into Python.
2. Extract and load all `.csv` files into a single pandas DataFrame.
3. Clean the data to isolate relevant variables. Visualize "raw" reaction time data.
4. Aggregate data by participant and analyze mean reaction times.
5. Visualize aggregated data.

## 0: Download the Zip File

> What's a Zip File? A zip file is a compressed folder that contains one or more files. It's a common way to package and share multiple files together.

[Click here to download the reaction time `.zip` file](files/reaction_time_data.zip)



## 1: Load and Unzip the Data

To begin, ensure you have downloaded the zip file. You can unzip it manually or programmatically within Python. Here’s how to do it in Python:

```python
import zipfile
import os

# Define file paths
zip_path = 'reaction_time_data.zip' # If you've put your file in the same directory as the notebook you're working in, your path is just the file name. If not, you'll need to include the path to the file.
extract_path = '.' # This will extract the files to the current directory

# Unzip the file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
```

After running this code, you should see the extracted `.csv` files in the specified directory - this will be a lot of files!

## 2: Load CSV Files into a Pandas DataFrame

With the files extracted, we can load each `.csv` file into a DataFrame. Each row in the final DataFrame will represent a trial, with columns for relevant data.

```python
import pandas as pd
import glob
import os

# Path to the directory containing extracted .csv files
csv_files = glob.glob(os.path.join(extract_path, '*.csv'))

# Initialize an empty list to store DataFrames
dfs = []

# Loop through and read each csv file
for idx, file in enumerate(csv_files):
    data = pd.read_csv(file)

    # Extract relevant rows and columns
    # Filter rows where 'trial_type' is 'response' (indicating a reaction time trial)
    data = data[data['trial_type'] == 'image-keyboard-response']

    # Select and rename relevant columns
    df = data[['rt', 'stimulus', 'response', 'correct']].copy()
    df.rename(columns={
        'rt': 'reaction_time',
        'stimulus': 'circle_color',
        'response': 'key_pressed',
        'correct': 'accuracy'
    }, inplace=True)

    # Clean up 'circle_color' to extract only color names
    df['circle_color'] = df['circle_color'].str.extract(r'images/(\w+).png')[0]

    # Add subject_id column
    df['subject_id'] = idx + 1

    # Reorder columns to make 'subject_id' the first column
    df = df[['subject_id', 'reaction_time', 'circle_color', 'key_pressed', 'accuracy']]

    # Append the processed DataFrame
    dfs.append(df)

# Concatenate all DataFrames
all_data = pd.concat(dfs, ignore_index=True)
```

## 3: Clean and Visualize Reaction Time Data

Now that we have all trials loaded into a DataFrame, we can start visualizing the reaction time data.

### 3a. Histogram of Reaction Time Data

Use a histogram to explore the distribution of reaction times. Adjust the bin width with an interactive widget.

```python
import matplotlib.pyplot as plt
import ipywidgets as widgets

def plot_histogram(bin_width):
    plt.hist(all_data['reaction_time'].dropna(), bins=bin_width)
    plt.title('Histogram of Reaction Times')
    plt.xlabel('Reaction Time (ms)')
    plt.ylabel('Frequency')
    plt.show()

widgets.interactive(plot_histogram, bin_width=widgets.IntSlider(min=5, max=100, step=5, value=20))
```

### 3b. Box Plot of Mean Reaction Times by Accuracy

A box and whisker plot can show differences in reaction times between "true" (correct) and "false" (incorrect) responses.

!!! Tip "Seaborn"
    Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for creating attractive and informative statistical graphics. You can install Seaborn using `pip install seaborn`.

    In your notebook, you might want to run `%pip install seaborn` to install Seaborn, instead of the normal pip install.

```python
import seaborn as sns

# Plot box and whisker plot for reaction times by accuracy
sns.boxplot(x='accuracy', y='reaction_time', data=all_data)
plt.title('Reaction Times by Accuracy')
plt.xlabel('Accuracy (True or False)')
plt.ylabel('Reaction Time (ms)')
plt.show()
```

It's great to have a visualization, but it will probably be good to know the means and standard deviation values of these plots as well, let's use Pandas to calculate those!

```python
import pandas as pd

# Assuming 'all_data' is your DataFrame
true_responses = all_data[all_data['accuracy'] == True]
false_responses = all_data[all_data['accuracy'] == False]

true_mean = true_responses['reaction_time'].mean()
true_sd = true_responses['reaction_time'].std()

false_mean = false_responses['reaction_time'].mean()
false_sd = false_responses['reaction_time'].std()

# Print the mean and standard deviation values, and the counts of each group
print(f"True responses - Mean: {true_mean}, SD: {true_sd}, Count: {len(true_responses)}")
print(f"False responses - Mean: {false_mean}, SD: {false_sd}, Count: {len(false_responses)}")
```

#### Think about the data

Look at the means and standard deviations. What do you think a paired t-test would show? What problem arrises when we look at the "Count" of each data type?

## 4: Aggregate Mean Reaction Times by Participant/Subject

Next, let’s condense the data to calculate each subject's mean reaction time and the number of "true" (correct) trials out of 50.

```python
# Calculate mean reaction times and true trial counts
subject_summary = all_data.groupby('subject_id').agg(
    mean_reaction_time=('reaction_time', 'mean'),
    true_count=('accuracy', lambda x: (x == True).sum())
).reset_index()
```

## 5: Visualize Mean Reaction Time Data

### 5a. Histogram of Mean Reaction Times

Plot a histogram of mean reaction times for each participant.

```python
plt.hist(subject_summary['mean_reaction_time'], bins=20)
plt.title('Histogram of Mean Reaction Times by subject')
plt.xlabel('Mean Reaction Time (ms)')
plt.ylabel('Frequency')
plt.show()
```

### 5b. Scatterplot of Reaction Time and % "True" Responses

Plot a scatterplot to explore the relationship between subjects’ mean reaction times and their accuracy rate.

```python
# Calculate accuracy percentage
subject_summary['true_percentage'] = (subject_summary['true_count'] / 50) * 100

# Scatterplot of mean reaction time vs. true percentage
plt.scatter(subject_summary['mean_reaction_time'], subject_summary['true_percentage'])
plt.title('Mean Reaction Time vs. % True Responses')
plt.xlabel('Mean Reaction Time (ms)')
plt.ylabel('% True Responses')
plt.show()
```

## 6. Have fun with it!

Take time to play with [Seaborn](https://seaborn.pydata.org/) and [Matplotlib](https://matplotlib.org/) to create more visualizations and explore the data further. You can also experiment with different data transformations and analysis techniques to gain deeper insights!

Dig into the Pandas dataframe, look at the data, and see if you can find any interesting patterns or relationships.

```python
# Display the first few rows of the DataFrame
all_data.head()
```

You can grab different columns and plot them against each other to see if there are any relationships. For example, you could plot the reaction time against the color of the circle that was shown to the participant.

## 7. Review

In this step, you’ve learned how to handle, clean, and visualize reaction time data using pandas, matplotlib, and seaborn. In a future step, we'll look at how to analyze this data statistically to draw meaningful conclusions!

# Step 22

## **Basic Statistics**

In this step, we'll apply statistical methods to the reaction time dataset generated in the previous steps. This dataset includes data related to reaction times for trials where the independent variable (IV) is the color of a circle. Here's what we aim to accomplish:

### Objectives
1. Establish the dataset.
2. Compute basic descriptives and create plots suitable for a paired samples t-test.
3. Perform and interpret a paired samples t-test.
4. Manipulate the dataset to add an additional variable, *previous circle color*.
5. Set up and run a two-way ANOVA to investigate interactions between the current circle color and the previous circle color.

---

### 1: Establish the Dataset
We will start with the `all_data` dataset generated in Step 21. This dataset contains reaction times for trials where the circle color is the independent variable.

Go back to Step 21 to get the `all_data` dataframe, when you do you should be able to run the code below and get the following result.

Code:

```python
all_data.head()
```

Result:
```python
	subject_id	reaction_time	circle_color	key_pressed	accuracy
0	    1	        445.0	        orange	        j	       True
1	    1	        386.0	        blue	        f	       True
2	    1	        366.0	        blue	        f	       True
3	    1	        374.0	        orange	        j	       True
4	    1	        409.0	        orange	        j	       True
```

---

### 2: Descriptives and Paired Samples T-Test Preparation
To prepare for the paired samples t-test:
- Compute summary statistics for each circle color.
- Visualize the data with plots to check assumptions like normality.

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Group by circle color and calculate summary statistics
descriptives = all_data.groupby('circle_color')['reaction_time'].describe()

# Boxplot to visualize reaction times by circle color
sns.boxplot(x='circle_color', y='reaction_time', data=all_data)
plt.title('Reaction Times by Circle Color')
plt.show()

# Print descriptive statistics
print(descriptives)
```

---

### 3: Perform the Paired Samples T-Test
A paired samples t-test compares reaction times between two conditions.

!!! Tip "pip install `scipy`"
    At this point you'll most likely need to install the `scipy` package. You can do this by running `%pip install scipy` in your notebook.

    What's `scipy`? Think of it as "scientific Python" - it's a library that provides many user-friendly and efficient numerical routines andf functions that are commonly used in scientific and engineering applications.

```python
from scipy.stats import ttest_rel

# Perform paired t-test
group1 = all_data[all_data['circle_color'] == 'orange']['reaction_time'] # Orange circle
group2 = all_data[all_data['circle_color'] == 'blue']['reaction_time'] # Blue circle

t_stat, p_value = ttest_rel(group1, group2)

# Display results
print(f"Paired Samples T-Test:\nT-Statistic = {t_stat}, p-value = {p_value}")
```

**Interpretation:** Based on the p-value, determine if there is a significant difference between reaction times for orange and blue circles.

??? Tip "Check your results"
    If you ran it correctly, you should get the following output:
    ```python
    # Paired Samples T-Test:
    # T-Statistic = -0.2520879211177987, p-value = 0.8010674499745879
    ```
    The p-value is greater than 0.05, indicating that there is no significant difference between reaction times for orange and blue circles.

    Is this surprising? No not really! The data didn't appear to be significantly different in the boxplot, and we don't have a good reason to think that the color of the circle alone would affect reaction times.

---

### 4: Add *Previous Circle Color* Variable
To explore potential effects of *previous circle color*, add this column to the dataset. The first trial is excluded as it lacks a "previous" circle.

```python
# Shift the 'circle_color' column to create the 'previous_circle_color' column
all_data['previous_circle_color'] = all_data['circle_color'].shift(1)

# Remove the first trial or row of data from every subject
all_data = all_data.groupby('subject_id').apply(lambda x: x.iloc[1:]).reset_index(drop=True)

# Display the updated dataset
print(all_data.head())
```

!!! Tip "Lambda Functions"
    In the code above, we used a lambda function to remove the first trial or row of data from every subject. Lambda functions are small, anonymous functions that can have any number of arguments but only one expression. They are often used in situations where a function is needed for a short period of time.

    Be on the lookout for a "Side Quest" where you can learn more about lambda functions!

I have a hypothesis; if the previous circle color was the same as the current circle color, the reaction time will be faster. Let's see if this is true!

To make our live's easier, we'll create a new column to include a new variable, `repeat_color`, which will be `True` if the previous circle color is the same as the current circle color, and `False` otherwise.

```python
# Create a new column 'same_color' to indicate if the previous circle color is the same as the current circle color
all_data['repeat_color'] = all_data['circle_color'] == all_data['previous_circle_color']
all_data.head()
```

In the next part, we'll perform an additional t-test to see if there is a significant difference in reaction times between trials where the previous circle color is the same as the current circle color and trials where it is different.

---

### 5: Another Paired Samples T-Test

Based on the code in part 3, I'd like for you to look at the code and then think about how you'd set it up yourself. After you think/test it, continue reading below.

#### Some Snags in the Plan

A problem arrises if you simply group the data by `repeat_color` and then run the t-test. The issue is that we no longer have equal sample sizes for each group, this is because, randomly, we ended up with 250 trials where the previous circle color was the same as the current circle color, and 828 trials where they were different.

Run the following code and you'll get an `ValueError: unequal length arrays` error.

```python
# Perform paired t-test
group1 = all_data[all_data['repeat_color'] == True]['reaction_time']  # Repeat color is True
group2 = all_data[all_data['repeat_color'] == False]['reaction_time']  # Repeat color is False

t_stat, p_value = ttest_rel(group1, group2)

# Display results
print(f"Paired Samples T-Test:\nT-Statistic = {t_stat}, p-value = {p_value}")

# Boxplot visualization
plt.figure(figsize=(10, 6))
sns.boxplot(x='repeat_color', y='reaction_time', data=all_data)
plt.title('Reaction Time by Repeat Color')
plt.xlabel('Repeat Color')
plt.ylabel('Reaction Time')
plt.show()
```

We can run this block of code below to demonstrate that the two arrays are indeed unequal lengths:

```python
import numpy as np

np.shape(group1), np.shape(group2)
```

#### Fixing the Issue

One way to fix the problem (an imperfect, but fine way for quick data visualization and exploration) is to randomly sample 250 trials from the `repeat_color == False` group. This way, we'll have equal sample sizes for both groups.

Let's do that below, and then perform the t-test and plot the results.

```python
# Randomly sample 250 trials from the 'repeat_color' == False group

group2_sample = all_data[all_data['repeat_color'] == False].sample(n=250, random_state=1)['reaction_time']

t_stat, p_value = ttest_rel(group1, group2_sample)

# Display results
print(f"Paired Samples T-Test:\nT-Statistic = {t_stat}, p-value = {p_value}")

# Get descriptive statistics
group1_desc = group1.describe()
group2_desc = group2_sample.describe()

print("\nDescriptive Statistics for Group 1 (Repeat Color is True):")
print(group1_desc)

print("\nDescriptive Statistics for Group 2 (Repeat Color is False):")
print(group2_desc)

# Boxplot visualization
plt.figure(figsize=(10, 6))
sns.boxplot(x='repeat_color', y='reaction_time', data=all_data)
plt.title('Reaction Time by Repeat Color')
plt.xlabel('Repeat Color')
plt.ylabel('Reaction Time')
plt.show()
```

By making the random_state equal to 1, we ensure that the random sample is the same every time we run the code. This way, we can reproduce the results and compare them across different runs.

This should also mean you see the same result that I do: it looks like there is no significant difference between reaction times when the previous circle color is the same as the current circle color compared to when they are different. It was a cool idea though, right?!

### 6: Two-Way ANOVA

There's one more thing that I'd like for us to explore: the possible effect and interaction between subjects...

We can set up a two-way ANOVA to investigate the effects of the current circle color, the previous circle color, and their interaction on reaction times.

!!! Tip "%pip install statsmodels"
    To run the two-way ANOVA, you'll need to install the `statsmodels` package. You can do this by running `%pip install statsmodels` in your notebook.

```python
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

# Fit the two-way ANOVA model
model = ols('reaction_time ~ C(subject_id) + C(circle_color) + C(subject_id):C(circle_color)', data=all_data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Display the ANOVA table
print(anova_table)

# Boxplot visualization
plt.figure(figsize=(12, 8))
sns.boxplot(x='circle_color', y='reaction_time', hue='subject_id', data=all_data)
plt.title('Reaction Time by Circle Color and Subject ID')
plt.xlabel('Circle Color')
plt.ylabel('Reaction Time')
plt.legend(title='Subject ID', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
```

If everything has gone smoothly, your resulting ANOVA table should look like this:
```txt
                                     sum_sq      df          F        PR(>F)
C(subject_id)                  3.327539e+06    21.0  11.095641  1.533542e-33
C(circle_color)                1.209871e+03     1.0   0.084720  7.710580e-01
C(subject_id):C(circle_color)  2.686349e+05    21.0   0.895760  5.971599e-01
Residual                       1.476631e+07  1034.0        NaN           NaN
```

The last column is your p-value in scientific notation; we can see that the only significant effect is the subject ID. This is not surprising, as we would expect that different subjects would have different reaction times.

What does this mean? It means that the color of the circle and the interaction between the color of the circle and the subject ID do not have a significant effect on reaction times, but different people do have different reaction times.

Now you've run a two-way ANOVA in Python! This is a powerful tool for analyzing the effects of multiple factors on a dependent variable.

---

### Conclusion
In this step, we:

- Established the reaction time dataset and computed basic statistics.
- Conducted a paired samples t-test to evaluate differences between orange and blue circles.
- Introduced a new variable (*same circle color*), and randomly sampled to ensure equal sample sizes for a second t-test.
- Performed a two-way ANOVA and visualized all of the data.

What are some things we didn't do?

- We didn't check for normality or homogeneity of variance in the t-tests or ANOVA.
- We didn't explore other statistical tests or models that could be applied to this dataset (Logistic Regression would be great, for example).
- We didn't remove outliers, this could have changed the results of the t-tests and ANOVA.

Take a moment to think about what else you'd like to explore with this dataset. What other statistical tests or models could be applied? What additional variables could be included to enhance the analysis? If you're brave enough, try to implement some of these ideas!

# Step 23

## Data Dive I: Finding Data

Your journey into data analysis starts with finding an interesting dataset. For this step, you can either:

1. **Search for Open Datasets**: Explore open-source datasets available on platforms like [Kaggle](https://www.kaggle.com/), [Data.gov](https://www.data.gov/), or [Google Dataset Search](https://datasetsearch.research.google.com/).

2. **Download Personal Data**: Many services allow you to download your personal data (e.g., Instagram, Spotify, or Google). Make sure the downloaded data is in a workable format such as `json`, `csv`, or `txt`. If you want to work with your own data, Google how to download it from the respective service.

## Preparing for Import

Once you have your data:

- Ensure the dataset is saved locally in a known file path.
- Check the file format (e.g., `.csv`, `.json`, `.txt`) as it will guide how you load it into Python.

## Using AI to Help Format Your Data

Organizing raw data can be challenging, especially if the dataset has many columns or uses inconsistent formatting. AI tools like **ChatGPT**, **Claude**, and **Microsoft Copilot** can help you write Python code to clean and organize your data.

### Best Practices When Using AI Tools

1. **Feed Your Datafile**: Many AI tools allow you to upload your dataset directly for analysis. Uploading your file can help the AI better understand your data structure.
2. **Provide Context**: Clearly describe what you're trying to achieve, such as renaming columns, handling missing values, or filtering rows.
3. **Iterate**: If the AI-generated code doesn’t work perfectly, provide feedback and ask for adjustments.

### Example Prompts for Using AI

Here are some sample prompts to get you started:

#### Prompt 1: General Formatting

*"I have a dataset in CSV format with inconsistent column names. Here's a sample of the data: [paste or upload your dataset]. Could you help me write Python code using Pandas to clean the column names (e.g., make them lowercase and replace spaces with underscores) and handle missing values by filling them with 0?"*

#### Prompt 2: Renaming Columns

*"Here’s my dataset: [paste or upload]. I want to rename the column `Old Column Name` to `new_column_name`. Could you provide the Pandas code to do this?"*

#### Prompt 3: Filtering Rows

*"My dataset has a column called `age`. Could you write Python code using Pandas to filter out rows where the age is less than 18? Here’s the data: [paste or upload]."*

#### Prompt 4: Creating New Columns

*"I have this dataset: [paste or upload]. I’d like to create a new column that calculates the ratio of `sales` to `profit`. Could you help me write the code for that in Pandas?"*

#### Prompt 5: Data Structure Insights

*"Here’s my dataset: [paste or upload]. Could you provide a summary of the dataset, including column data types and a preview of the first few rows? Also, suggest any obvious cleaning steps that might be necessary."*

### Why Use AI?

AI tools can speed up your workflow, reduce errors, and give you creative ideas for working with your data. However, it's essential to understand the basics of Pandas so you can verify and tweak the code generated by the AI.

How do you get the basics of Pandas down? By practicing and looking things up! In previous learning steps, we've used Pandas to do a variety of tasks, such as filtering data, creating new columns, and summarizing data. Go back and look at what we did, look up function names in the Pandas documentation [(linked here)](https://pandas.pydata.org/pandas-docs/stable/index.html), and practice using Pandas on your own data.

## Importing Data into Pandas

Follow these steps to import and organize your data into a Pandas DataFrame:

### 1. Setting Up

Start by importing the necessary libraries.

```python
import pandas as pd
import json  # Only if your dataset is in JSON format

# Add more libraries if needed (e.g., os for file management)
```

### 2. Loading Data Based on File Type

#### For CSV Files:

```python
# Replace 'your_dataset.csv' with your file's name
file_path = 'your_dataset.csv'
data = pd.read_csv(file_path)

# Preview the first few rows
print(data.head())
```

#### For JSON Files:

```python
# Replace 'your_dataset.json' with your file's name
file_path = 'your_dataset.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Convert JSON data into a DataFrame
df = pd.DataFrame(data)
print(df.head())
```

#### For TXT Files (Delimited):

```python
# Replace 'your_dataset.txt' with your file's name and delimiter (e.g., '\t' for tab-delimited)
file_path = 'your_dataset.txt'
data = pd.read_csv(file_path, delimiter='\t')

# Preview the first few rows
print(data.head())
```

### 3. Cleaning and Organizing the DataFrame

Once your data is loaded, ensure it's organized and meaningful:

!!! Tip "Keep looking at your DataFrame"
    As you clean and organize your data, keep checking the DataFrame to ensure it's structured the way you want. Use `print(data.head())` to preview the first few rows and `print(data.info())` to get an overview of the columns and data types.

- **Inspect the structure**:
  ```python
  print(data.info())  # Overview of columns and data types
  ```

- **Rename columns** if needed:
  ```python
  data.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)
  ```

- **Filter unnecessary rows/columns**:
  ```python
  # Dropping a column
  data.drop(columns=['unnecessary_column'], inplace=True)
  
  # Keeping specific rows
  data = data[data['column_name'] > threshold_value]
  ```

- **Handle missing values**:
  ```python
  data.fillna(value=default_value, inplace=True)  # Fill missing values
  data.dropna(inplace=True)  # Optionally drop rows with missing values
  ```

## Conclusion

At this stage, you should have:

- Located and downloaded an interesting dataset.
- Used AI tools (optional but highly recommended!) to assist in formatting and organizing your data.
- Imported it into Python using Pandas.
- Organized the dataset to ensure meaningful rows and columns.

Once you're comfortable with the structure of your data, you're ready to dive into visualizations in Step 24!