# Coding Assignment 3

> Note: Ensure you have thoroughly understood the concepts related to Python classes, instance methods, and class interaction as covered in Steps 9-12 of the Learning Path before attempting this assignment.

This assignment is designed to test your ability to debug complex class structures, create classes with specific behaviors and attributes, and develop interactions between multiple classes.

## Problem 1: Debugging a Class Implementation

You are given a Python class that manages user profiles for a software application. The class is intended to add, update, and retrieve user information but contains multiple errors. Identify and fix a total of five errors ranging from syntax to logical issues.

Here's the code:

```python
class UserProfile:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.profiles = {}

    def add_profile(self, profile_data: dict):
        if profile_data.id not in self.profiles:
            self.profiles[profile_data.id] = profile_data

    def get_profile(self, profile_id: int):
        return self.profiles.get(profile_id, "Profile not found.")

    def update_profile(self, profile_id: int, new_data: dict):
        if profile_id in self.profiles:
            self.profiles[profile_id].update(new_data)
            return "Update successful"
        else:
            return "Profile not found."
```

## Problem 2: Create a "Pet" Class

Create a class called `Pet` with attributes and methods that reflect the behavior and properties of pets. This class should include the following:

- Attributes:
  - `name` (str): the name of the pet
  - `age` (int): the age of the pet in years
  - `species` (str): the type of animal
  - `fur_color` (str): the color of the fur
  - `tail_type` (str): the type of tail the pet has
  - `hungry` (bool): whether the pet is hungry, initially set to `True`

- Methods:
  - `feed`: changes the `hungry` attribute to `False` when called and prints "Pet is now fed!"
  - `describe`: prints a description of the pet, including all of its attributes. 

Create three instances of this class with different attributes and demonstrate the functionality of the methods.

## Problem 3: Develop Two Interacting Classes

Create two classes, `Author` and `Book`. The `Author` class should have attributes like name and a list of books, while the `Book` class should include attributes like title, author (reference to an `Author` object), and publication year. Demonstrate how these instances interact by querying an author to list all books written by them.

> Hint: You can look at the "Family" and "Person" classes from Step 11 to help you create these classes.

___

Ensure all your solutions are tested and functioning as expected. When you are satisfied, you can submit your work as an `.ipynb` on Canvas.