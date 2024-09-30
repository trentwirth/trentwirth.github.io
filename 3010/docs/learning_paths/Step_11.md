# Step 11

Welcome back! In Step 10, we introduced the fundamental concepts of Object-Oriented Programming (OOP) with Python classes and objects. Today, we will dive deeper into these concepts to solidify your understanding and practical skills in OOP.

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