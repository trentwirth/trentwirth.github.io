# Step 14

In Step 14, we will explore four of the most common data structures in Python: **Lists**, **Tuples**, **Dictionaries**, and **Sets**. These data structures are essential for organizing and storing data efficiently, and you will frequently encounter them in any kind of data analysis, especially in behavioral science research.

Let’s dive into each one and understand how to use them in Python!

---

## 1. Introduction to Python Data Structures

Python offers a variety of ways to store and organize data. Each structure has its own use cases and advantages. In this step, we will cover:

- **Lists**: Ordered, mutable collections of items.
- **Tuples**: Ordered, immutable collections of items.
- **Dictionaries**: Key-value pairs for efficient data lookup.
- **Sets**: Unordered collections of unique elements.

We’ll discuss each one in detail, provide code examples, and give you exercises to help solidify your understanding.

---

## 2. Working with Lists

### What Are Lists?

A **list** is an ordered collection of items (elements). Lists are **mutable**, which means that the elements can be changed after the list is created. You can add, remove, and modify elements in a list.

### Example: Creating and Modifying Lists

```python
# Creating a list of participants
participants = ["Alice", "Bob", "Charlie", "David"]

# Accessing elements in a list
print(participants[0])  # Output: Alice

# Modifying elements in a list
participants[1] = "Barbara"
print(participants)  # Output: ['Alice', 'Barbara', 'Charlie', 'David']

# Adding new elements to the list
participants.append("Eve")
print(participants)  # Output: ['Alice', 'Barbara', 'Charlie', 'David', 'Eve']

# Removing an element from the list
participants.remove("Charlie")
print(participants)  # Output: ['Alice', 'Barbara', 'David', 'Eve']
```

### List Methods

Here are a few useful methods you can use with lists:
- **`append()`**: Adds an element to the end of the list.
- **`remove()`**: Removes the first occurrence of an element from the list.
- **`sort()`**: Sorts the list in place.
- **`len()`**: Returns the length of the list.

### Exercise: Working with Lists
1. **Create a List**: Create a list of 5 favorite hobbies.
2. **Modify the List**: Add a new hobby to the list, then remove the second hobby from the list.
3. **Print and Sort**: Print the final list and sort it alphabetically.

---

## 3. Working with Tuples

### What Are Tuples?

A **tuple** is similar to a list, but it is **immutable**, meaning that once a tuple is created, its elements cannot be changed. Tuples are useful when you want to store a collection of items that should not be modified.

### Example: Creating and Accessing Tuples

```python
# Creating a tuple
coordinates = (10, 20)

# Accessing elements in a tuple
print(coordinates[0])  # Output: 10

# Tuples are immutable, so you cannot modify them
# The following line would raise an error:
# coordinates[0] = 15  # Uncommenting this will raise a TypeError

# You can create a tuple with a single element by adding a comma at the end
single_element_tuple = (42,)
print(single_element_tuple)  # Output: (42,)
```

!!! Tip "Tuple Syntax"
    Notice that Tuples are created using parentheses `()` and elements are separated by commas, where as Lists are created using square brackets `[]`. This distinction is important to remember when working with these data structures!

### When to Use Tuples

- Use a **tuple** when you have a collection of items that should not change.
- Tuples are often used to represent fixed collections, such as geographical coordinates or RGB color values.

### Exercise: Working with Tuples
1. **Create a Tuple**: Create a tuple that contains your birthdate (day, month, year).
2. **Access Elements**: Print the day, month, and year individually by accessing the tuple elements.
3. **Experiment**: Try modifying the tuple (and note why it doesn’t work).

---

## 4. Working with Dictionaries

### What Are Dictionaries?

A **dictionary** is a collection of **key-value pairs**. Each key is associated with a value, and you can use the key to quickly access the corresponding value. Dictionaries are **mutable**, so you can change the values associated with keys after the dictionary is created.

### Example: Creating and Using Dictionaries

```python
# Creating a dictionary to store survey responses
survey_responses = {
    "Alice": 5,
    "Bob": 7,
    "Charlie": 6
}

# Accessing a value by its key
print(survey_responses["Bob"])  # Output: 7

# Modifying a value
survey_responses["Bob"] = 8
print(survey_responses)  # Output: {'Alice': 5, 'Bob': 8, 'Charlie': 6}

# Adding a new key-value pair
survey_responses["David"] = 9
print(survey_responses)  # Output: {'Alice': 5, 'Bob': 8, 'Charlie': 6, 'David': 9}

# Removing a key-value pair
del survey_responses["Charlie"]
print(survey_responses)  # Output: {'Alice': 5, 'Bob': 8, 'David': 9}
```

### Dictionary Methods

- **`keys()`**: Returns a list of all keys in the dictionary.
- **`values()`**: Returns a list of all values in the dictionary.
- **`items()`**: Returns a list of key-value pairs (tuples).

#### Example: Using Dictionary Methods

```python
# Getting all keys in the dictionary
print(survey_responses.keys())  # Output: dict_keys(['Alice', 'Bob', 'David'])

# Getting all values in the dictionary
print(survey_responses.values())  # Output: dict_values([5, 8, 9])

# Getting key-value pairs as tuples
print(survey_responses.items())  # Output: dict_items([('Alice', 5), ('Bob', 8), ('David', 9)])
```

