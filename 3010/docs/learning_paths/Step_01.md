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
