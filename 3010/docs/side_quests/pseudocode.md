# Pseudocode

## What is Pseudocode?

Pseudocode is a way to describe how a program works using plain, human-readable language. It doesn't follow the syntax of any specific programming language but is structured to reflect the logical flow and actions that a program will take. Think of it as a "blueprint" for your code.

Pseudocode is useful because it allows you to focus on the **logic** and **structure** of a program without worrying about the syntax errors that can come from coding too soon. It's a great tool for planning how you'll solve a problem and is often used as a step between figuring out what a program needs to do and writing the actual code.

### Why Pseudocode is Useful

- **Clarifies Thinking**: Writing pseudocode forces you to think through the logic of a problem before getting bogged down in syntax.
- **Simplifies Collaboration**: Since pseudocode is written in plain language, it’s easier for non-programmers or teammates who aren't familiar with a specific programming language to understand and contribute to the plan.
- **Reduces Errors**: By organizing your thoughts first, you minimize the chance of errors when you eventually write the actual code.
- **Serves as a Guide**: Pseudocode can act like a "to-do list" when you're coding. You can gradually convert each step into actual code, making the programming process smoother.

## How to Write Pseudocode

When writing pseudocode:

1. Use simple, plain language.
2. Focus on the logical flow of the problem.
3. Break tasks into small, manageable steps.
4. Avoid worrying about the syntax of any programming language—just focus on the **steps** you need to take.

### Basic Structure of Pseudocode

- **Start with a goal**: What do you want the program to accomplish?
- **List the tasks**: Break down the steps required to reach the goal.
- **Use conditionals**: If needed, use "IF", "ELSE", and "WHILE" to represent decision-making points in your logic.

!!! Tip "Write it all out"
    Pseudocoding is an opportunity to externalize all the thoughts you have about approaching a problem. Think of it as a brainstorming tool - it is a low stakes environment where you can write out all your thoughts and ideas without worrying about the syntax of a programming language.

    Worried that something wont work? Who cares! When in doubt, just write it out. Then, when you're done, you can edit and refine your thoughts into a more coherent plan.
---

## A Situation: Describing Neighborhood Pets

Imagine you want to write code that would allow you to fluidly describe all the pets in your neighborhood. You want to collect information about each pet, such as their name, type, age, and - if they're a dog - whether they like *pats*.

1. Collect the pet’s **name**.
2. Note the **type** of pet (e.g., dog, cat, turtle).
3. Record the pet’s **age**.
4. If the pet is a dog, note if they like pats or not.

Think about how you'd approach this problem. Try writing pseudocode to outline the steps you'd take to collect and describe the pets in your neighborhood!

When you're done, look at the potential solution below. Note: there are many ways to approach this problem, and your pseudocode might look different from the example provided.

---

## Practice Writing Pseudocode

Here’s an example of how you might write pseudocode for the neighborhood pet description problem:

```
- Start
- For each pet in the neighborhood:
    - Get the pet's name
    - Get the type of pet
    - Get the pet's age
    - IF the pet is a dog:
        - Ask if the dog likes pats (being pet)
        - Record whether the dog likes pats
    - Record all the information for this pet
- Repeat for all pets
- End
```

---

## Refining Pseudocode

We can use Pseudocode as an opportunity to think out the structure of classes and methods we would use to solve the problem.

If we were to approach this problem using classes and object-oriented thinking, here’s how you could outline it in pseudocode:

```
- Define a class called Pet:
    - The class has the following attributes:
        - pet's name
        - type of pet (e.g., dog, cat)
        - pet's age
        - IF the pet is a dog:
            - an attribute to store whether the dog likes pats
    - Define a method called `display_info()` in the Pet class:
        - The method prints out all the pet's details, including whether a dog likes pats if applicable

- Create an empty list to store all the pets
- For each pet in the neighborhood:
    - Ask for the pet's name
    - Ask for the type of pet
    - Ask for the pet's age
    - IF the type of pet is a dog:
        - Ask if the dog likes pats
        - Store whether the dog likes pats
    - Create an instance of the Pet class with the collected information
    - Add the new pet to the list of pets
- After all pets have been recorded:
    - Loop through the list of pets and call `display_info()` on each pet to show their details
- End
```

!!! Tip "Buzz words to help you"
    Object oriented programming is filled with little terms that can help you structure your pseudocode. Here are a few to get you started:

    - **Class**: A blueprint for creating objects. Classes define the attributes and methods that objects will have.
    - **Instance**: An object created from a class. Each instance has its own unique data.
    - **Method**: A function defined inside a class that operates on the object's data.
    - **Attribute**: A variable that belongs to an object. Attributes store the object's state.
    
---

## Implementing Psuedocode

If you're feeling up to it, take the outline written above and use it to construct *properly functioning* Python code.

If you're struggling or finished trying, check out the implemented solution below:

??? Tip "Implementation"
    ```python
    # Define the Pet class
    class Pet:
        def __init__(self, name, pet_type, age, friendly=None):
            self.name = name
            self.pet_type = pet_type
            self.age = age
            self.friendly = friendly  # Only relevant for dogs

        def display_info(self):
            info = f"Name: {self.name}, Type: {self.pet_type}, Age: {self.age}"
            if self.pet_type == "dog":
                info += f", Friendly: {self.friendly}"
            print(info)

    # Create an empty list to store pets
    pets_list = []

    # Loop to collect information for each pet
    while True:
        name = input("Enter the pet's name (or 'stop' to finish): ")
        if name == 'stop':
            break
        pet_type = input("Enter the type of pet (e.g., dog, cat): ")
        age = input("Enter the pet's age: ")

        # If the pet is a dog, ask if it is friendly
        friendly = None
        if pet_type == "dog":
            friendly = input("Is the dog friendly? (yes/no): ")

        # Create a new Pet object
        pet = Pet(name, pet_type, age, friendly)
        pets_list.append(pet)

    # Display information about each pet
    for pet in pets_list:
        pet.display_info()
    ```

This code example shows how pseudocode can be converted into working Python code using classes and loops. The `Pet` class models the pets, while the main loop collects and stores data in an organized way. Once all the data is collected, we display the information for each pet.