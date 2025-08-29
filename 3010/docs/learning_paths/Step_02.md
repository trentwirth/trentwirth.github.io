# Step 2

In step 2, we have two objectives:

1. Get familiar with the VSCode interface, including the file explorer, terminal, and editor.
2. Introduce ourselves to the building blocks of Python, including environments, libraries, syntax, and programming terminology.

## Exercise: Intro to VSCode

### **Visually navigating VSCode**

Visual Studio Code (VSCode) is a powerful code editor. If you didn't install it yet, go back to `Step 1` and follow the instructions.

Here's a quick overview of the main components we're concerned with:

- **Side Bar**: Shows different views like the Explorer, Search, Source Control, etc.
- **Editor**: The main area where you edit your files.
- **Bottom Panel**: Located at the bottom, it shows output, terminal, problems, etc.

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
    
### Some more basic terminal commands

1. **Get to know your directory structure in the terminal**:
Use the `ls` command to list the contents of your current directory:
     ```sh
     ls
     ```

2. Use the `mkdir` command:
     ```sh
     mkdir a_folder_is_a_directory
     ```
> `mkdir` stands for "make directory" and is used to create new directories (or, "folders").

3. **Create a new directory called `a_folder_is_a_directory/this_is_a_directory_within_a_directory`**:
Use the `mkdir` command again:
     ```sh
     mkdir a_folder_is_a_directory/this_is_a_directory_within_a_directory
     ```
> This creates a directory within a directory, also known as a subdirectory.

4. **Create a file called `test_1.md` next to the `this_is_a_directory_within_a_directory` directory**:
Use the `New-Item` command:
     ```sh
     New-Item -Name "test_1.md" -ItemType File
     ```
> If you want to create the file inside of a particular directory, you can specify the path like this:
```sh
New-Item -Name "a_folder_is_a_directory/this_is_a_directory_within_a_directory/test_1.md" -ItemType File
```

!!! Warning "Are you using a Mac?"
     If you are on a Mac, the command to create a new file is slightly different. Use the `touch` command instead:
     ```sh
     touch test_1.md
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
