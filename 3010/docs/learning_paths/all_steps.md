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

In Step 3, first, we will install `Anaconda` as well as a new version of `Python` onto each of your machines. 

After that, we will learn about different data types in Python and how to work with variables. Data types and variables are the building blocks of any programming language, and understanding them is essential for writing code!

## Installing `Anaconda` and `Python`

You might be wondering, what's `Anaconda`? `Anaconda` is a free and open-source distribution of Python ([and R](https://www.r-project.org/)) programming languages for scientific computing, that aims to simplify environment creation and management. Look back to Step 2 if you need a refresher on `Python Environments`.

### AI Exercise: Install `Anaconda` and `Python`

I'd like for you to explore using an AI Chatbot to help you do technical IT tasks, like installing software.

Take the following prompt to either [Microsoft Copilot](https://copilot.microsoft.com) or [ChatGPT](htps://chatgpt.com) - if you go to Copilot, make sure to use your student credentials (if you have them) to login and get access to the best version of Copilot. Note: This best version doesn't maintain a chat history, so if you want to keep a record of your conversation, you should take notes.

Here's the prompt (*make sure you tell it if you have a Windows machine or a Mac*):

```
I'm a psychology student who is new to VSCode and Python. 
I need to install Anaconda and Python version 3.12, 
and I want to do it through the VSCode terminal. 
If that doesn't work, we can try other methods. 

I have a _____ machine. Can you help me with this?
```

### Exercise: 

Work with the Chatbot to get the software installed on your machine. If you're doing this in class and you run into issues, let your professor know!

Once you've installed `Anaconda` and `Python`, you're ready to move on to the next section!

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

??? Note "Answer"
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
