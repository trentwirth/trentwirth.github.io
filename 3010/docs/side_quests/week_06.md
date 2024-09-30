# Week 6 Side Quest: OOP Challenge

## Introduction

Welcome to the Week 6 Side Quest! This week, we challenge you to explore advanced Object-Oriented Programming (OOP) concepts by engaging with inheritance and abstract classes. You will be tasked with creating a system of classes that simulate a small ecosystem involving different types of plants.

## Task Description

Your challenge is to design an `Ecosystem` that consists of various types of `Plant` objects. You’ll demonstrate inheritance by creating specific plant types that inherit from a base `Plant` class and use an abstract class to define common interfaces.

### Requirements:

- **Plant Abstract Class**
  - Create an abstract class called `Plant` that defines a structure for other plant types.
  - Attributes: `name`, `height`
  - Abstract Methods: `grow()`, which all subclasses must implement differently based on their growth behavior.

```
from abc import ABC, abstractmethod

class Plant(ABC):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @abstractmethod
    def grow(self):
        pass
```

- **Specific Plant Subclasses**
  - Implement at least two specific plant subclasses (e.g., `Flower`, `Tree`) that inherit from `Plant` and provide specific implementations of the `grow()` method.

```
class Flower(Plant):
    def grow(self):
        self.height += 2
        print(f"The {self.name} grows quickly and is now {self.height}cm tall.")

class Tree(Plant):
    def grow(self):
        self.height += 1
        print(f"The {self.name} grows slowly and is now {self.height}cm tall.")
```

- **Ecosystem Class**
  - Implement an `Ecosystem` class that can contain multiple different plants and has a method to simulate passing time in which all plants grow.

```
class Ecosystem:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def pass_time(self):
        print("Time is passing in the ecosystem...")
        for plant in self.plants:
            plant.grow()
```

## Advanced Challenge (Optional)

- Implement a method in the `Ecosystem` that can report the total height of all plants combined, showcasing aggregate data collection.
- Experiment with polymorphism by adding different methods or properties to the subclasses that can be called specifically in more detailed scenarios.

## Resources

- Python Official Documentation on Abstract Base Classes: [Link](https://docs.python.org/3/library/abc.html)
- Tutorial on Python Inheritance and Polymorphism: [Link](https://realpython.com/inheritance-composition-python/)

## Submission Guidelines

Please submit your Python script file containing the `Plant`, `Flower`, `Tree`, and `Ecosystem` classes. Include a brief discussion in your submission about how inheritance and abstraction help manage complexity in software development.

Let's cultivate your understanding of advanced OOP with this botanical challenge!