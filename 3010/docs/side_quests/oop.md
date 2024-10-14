# Side Quest: OOP Challenge

## Introduction

Welcome to the Week 6 Side Quest! This exercise will help you explore and apply inheritance in Python's Object-Oriented Programming (OOP) by developing a hierarchy of plant classes that exhibit unique behaviors.

## Understanding Inheritance in OOP

### What is Inheritance?

Inheritance is a key OOP feature that allows one class (a subclass) to inherit the attributes and methods from another class (known as a superclass or base class). This facilitates code reusability, reduces redundancy, and enhances the maintainability of code.

### Why Use Inheritance?

Inheritance allows you to write a general class with common functionality and have more specific classes extend this class, adding or modifying behaviors. This structure makes your code more modular and intuitive.

## Task Description

You will create a basic `Plant` class and then extend it with specific plant types, each inheriting the general characteristics of the base class but also introducing their own unique behaviors.

### Part 1: Create the Plant Base Class

Start by defining a `Plant` class that will act as the base class for all specific plant types.

- Attributes: `name`, `height`
- Method: `grow()`, simulates the growth of the plant.

```python
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grows to {self.height}cm tall.")
```

### Part 2: Define Specific Plant Subclasses

Next, create specific subclasses for `Flower` and `Tree`. These subclasses will inherit the base `Plant` class by creating them and feeding in `Plant` as an argument to the class definition, and then calling a `super()` method in the `__init__` method.

`super()` is used to call the superclass's (the class from which a method is inherited) methods.

```python
class Flower(Plant):
    def grow(self):
        super().grow()  # Calls the base class grow method
        print(f"The {self.name} prepares to bloom.")

class Tree(Plant):
    def grow(self):
        super().grow()  # Calls the base class grow method
        print(f"The {self.name} stretches towards the sky.")
```

### Part 3: Adding Unique Behaviors to Subclasses

Now, add unique methods to these subclasses that reflect specific behaviors not shared by all plants.

- Add a `bloom()` method to the `Flower` class.
- Add a `shed_leaves()` method to the `Tree` class.

```python
class Flower(Plant):
    def bloom(self):
        print(f"The {self.name} blooms with vibrant colors!")

class Tree(Plant):
    def shed_leaves(self):
        print(f"The {self.name} sheds its leaves for the winter.")
```

### Part 4: Integrating New Behaviors into the Growth Cycle

Now, try to modify the `grow()` method in each subclass to include these new behaviors as part of the growth cycle.

## Advanced Challenge (Optional)

Consider enhancing the `Flower` and `Tree` classes further by:
- Implementing seasonal effects where flowers bloom only in spring and trees shed leaves only in autumn.
- Adding additional attributes like `color` for flowers and `leaf_count` for trees to make the simulations more detailed.
