# Coding Assignment 3

> Note: Ensure you have thoroughly understood the concepts related to Python classes, instance methods, and class interaction as covered in Steps 9-12 of the Learning Path before attempting this assignment.

This assignment is designed to test your ability to debug complex class structures, create classes with specific behaviors and attributes, and develop interactions between multiple classes.

## Problem 1: Debugging a Class Implementation

Below is a Python class called `Plant` that allows you to water, prune and display information about an instanced plant. 

At the end of the code block is an example of what the code should look like... but something isn't right! There are 5 errors in the code block, you'll get 1 point for each error fixed.

```python
class Plant:
    def __init__(self, plant_type: str, height: float):
        self.plant_type = plant type
        self.height = height  # Initial height in centimeters
        self.growth_rate = "1.0"  # Initial growth rate, height increase per watering

    def water(self):
        """Water the plant to increase its height by the growth rate."""
        self.height + self.growth_rate

    def prune(self):
        """Prune the plant to increase its growth rate. No pain, no gain."""
        self.hieght -= 0.5 # Reduce the height by 0.5 cm
        self.growth_rate = 1.0  # Increase growth rate by 1 cm per watering

    def display_info(self):
        """Display the current information about the plant."""
        display_message = f"Plant Type: {self.plant_type}, Height: {self.height}cm, Growth Rate: {self.growth_rate}cm/watering"
        print()


# Creating instances of the Plant class
sunflower = Plant("Sunflower", 30.0)
rose = Plant("Rose", 20.0)
cactus = Plant("Cactus", 50.0)

# Interacting with the sunflower plant
sunflower.water()
sunflower.prune()
sunflower.water()
sunflower.display_info()

# Interacting with the rose plant
rose.prune()
rose.display_info()

# Interacting with the cactus plant
cactus.water()
cactus.display_info()

# If your code is working correctly, the output should be:

    # Plant Type: Sunflower, Height: 32.5cm, Growth Rate: 2.0cm/watering
    # Plant Type: Rose, Height: 19.5cm, Growth Rate: 2.0cm/watering
    # Plant Type: Cactus, Height: 51.0cm, Growth Rate: 1.0cm/watering
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

!!! Tip "Practice for the Written Assessment"
    To practice for the written assessment, before you start your implementation, either on a piece of paper or in your text editor of choice (Google/Word Doc, etc.), outline how this code should work independent of your ability to write and test the code. 

    The written assessment will be just that - your ability to write out how you would solve a problem, not necessarily your ability to write the code itself. You can and should be as detailed as you can manage. 

    If you'd like more practice, try writing out your solution to Problem 3 as well!

## Problem 3: Develop Two Interacting Classes

Create two classes, `Author` and `Book`. The `Author` class should have attributes like name and a list of books, while the `Book` class should include attributes like title, author (reference to an `Author` object), and publication year. Demonstrate how these instances interact by querying an author to list all books written by them.

> Hint: You can look at the "Family" and "Person" classes from Step 11 to help you create these classes.

___

Ensure all your solutions are tested and functioning as expected. When you are satisfied, you can submit your work as an `.ipynb` on Canvas.