### Exercise: Working with Dictionaries
1. **Create a Dictionary**: Create a dictionary with the names of three friends and their favorite colors.
2. **Modify the Dictionary**: Change one friend's favorite color and add a new friend with their favorite color.
> Hint, use the [`update()` method (this is a clickable link)](https://www.w3schools.com/python/ref_dictionary_update.asp) to add a new key-value pair to the dictionary as well as to update an existing key-value pair.
3. **Print and Access**: Print the dictionary and access the favorite color of one of your friends.

---

## 5. Working with Sets

### What Are Sets?

A **set** is an unordered collection of **unique elements**. Sets are useful when you want to store items without duplicates and don't care about the order of the elements. Sets are **mutable**, but you cannot access elements by index like in lists.

> Online resource for sets can be found [here](https://www.w3schools.com/python/python_sets.asp)

### Example: Creating and Using Sets

```python
# Creating a set of participants
participants = {"Alice", "Bob", "Charlie", "David"}

# Adding a new element to the set
participants.add("Eve")
print(participants)  # Output: {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}

# Trying to add a duplicate element (it will have no effect)
participants.add("Alice")
print(participants)  # Output: {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}

# Removing an element from the set
participants.remove("David")
print(participants)  # Output: {'Alice', 'Bob', 'Charlie', 'Eve'}
```

### Set Operations

- **`add()`**: Adds an element to the set.
- **`remove()`**: Removes an element from the set.
- **`union()`**: Returns a new set containing all elements from two sets (without duplicates).
- **`intersection()`**: Returns a new set containing only elements found in both sets.

### Exercise: Working with Sets
1. **Create a Set**: Create a set of favorite fruits.
2. **Add Elements**: Add a new fruit to the set and attempt to add a duplicate fruit.
3. **Perform Set Operations**: Create a second set of fruits and find the **union** and **intersection** of the two sets.

---

## 6. Final Exercise: Working with Data Structures

Now that you’ve learned about lists, tuples, dictionaries, and sets, let's wrap up with a final exercise that brings these concepts together.

### Instructions:

1. **Create a Class System for Participants**:
    - Create a `Participant` class that stores the name, age, and favorite hobby of each participant.
    - Use a **list** to store a collection of `Participant` objects.

2. **Store Data in a Dictionary**:
    - Create a dictionary where the keys are participant names and the values are tuples containing their age and favorite hobby.

3. **Use a Set for Unique Hobbies**:
    - Extract all unique hobbies from the participants and store them in a **set**.

4. **Final Output**:
    - Print the list of participants.
    - Print the dictionary mapping names to participant details.
    - Print the set of unique hobbies.

!!! Tip "Practice for your Written Assessment"
    To practice for the written assessment, outline how you would solve this problem before you start your implementation. You can write out your solution on a piece of paper or in your text editor of choice (Google/Word Doc, etc.). Be as detailed as you can manage. Once you're done with this, then use your outline to implement the solution - how close were you? What did you forget? Answering these questions will help you prepare for the written assessment!

??? Tip "Potential Solution"

    ```python
    class Participant:
        def __init__(self, name, age, hobby):
            self.name = name
            self.age = age
            self.hobby = hobby

    # List to store participants
    participants = [
        Participant("Alice", 29, "Reading"),
        Participant("Bob", 34, "Cycling"),
        Participant("Charlie", 27, "Reading"),
        Participant("David", 31, "Swimming")
    ]

    # Dictionary to map participant names to their age and hobby
    participant_dict = {p.name: (p.age, p.hobby) for p in participants}
    print(participant_dict)
    ```

    ```python
    # Set to store unique hobbies
    unique_hobbies = {p.hobby for p in participants}
    print(unique_hobbies)
    
    #Expected Output:
    # {'Reading', 'Cycling', 'Swimming'}
    ```
    
---

## 7. Reflect and Review

In this step, we covered four essential Python data structures:

- **Lists**: Ordered, mutable collections of items, which are ideal for managing an ordered set of data that might need to be modified.
- **Tuples**: Ordered but immutable collections, useful for fixed data that should not be changed once defined.
- **Dictionaries**: Unordered collections of key-value pairs, which are excellent for mapping relationships, such as names to data.
- **Sets**: Unordered collections of unique items, great for ensuring no duplicates and for performing mathematical set operations such as unions and intersections.

### Why Are These Data Structures Important?

These data structures help organize, store, and access data efficiently in Python programs, especially in scenarios where datasets are large or need to be processed in various ways. Understanding the strengths and limitations of each type of data structure is crucial for writing effective and optimized Python code.

Think about how you might apply these structures in real-world projects:

- **Lists** for managing ordered collections like participant data or survey responses.
- **Tuples** for grouping related but unchangeable data, like coordinates or fixed settings.
- **Dictionaries** for looking up information quickly, such as mapping survey participants to their answers.
- **Sets** for managing collections where uniqueness is required, such as lists of unique hobbies or tags.

Having a strong grasp of Python’s core data structures will help you organize and manipulate data more effectively in future projects.

---