# Step 10

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
