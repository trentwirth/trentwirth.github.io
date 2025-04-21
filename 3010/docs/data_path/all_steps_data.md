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

# Step 15

In Step 14, we introduced the four most common data structures in Python: **Lists**, **Tuples**, **Dictionaries**, and **Sets**. Now that you have a basic understanding of these structures, it's time to practice manipulating them. Data manipulation is essential in research and real-world projects, as it allows you to prepare, clean, and transform data for analysis.

### 1. Working with Lists

Lists are mutable, meaning you can change their elements after they've been created. Let’s explore some ways to manipulate lists.

#### Adding Elements

You can add new elements to a list using the `append()` and `insert()` methods.

```python
# Example: Append vs Insert
my_list = [1, 2, 3]
my_list.append(4)  # Adds 4 to the end
my_list.insert(1, "inserted")  # Inserts at index 1

print(my_list)
```

- **`append()`** adds the element to the **end** of the list.
- **`insert()`** allows you to add an element at a specific position in the list. The first argument is the **index** where you want to insert the element.

#### Removing Elements

To remove elements, you can use the `remove()` method or the `pop()` method.

- **`remove()`** deletes the first occurrence of a value.
- **`pop()`** removes an element by **index**, which means it removes the element at a specific position in the list, rather than searching for the value itself. Every item in a list has an index that represents its position in the list, starting with 0 for the first item.

For example, in the list `['apple', 'banana', 'cherry']`, 'apple' has index 0, 'banana' has index 1, and 'cherry' has index 2. If you use `pop(1)`, it will remove 'banana' because it's at index 1.

```python
# Example: Remove vs Pop
my_list.remove(2)  # Removes the first occurrence of 2
my_list.pop(1)  # Removes the element at index 1, which is "inserted"

print(my_list)
```

### 2. Working with Tuples

Tuples are immutable, meaning you cannot change their contents after creation. However, you can perform operations like slicing and **unpacking**.

#### Unpacking Tuples

"Unpacking" means assigning the elements of a tuple to individual variables. This allows you to break the tuple into its components and work with each one separately. For example:

```python
# Example: Tuple Unpacking
my_tuple = (10, 20, 30)
a, b, c = my_tuple  # Unpacks the values into a, b, c

print(a, b, c)
```

- In this example, the values 10, 20, and 30 are "unpacked" from the tuple and assigned to the variables `a`, `b`, and `c`. This technique is useful when you need to work with individual components of a tuple.

If the number of variables on the left doesn’t match the number of elements in the tuple, Python will raise an error.

### 3. Manipulating Dictionaries

Dictionaries allow you to store key-value pairs. You can add, update, and delete key-value pairs easily.

#### Adding and Updating Elements

You can add new key-value pairs or update existing ones by assigning a value to a key.

```python
# Example: Add and Update Dictionary
my_dict = {"name": "Alice", "age": 25}
my_dict["age"] = 26  # Update existing key
my_dict["city"] = "New York"  # Add new key-value pair

print(my_dict)
```

#### Removing Elements

To remove an element, use the `del` statement or the `pop()` method.

```python
# Example: Delete vs Pop
del my_dict["city"]  # Deletes the key-value pair for 'city'
my_dict.pop("age")  # Removes 'age' key and returns its value

print(my_dict)
```

#### Looping Through a Dictionary

You can loop through a dictionary to access its keys and values, allowing you to manipulate or analyze its data.

```python
# Example: Looping through a dictionary
my_dict = {"name": "Alice", "age": 26, "city": "New York"}

for key, value in my_dict.items():
    print(f"The key is {key} and the value is {value}")
```

- `my_dict.items()` returns each key-value pair as a tuple, and you can unpack it into `key` and `value` as shown in the example. This is useful for iterating over all the entries in a dictionary to access or modify the data.


### 4. Set Operations

Sets are unordered collections of unique elements. They support mathematical operations like **union**, **intersection**, and **difference**, which are helpful when comparing sets of data.

#### Adding and Removing Elements

```python
# Example: Add and Remove in Set
my_set = {1, 2, 3}
my_set.add(4)  # Adds 4 to the set
my_set.remove(2)  # Removes 2 from the set

print(my_set)
```

#### Set Operations: Union, Intersection, Difference

- **Union** combines all unique elements from two sets.
- **Intersection** returns only the elements that are present in both sets.
- **Difference** returns the elements that are in one set but not in the other.

```python
# Example: Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)  # Union of two sets
intersection_set = set1.intersection(set2)  # Intersection of two sets
difference_set = set1.difference(set2)  # Elements in set1 but not in set2

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
```

- **Union**: `{1, 2, 3}` and `{3, 4, 5}` together become `{1, 2, 3, 4, 5}` because all elements are included but duplicates are removed.
- **Intersection**: Only the number `3` appears in both sets, so the result is `{3}`.
- **Difference**: In the difference operation, the result is `{1, 2}` because these are the elements in `set1` that are not in `set2`.

### Exercises

1. **Create a list of your favorite fruits** and perform the following operations:
    - Add a new fruit to the end.
    - Insert a fruit at the second position.
    - Remove one fruit by its value.

    ??? Tip "Solution"
        ```python
        fruits = ["apple", "banana", "cherry"]
        fruits.append("orange")  # Add orange to the end
        fruits.insert(1, "grape")  # Insert grape at the second position
        fruits.remove("banana")  # Remove banana by value

        print(fruits)
        ```

2. **Create a dictionary** that contains the names of 3 countries and their capitals. Then:
    - Update the capital of one country.
    - Add a new country-capital pair.
    - Remove one country from the dictionary.

    ??? Tip "Solution"
        ```python
        capitals = {"France": "Paris", "Japan": "Tokyo", "USA": "Washington D.C."}
        capitals["USA"] = "Cincinnati"  # Update capital of USA
        capitals["Germany"] = "Berlin"  # Add new country-capital pair
        capitals.pop("USA")  # Remove USA from the dictionary

        print(capitals)
        ```

3. Create a tuple of 3-4 numbers. **Given a tuple of numbers**, unpack it into individual variables and print them.

    ??? Tip "Solution"
        ```python
        numbers = (100, 200, 300)
        x, y, z = numbers  # Unpack the tuple into x, y, z

        print(x, y, z)
        ```

4. **Create two sets of integers** and:
    - Perform union, intersection, and difference operations.

    ??? Tip "Solution"
        ```python
        set1 = {10, 20, 30, 40}
        set2 = {30, 40, 50, 60}

        union_set = set1.union(set2)  # Union
        intersection_set = set1.intersection(set2)  # Intersection
        difference_set = set1.difference(set2)  # Difference

        print("Union:", union_set)
        print("Intersection:", intersection_set)
        print("Difference:", difference_set)
        ```

# Step 16

## Introduction to Data Visualization

In this step, we'll start exploring **data visualization** using Python, specifically with the [`matplotlib` library](https://matplotlib.org/) and [`numpy`](https://numpy.org/) for data creation. Data visualization is an essential tool in data analysis—it allows you to better understand your data by uncovering patterns, trends, and outliers. In scientific research, visualizing data is especially valuable, helping to interpret experiment results, compare groups, and communicate findings effectively.

We'll cover a few essential plot types: **line plots**, **bar plots**, **histograms**, and **scatter plots**. These visualizations are foundational, and you’ll likely use them to analyze data in future projects.

### Getting Started: Setting Up Matplotlib and Numpy

To start, make sure you have `matplotlib` installed. If you haven’t installed it yet, you can install it by running:
```python
!pip install matplotlib
```
!!! Tip "The `!`"
    The `!` at the beginning of the command is used in Jupyter notebooks to things like installation commands - this will install matplotlib if it's not already installed.

Import `matplotlib` and `numpy` with the following aliases:
```python
import matplotlib.pyplot as plt
import numpy as np
```

### 1. Line Plot

#### Use Case
Line plots are great for visualizing changes over time or across experimental trials. Let’s start by creating a basic line plot with synthetic data.

#### Creating a Basic Line Plot
We’ll create an array of data points and visualize them:

```python
# Generate data
x = np.arange(0, 10, 1)  # x-axis: from 0 to 9
y = np.random.randint(1, 10, size=10)  # y-axis: random integers

# Create line plot
plt.plot(x, y, label="Random Data", color="blue", linestyle="--", marker="o")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Basic Line Plot")
plt.legend()
plt.show()
```

!!! Tip "Plots a as a Debugging Tool"
    Just like when you use a print statement, when you run `plt.show()`, you should see the plot appear in your notebook - this is great for instantaneous feedback.

    Think about how you can use this to debug your *data* - if you're not getting the results you expect, you can visualize your data to visually inspect it, and see if something's wrong. As scientists, we build up intuitions for the "shape" of our data, and visualizing it can help us understand what's going on.

#### Breaking it down:
- `plt.plot(x, y)`: This function creates a line plot with `x` on the x-axis and `y` on the y-axis.
- `plt.xlabel()`: Sets the label for the x-axis.
- `plt.ylabel()`: Sets the label for the y-axis.
- `plt.title()`: Sets the title of the plot.
- `plt.legend()`: Displays the legend on the plot.
- `plt.show()`: Displays the plot.

You can check out the `plot` documentation for matplotlib [here](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html).

#### Customizing the Line Plot
Try adjusting colors, line styles, and adding markers to make the plot more informative.

[Here is a web link to the named colors of matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html), it can be a lot of fun and very useful to experiment with different colors.

!!! Tip "Colors from Hex Codes"
    You can also use hex codes to specify colors in matplotlib. For example, `color="#FF5733"` would give you a specific shade of orange.

    Something that I personally love to do to find unique combinations of hex code colors is to use PokePalettes, a website that generates color palettes based on Pokemon. [Check it out here!](https://pokepalettes.com/)

    To replace a color in a plot with a hex code, you can use the following syntax:
    ```python
    plt.plot(x, y, color="#FF5733")
    ```

### 2. Bar Plot

#### Use Case
Bar plots are useful for comparing categorical data, like response counts across different participant groups.

#### Creating a Basic Bar Plot
Here, we’ll create a bar plot with categorical labels on the x-axis:

```python
# Data
categories = ["Group A", "Group B", "Group C"]
values = [15, 35, 25]

# Create bar plot
plt.bar(categories, values, color="green")
plt.xlabel("Groups")
plt.ylabel("Values")
plt.title("Bar Plot of Categorical Data")
plt.show()
```

You can see the `bar` documentation for matplotlib [here](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html).

#### Customizing the Bar Plot
Experiment with changing colors, adjusting bar width, and adding values on top of each bar to emphasize comparisons.

!!! Tip "Fun Example"
    You can change the way the bars are displayed, their orientation, and other properties. For example, you can create a horizontal bar plot by using `plt.barh()` instead of `plt.bar()`.

    ```python
    plt.barh(categories, values, color="green")
    ```

### 3. Histogram

#### Use Case
Histograms are ideal for visualizing the distribution of a dataset, such as reaction times or score distributions.

#### Creating a Basic Histogram
Using Numpy, we’ll generate a normal distribution and plot it as a histogram.

```python
# Generate data with a normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)

# Create histogram
plt.hist(data, bins=30, color="purple", edgecolor="black")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Normally Distributed Data")
plt.show()
```

#### Importance of Bin Size
Histograms are great data visualization tools, but it's important to understand how the bin size can be adjusted to change the level of detail in the plot, sometimes altering the interpretation of the data.

You can adjust the number of bins by changing the `bins` parameter in the `hist()` function. Functionally, the number of bins determines the number of intervals (or groups) the data is divided into, the more bins, the more detailed the histogram.

### Customizing the Histogram
Experiment with changing colors, adjusting the number of bins, and adding labels to make the histogram more informative.

### 4. Scatter Plot

#### Use Case
Scatter plots are useful for showing relationships between two continuous variables, like age and reaction time.

#### Creating a Basic Scatter Plot
Here, we’ll create two correlated datasets and plot them against each other.

```python
# Generate data
x = np.random.rand(100)
y = x * 2 + np.random.normal(0, 0.1, 100)

# Create scatter plot
plt.scatter(x, y, color="red", s=20, label="Data Points")
plt.xlabel("X Variable")
plt.ylabel("Y Variable")
plt.title("Scatter Plot Example")
plt.legend()
plt.show()
```

#### Customizing the Scatter Plot
Change point size, colors, and add legends to enhance interpretability.

!!! Tip "Fun Example"
    You can change the shape of the markers in a scatter plot. For example, you can use triangles instead of circles by specifying `marker="^"`.

    ```python
    plt.scatter(x, y, color="red", s=20, label="Data Points", marker="^")
    ```

    This is particularly useful when you have multiple datasets on the same plot and want to differentiate them.

### 5. Combining Multiple Plots in a Single Figure

#### Use Case
Sometimes, it’s useful to compare multiple visualizations side-by-side. Using subplots, you can arrange multiple plots in one figure.

#### Creating Subplots
Below is an example of creating a line plot and a histogram in a 1x2 grid layout.

```python
# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Scatter Plot
axes[0].scatter(x, y, color="blue", label="Scatter Plot")
axes[0].set_title("Scatter Plot")
axes[0].set_xlabel("X-axis")
axes[0].set_ylabel("Y-axis")
axes[0].legend()

# Histogram
axes[1].hist(data, bins=20, color="orange", edgecolor="black")
axes[1].set_title("Histogram")
axes[1].set_xlabel("Value")
axes[1].set_ylabel("Frequency")

# Adjust layout
plt.tight_layout()
plt.show()
```

Notice how `axes[0]` and `axes[1]` are used to access the individual subplots. This allows you to customize each subplot independently.

## A quick note on the importance of clear labels

When creating visualizations, it's crucial to provide clear labels for the axes, titles, and legends. These labels help viewers understand the data being presented and the context of the visualization. Always ensure that your visualizations are labeled appropriately to convey the intended message effectively.

Your goal should be for the plot to make sense independent of the context; such that if you were to show a data visualization depicting the relationship between age and reaction time, someone who had never seen the data before could understand what the plot is showing by reading the labels, axes, and title.

## Coding Exercise: Custom Visualizations

In this exercise, you’ll work with a dataset generated using `numpy`. Your goal is to explore different ways to visualize this data and think about what insights each visualization type can reveal. You’ll create at least **two different visualizations** of the dataset, using different plot types.

### A. Generate the Data

Run the code below to generate a synthetic (fake) dataset. This dataset simulates reaction times and accuracy scores from a fictional psychology experiment with 200 participants.

```python
import numpy as np

# Setting random seed for reproducibility
np.random.seed(42)

# Generate participant IDs (1 through 200)
participant_ids = np.arange(1, 201)

# Generate random reaction times (in milliseconds) with a mean of 500 ms and std deviation of 50 ms
reaction_times = np.random.normal(loc=500, scale=50, size=200)

# Generate random accuracy scores (out of 100) with a mean of 75 and std deviation of 10
accuracy_scores = np.random.normal(loc=75, scale=10, size=200)

# Print first few values for each array
print("Participant IDs:", participant_ids[:5])
print("Reaction Times:", reaction_times[:5])
print("Accuracy Scores:", accuracy_scores[:5])
```

### B. Review your data visualization options

1. **Line Plot**: Consider visualizing reaction times across participants to see how response times vary.
2. **Histogram**: A histogram of reaction times or accuracy scores can help show the distribution of these values.
3. **Scatter Plot**: A scatter plot of accuracy vs. reaction time can show any correlation between speed and accuracy.
4. **Bar Plot**: You could create a bar plot of average reaction times or accuracy for groups of participants (e.g., participants 1–50, 51–100).

### C. Create Your Visualizations

Using `matplotlib`, create at least **two different visualizations** of the data. Use the examples above or come up with your own! Think about:
- What insights does each plot type reveal?
- How can you customize your plots to make them more informative?

??? Tip "Example Starter Code"
    Below is an example of how you might start with a histogram. Remember to create your own additional plot(s) and customize as needed!

    ```python
    import matplotlib.pyplot as plt

    # Example Histogram for Reaction Times
    plt.hist(reaction_times, bins=20, color="skyblue", edgecolor="black")
    plt.xlabel("Reaction Time (ms)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Reaction Times")
    plt.show()

    # Continue with your own visualizations!
    ```

### D. Reflect

After creating your visualizations, reflect on the following:
- What insights did each visualization reveal about the data?
- Which visualization do you think was most effective, and​⬤

## Review

In this step, you learned:
- How to create and customize **line plots**, **bar plots**, **histograms**, and **scatter plots**.
- Basic customization techniques to make plots more readable and informative.
- How to use **subplots** to compare multiple visualizations side-by-side.

Data visualization is a powerful skill that will help you analyze and interpret data effectively in your research and academic work.

# Step 17

## Interactive Data Visualization with ipywidgets

In this step, we’ll enhance our data visualizations by adding **interactivity** using the `ipywidgets` library. `ipywidgets` allows us to add interactive controls, such as sliders and dropdowns, that let you modify visualization parameters in real-time.

### Why Use ipywidgets?

Interactive visualizations are especially useful for exploring data dynamically. Rather than generating a new plot for every change, you can use widgets to modify aspects of the plot—like adjusting data ranges, selecting data subsets, or changing visual elements—right from the notebook.

!!! Tip "Note - only for Notebooks!"
    `ipywidgets` is designed for use in Jupyter notebooks like Google Colab and VSCode. If you want to develop interactive visualizations for web applications, you might consider using libraries `Plotly`.

### Getting Started with ipywidgets

To start, make sure `ipywidgets` is installed. You can install it by running:
```python
!pip install ipywidgets
```

Then, import the widgets and display functionality:
```python
import ipywidgets as widgets
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np
```

### 1. Basic Interactive Plot with a Slider

To introduce `ipywidgets`, let’s create an interactive line plot using a slider. This slider will control the number of data points displayed in the plot.

#### Creating Interactive Line Plot

We’ll generate data with `numpy` and then use the `interact` function to link a slider to the number of data points.

```python
# Generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Define plot function
def plot_sine(num_points):
    plt.plot(x[:num_points], y[:num_points], color="blue")
    plt.xlabel("X-axis")
    plt.ylabel("Sine of X")
    plt.title(f"Sine Wave with {num_points} Points")
    plt.show()

# Create slider with interact
interact(plot_sine, 
         num_points=widgets.IntSlider(min=10, 
                                      max=100, 
                                      step=10, 
                                      value=50))
```

#### Explanation
The `plot_sine` function generates the plot, and the `interact` function links the `num_points` argument to the slider widget. Now, try moving the slider to see how it affects the plot!

### 2. Creating Interactive Scatter Plots with Dropdowns

Next, we’ll add more complexity by allowing users to choose between different datasets. For example, this could be useful for comparing the relationship between different experimental variables.

#### Generate Sample Data

We’ll create two sets of data for our scatter plot: a **linear** relationship and a **quadratic** relationship.

```python
# Sample data for two relationships
x_data = np.linspace(0, 10, 100)
linear_y = 2 * x_data + np.random.normal(0, 1, 100)  # Linear relationship
quadratic_y = x_data**2 + np.random.normal(0, 5, 100)  # Quadratic relationship

# Define plot function
def plot_scatter(relation_type):
    plt.scatter(x_data, linear_y if relation_type == "Linear" else quadratic_y, color="red", s=20)
    plt.xlabel("X Variable")
    plt.ylabel("Y Variable")
    plt.title(f"{relation_type} Relationship")
    plt.show()

# Create dropdown with interact
interact(plot_scatter, relation_type=widgets.Dropdown(options=["Linear", "Quadratic"], value="Linear", description="Relationship Type"))
```

#### Explanation
The `plot_scatter` function adjusts the `y` values depending on the chosen relationship type. The dropdown menu lets users choose between the linear and quadratic datasets, updating the plot accordingly.

### 3. Combining Multiple Widgets: Slider and Dropdown

Now, let’s create an interactive histogram where users can:
- Adjust the number of bins with a slider.
- Select the dataset to visualize with a dropdown.

#### Creating Data and Function

We’ll generate two datasets: one with a **normal distribution** and one with a **uniform distribution**.

```python
# Sample datasets
normal_data = np.random.normal(0, 1, 1000)
uniform_data = np.random.uniform(-3, 3, 1000)

# Define histogram plot function
def plot_histogram(dist_type, bins):
    data = normal_data if dist_type == "Normal" else uniform_data
    plt.hist(data, bins=bins, color="green", edgecolor="black")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title(f"{dist_type} Distribution with {bins} Bins")
    plt.show()

# Create interactive widgets
interact(plot_histogram, 
         dist_type=widgets.Dropdown(options=["Normal", "Uniform"], value="Normal", description="Distribution"),
         bins=widgets.IntSlider(min=5, max=50, step=5, value=20))
```

#### Explanation
This function combines a dropdown (for dataset selection) and a slider (for number of bins) to create a more interactive histogram, allowing users to explore both distribution shapes and bin adjustments.

### Reflect and Practice

After experimenting with the examples above, create your own interactive visualization:

1. **Choose a dataset**: Use `numpy` to generate a dataset (or modify one of the provided datasets, you can even use the data from `Step 16`).
2. **Select a widget**: Decide which widget(s) would be useful to control the data or visualization.
3. **Customize**: Modify the appearance or functionality to make the visualization more insightful.

### Review

In this step, you learned:
- How to create interactive plots using `ipywidgets`.
- Basic widgets, like sliders and dropdowns, to control plot parameters.
- How to combine multiple widgets to create rich, interactive visualizations.

Adding interactivity to data visualization lets you explore data more deeply, helping you to uncover trends and patterns more easily. You can apply these techniques to create interactive visualizations for research and data exploration, making it easier to gain insights from your data.

# Step 18: Conducting Experiments Online and Basic Web Development

Up until this point, our course has focused on learning Python. While Python absolutely could be used to build an online research study, as we will see in this Step of the learning path, there are tools better suited to conducting online research.

In this step, we will explore how behavioral science experiments can be conducted on the web. We’ll look at a few web technologies that make this possible, such as `jsPsych`, HTML, CSS, and JavaScript, and provide you with code examples you can try out. We will also introduce tools that allow for online research without requiring any coding (Google Forms).

> Note: This step is meant to conceptually introduce you to a different programming language, specifically JavaScript and web development lanugages (HTML and CSS). We will take a slightly deeper dive into JavaScript in Step 20 when we look at `jsPsych`!

---

## 1. Experiments on the Web

Conducting experiments online allows researchers to reach a broader audience and collect data efficiently. While programming tools like `PsychoPy` (Python) can be used to design experiments, another accessible tool, **`jsPsych`**, simplifies the process of running experiments directly in a web browser.

### What is `jsPsych`?

`jsPsych` is a JavaScript library specifically designed for creating experiments that participants can complete online. It’s flexible, widely used in psychology research, and makes it easier to control and collect data from web-based studies.

### What is JavaScript?

**JavaScript** is a programming language used to create interactive elements on web pages. It’s essential for building dynamic websites and web applications. JavaScript can handle user interactions, animations, and data processing in real-time. 

Have you ever noticed a button change color on a website, or text appear when you hover over an image? These are examples of JavaScript in action!

JavaScript is incredibly versitile for all things on the web, and can be used to create interactive elements, animations, and more. One of my favorite uses of JavaScript is called "ThreeJS" which is a library that allows you to create 3D graphics in the browser! You can check out some examples [here](https://threejs.org/).

---

## 2. Basics of Web Development: HTML, CSS, and JavaScript

To understand how `jsPsych` functions, we’ll cover some core components of web development. Below, we’ll explore HTML, CSS, and JavaScript and provide examples you can try in **VSCode**.

??? Tip "Web Development?"
    Web development can be defined as the process of building websites and web applications. It involves writing code in languages like HTML, CSS, and JavaScript to create interactive and visually appealing web pages. These technologies work together to structure content, style elements, and add interactivity to web pages.

### 2.1. Install Live Server in VSCode

   In the Extensions sidebar, search for **Live Server** and install it. We'll use this extension to run our HTML files in a live server.

---

### 2.2. HTML (HyperText Markup Language)

HTML is the standard language for creating web pages. It allows you to structure content using "tags." A "tag" is a keyword surrounded by angle brackets, like `<tag>`. Tags are used to define elements such as headings, paragraphs, images, and links. A sample of a common tag is `<h1>`, which defines a top-level heading. To close a tag, use a forward slash, like `</h1>`.


Here’s a basic HTML structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Experiment</title>
</head>
<body>
    <h1>Welcome to My Experiment!</h1>
    <p>This is an experiment example using HTML, CSS, and JavaScript.</p>
</body>
</html>
```

> Notice the tags like `<html>`, `<head>`, `<title>`, `<body>`, `<h1>`, and `<p>`. These tags structure the content and define the appearance of the webpage. `<h1>` is a top-level heading, and `<p>` is a paragraph.

This code creates a basic webpage with a title and heading. Copy and paste this code into a new file with an `.html` extension, calling the file `index.html`.

You can open this file in VSCode and use the **Live Server** extension to view it in your browser. To do so, right-click on the HTML file and select **Open with Live Server**.

This will open up a new tab in your browser displaying the HTML content!

---

### 2.3. CSS (Cascading Style Sheets)

CSS styles your HTML content, making it look visually appealing. You can add color, align elements, and much more.

Add the following CSS to your HTML file within a `<style>` tag in the `<head>` section:

```html
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f8ff;
        text-align: center;
    }
    h1 {
        color: #4682b4;
    }
    p {
        color: #2f4f4f;
    }
</style>
```

??? Tip "The full HTML file should now look like this:"
    ```html
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Web Experiment</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                text-align: center;
            }
            h1 {
                color: #4682b4;
            }
            p {
                color: #2f4f4f;
            }
        </style>
        
    </head>
    <body>
        <h1>Welcome to My Experiment!</h1>
        <p>This is an experiment example using HTML, CSS, and JavaScript.</p>
    </body>

    </html>
    ```

This CSS changes the background color, centers the text, and applies colors to the heading and paragraph.

---

### 2.4. JavaScript

JavaScript adds interactivity to your webpage, such as reacting to user inputs or displaying alerts.

Include this script inside your HTML file’s `<body>` or `<head>` tags:

```html
<script>
    function showAlert() {
        alert("Welcome to the experiment!");
    }
</script>

<button onclick="showAlert()">Click Me</button>
```

This code adds a button that, when clicked, shows an alert message.


??? Tip "Your full HTML file should now look like this:"
    ```html
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Web Experiment</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                text-align: center;
            }
            h1 {
                color: #4682b4;
            }
            p {
                color: #2f4f4f;
            }
        </style>

        <script>
            function showAlert() {
                alert("Welcome to the experiment!");
            }
        </script>

        <button onclick="showAlert()">Click Me</button>


    </head>
    <body>
        <h1>Welcome to My Experiment!</h1>
        <p>This is an experiment example using HTML, CSS, and JavaScript.</p>
    </body>

    </html>
    ```

---

## 3. Play with Web Development Tools

Now that you've seen the basics of HTML, CSS, and JavaScript, let’s practice combining them to create a simple interactive page.

*Try out the coding exercise below to experiment with web development tools.*

#### 3.1 **Create an HTML file** in VSCode and add the following code:
  
   - This code has HTML, CSS, and JavaScript sections, all within the same file.
   - Run the code using **Live Server** to see the results immediately in your browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Web Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f3f3f3;
            text-align: center;
        }
        h1 {
            color: #4CAF50;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Play with Web Development!</h1>
    <p>Click the button to see a message.</p>
    <button onclick="displayMessage()">Click Me!</button>
    <p id="message"></p>

    <script>
        function displayMessage() {
            document.getElementById("message").innerHTML = "Hello, you're interacting with JavaScript!";
        }
    </script>
</body>
</html>
```


#### 3.2 **Experiment** by changing the following elements:

   - **CSS Colors**: Adjust colors in the CSS styles for `h1`, `body`, or `button`.
   - **Message Text**: Modify the message text in the JavaScript function `displayMessage()`.

This gives you a chance to experiment with the main elements of web development in one file. By changing CSS properties, HTML structure, and JavaScript functions, you’ll start to see how these tools work together.

!!! Tip "`jsPsych` in Step 20"
    When we get to Step 20, we'll take a look of `jsPsych` - but this is a good enough intro for now!

---

## 4. Using Non-Programming Tools for Online Research

For researchers who prefer not to code, tools like **Google Forms** are useful for creating and distributing online surveys. These tools are widely used in psychological and behavioral research to gather self-report data or feedback from participants.

### Designing Effective User Surveys

A **user survey** is a structured way of gathering data about participants' thoughts, behaviors, or experiences. Well-designed surveys can reveal valuable insights into how people feel or think about a topic.

To learn more about designing surveys, visit [How to Design a UX Research Survey](https://dscout.com/people-nerds/how-to-design-a-ux-research-survey), which covers practical tips and best practices for creating effective surveys.

---

## Summary

- **HTML, CSS, and JavaScript** allow us to create and style web-based experiments.
- **Playing with web development tools** helps you learn through hands-on practice, experimenting with colors, structure, and interactivity.
- **Google Forms** and other no-code tools provide options for collecting data without needing to write code.
- **Survey design** is crucial in psychology and UX research to capture reliable and meaningful data from participants.

This step gives you the tools to start exploring web-based research and consider how online experiments can expand your reach and capabilities in behavioral science research.


# Step 19

In this step, we’ll explore **Pandas**, a powerful Python library for data manipulation and analysis. Pandas provides tools to explore, manipulate, and analyze datasets efficiently, which is essential for behavioral scientists working with real-world data.

We’ll use a CSV file named `happiness correlation data-2.csv`, which you can download below. Each row represents data from one participant, with columns capturing various aspects like age, work hours, GPA, life satisfaction, and more.

## 0. Download the Dataset

[Click this link to donload the data](<files/happiness correlation data-2.csv>)

!!! Tip "Familiar?"
    This data was pulled from Stats 2002, a course at UC. If this data is familiar, it's probably because you've seen this before!

**IMPORTANT**: Make sure to place the downloaded CSV file in the same directory as your notebook or script!

## 1. Getting Started with Pandas

### Installing and Importing Pandas
To use Pandas, ensure it’s installed in your Python environment. You can install it by running:

```python
!pip install pandas
```

!!! Tip "`%pip install`"
    If the code above doesn't work, try using `%pip install` instead of `!pip install`.

Then, import Pandas at the beginning of your notebook or script:

```python
import pandas as pd
```

### Loading the Data
Load the CSV file into a DataFrame, which is Pandas’ primary data structure for handling data tables.

```python
# Load the data from the your directory
file_path = 'happiness correlation data-2.csv'
df = pd.read_csv(file_path)
```

### Viewing the Data
Use `head()` to see the first few rows and get a feel for the structure.

```python
df.head()
```

---

## 2. Exploring the Dataset

This dataset has columns capturing the following participant information:

- **age**: Participant's age
- **hours_work_week**: Hours worked per week
- **gpa**: Participant's GPA
- **life_satisfaction**: Self-reported life satisfaction score
- **desire_to_achieve**: Self-reported desire to achieve
- **number_drinks**: Number of alcoholic drinks consumed per week
- **stress**: Self-reported stress level

### Basic Data Information

To get a quick summary of the dataset, including column names, data types, and any missing values:

```python
df.info()
```

To get basic descriptive statistics (mean, median, etc.) for each column:

```python
df.describe()
```

---

## 3. Analyzing Specific Columns

### Calculating the Mean Age of Participants
Let’s calculate the average age of participants.

```python
mean_age = df['age'].mean()
print("Average Age:", mean_age)
```

### Distribution of Life Satisfaction Scores
To understand the distribution of `life_satisfaction` scores, we can use Pandas to plot a histogram (requires `matplotlib` library).

```python
import matplotlib.pyplot as plt

df['life_satisfaction'].plot(kind='hist', title='Life Satisfaction Distribution')
plt.xlabel('Life Satisfaction')
plt.show()
```

### Exploring Correlations
We may want to see how different variables relate to each other. For example, are work hours correlated with stress?

```python
correlation = df[['hours_work_week', 'stress']].corr()
print("Correlation between hours worked and stress:\n", correlation)
```

### Grouping Data
We can group data to find insights, such as average Stress level by different levels of `desire_to_achieve`.

```python
avg_stress_by_achievement = df.groupby('desire_to_achieve')['stress'].mean()
print("Stress by Desire to Achieve:\n", avg_stress_by_achievement)
```

---

## 4. Data Cleaning and Manipulation

### Calculating Letter Grades
Add a new column to the dataset that calculates the letter grade for each student's GPA:

```python
def calculate_letter_grade(gpa):
    if gpa >= 3.7:
        return 'A'
    elif gpa >= 3.0:
        return 'B'
    elif gpa >= 2.0:
        return 'C'
    elif gpa >= 1.0:
        return 'D'
    else:
        return 'F'

df['letter_grade'] = df['gpa'].apply(calculate_letter_grade)
```

### Create a Bar Graph of Letter Grades 

To visualize the distribution of letter grades, we can create a bar graph:

```python
grade_counts = df['letter_grade'].value_counts()
grade_counts.plot(kind='bar', title='Letter Grade Distribution')
plt.xlabel('Letter Grade')
plt.ylabel('Count')
plt.show()
```

---

## 5. Saving Processed Data

After adding a new column, it’s often useful to save the processed dataset. Here’s how to save it to a new CSV file:

```python
df.to_csv('letter_grades_added_happiness_data.csv', index=False)
```

---

## Summary

In this step, you learned:

- **Loading** a CSV file into a Pandas DataFrame
- **Exploring** the data using basic summary and statistical methods
- **Analyzing** specific columns and relationships between them
- **Cleaning** data by handling missing values
- **Saving** processed data to a new CSV file

Pandas is a powerful tool for data analysis in Python, allowing you to work with datasets efficiently and discover meaningful insights.

# Step 20

In this step, we’ll break down the components of the `reaction-time.html` file used to create a reaction time experiment that you will participate in for class! Then in step 21, we'll use Pandas to analyze the data we collect.

The reaction time experiment is implemented in JavaScript using the [jsPsych library](https://www.jspsych.org/), designed to help researchers conduct behavioral science experiments in a web browser.

[Click this link to download the `reaction-time.html` file](<files/reaction-time.html>){:download="reaction-time.html"}

In order to read this file, you'll want to move it to a folder in VSCode, and open it there.

Throughout this step, **I don't expect you to be learning JavaScript or jsPsych**. Instead, I want you to see how the principles you've learned in Python programming apply to other languages and tools. By examining the experiment’s structure and components, you’ll see how programming concepts you’ve learned in Python are used in a different context.

We'll also need to cover some basic concepts of experimental design, we'll do that before we dive into the code.

## General Principles of Experimental Design

Let's take a moment to recall (or learn for the first time!) the concepts of the Independent Variable and Dependent Variables in an experiment.

### Independent Variable (IV)

The indepdent variable in the experiment is the thing that is being man**I**pulated - I personally remember this by thinking of the "I" in IV. In the reaction time experiement, the independent variable is the color of the circle that is displayed, which requires a specific key press response from the participant depending on the color of the circle.

### Dependent Variable (DV)

The dependent variable in the experiment is the thing that is being measured - in other words, the thing that *depends* on the manipulated (independent variable). In the reaction time experiment, the dependent variable is the time it takes for the participant to press the correct key after the circle is displayed.

### Control Variables

Control variables are variables that are kept constant throughout the experiment. In the reaction time experiment, the control variables include the size of the circle, the position of the circle on the screen, and the key press that is required for each color.

### Data Collection

When programming an experiment, it's critical to think about how you're collecting your data. We'll look at how the data is collected in the reaction time experiment in the code breakdown.

### Random and Blocked Designs

In the reaction time experiment, there are two different trial types, trials where the circle is blue and trials where the circle is orange. These trials are presented in randomized order, which is a common design in psychology experiments to prevent participants from anticipating the next stimulus.

If you wanted to understand how color similarity might make people respond more slowly, you could have an additional "block" of trials within the experiment where blue and - let's say, a blue-ish purple - are presented as competing colors. This would allow you to examine the difference in reaction time between the two color pairs of blue and purple, and blue and orange.

## Jumping into the JavaScript

> Important code blocks will be highlighted in the following sections, but feel free to explore the entire file! If you want to know how the entire code block works, you give the file to ChatGPT or Copilot and ask the chatbot to explain it to you!

Many of the decisions for the experiment are made *outside* of the code. For example, in this experiment, the colors were chosen to be blue and orange. While we will load images into the experiment to show these colors to the participant when we want to display them, the actual color of the circle is not defined in the code. This is a design decision that was made before the experiment was programmed.

Similarly, it's not written into the code that the color is the IV, and that reaction time is the DV. These are concepts that are understood by the researcher before the experiment is programmed.

Now we'll dive into the pieces of the code that make the experiment run.

### Test Procedure

Below is a block of code within the `JavaScript` called "`test_procedure`", let's break it down:

```javascript
var test_procedure = {
  timeline: [fixation, test],
  timeline_variables: test_stimuli,
  repetitions: 25,
  randomize_order: true
};
```

- `timeline`
    - The `timeline` parameter is an array of objects that represent the sequence of events in the experiment. Here, the `test_procedure` consists of two components: `fixation` and `test`. The `fixation` object displays a fixation cross, while the `test` object presents the colored circle for the participant to respond to.
- `timeline_variables`
    - The `timeline_variables` parameter specifies the stimuli to be used in the experiment. In this case, `test_stimuli` is an array of objects containing the *color of the circle* and the correct response key for each trial.
- `repetitions`
    - The `repetitions` parameter determines how many times the `test_procedure` is repeated. With 25 repetitions, it tells the experiment to show the orange and blue circles 25 times each, meaning that there will be 50 trials in total.
- `randomize_order`
    - The `randomize_order` parameter specifies whether the order of trials should be randomized. When set to `true`, the order of trials is randomized to prevent participants from anticipating the next stimulus.

### Loading Images

This experiment uses two images, preloaded at the start to prevent delays during trials. Preloading is crucial when images need to display instantly. Other designs, like experiments requiring many images or complex visuals, may benefit from a more dynamic image-loading approach.

```javascript
var preload = {
  type: jsPsychPreload,
  images: ['images/blue.png', 'images/orange.png']
};
timeline.push(preload);
```

In simpler terms, this code gets the images ready to be shown at a moment's notice. The `jsPsychPreload` function is used to preload the images, ensuring they are ready for display when needed.

### Data Storage and CSV Export

Data in this experiment is stored in memory by jsPsych, including response accuracy and reaction times. At the experiment’s end, participants see a summary with accuracy and average reaction time. The `jsPsych.data.get().csv()` method then generates a CSV file of the collected data, downloadable via a button.

```javascript
var jsPsych = initJsPsych({
  on_finish: function() {
    jsPsych.data.displayData();
    document.getElementById('download-csv').style.display = 'block';
    document.getElementById('download-csv').onclick = function() {
      var csv = jsPsych.data.get().csv();
      var blob = new Blob([csv], { type: 'text/csv' });
      var url = window.URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'reaction_time_data.csv';
      a.click();
      window.URL.revokeObjectURL(url);
    };
  }
});
```

Let's break down the significant parts of the code block above:

- `jsPsych.data.displayData()`
    - This function displays the data collected during the experiment, showing participants their accuracy and average reaction time.
- `var csv = jsPsych.data.get().csv();`
    - This line generates a CSV file containing the data collected during the experiment.
- `var blob = new Blob([csv], { type: 'text/csv' });`
    - This code block creates a Blob object, which is a file-like object of raw data. In this case, it's a CSV file. A "Blob" is a way to store data that can be downloaded as a file.
- `a.download = 'reaction_time_data.csv';`
    - This line sets the `download` attribute of the anchor element to the desired filename for the downloaded CSV file. This allows the participant to download the data as a CSV file named `reaction_time_data.csv`.

## Connecting JavaScript and jsPsych to Python Principles

This experiment may be in JavaScript, but it uses many programming concepts you've learned in Python, let's think through them:

- **Functions and Initialization**: The function `initJsPsych()` initializes the experiment, just as you've used Python functions to set up programs and prepare data structures.
- **Control Structures (Loops and Conditions)**: The timeline configuration is structured similarly to Python dictionaries and lists. jsPsych uses objects to store multiple settings (analogous to Python’s dictionaries). Loops and conditional logic, like `randomize_order: true`, create flexible procedures, just as you’ve seen in Python loops and conditionals.
- **Trial Data Collection**: The way trial data is collected and stored in `jsPsych.data.get()` is similar to Python data management libraries (like `Pandas`), where you collect, process, and export data. Here, we export as CSV, a format you’ve worked with for storing and analyzing data in Python.
- **Parameter Setting and Modularity**: Each `timeline` component is modular and configured with specific parameters, similar to defining functions with arguments in Python. This modularity in design is essential for scalability and reusability in behavioral science programming.

In summary, although this experiment is in JavaScript, it reinforces core programming concepts: initializing structures, using loops and conditions to control flow, collecting data, and organizing code modularly. 

These are skills you’ll carry into any programming language, allowing you to adapt tools like jsPsych confidently for experimental design.

## Looking for more?

Check out the jsPSych documentation website to learn more about how to use jsPsych for your own experiments: [https://www.jspsych.org/](https://www.jspsych.org/). 

# Step 21

In this step, we will process and visualize the reaction time data we collected in `Step 20` using Pandas! We will get this data from a zip file containing many `.csv` files, where each file contains data from a participant in a reaction time experiment. 

You will learn to:

1. Load a zip file of data into Python.
2. Extract and load all `.csv` files into a single pandas DataFrame.
3. Clean the data to isolate relevant variables. Visualize "raw" reaction time data.
4. Aggregate data by participant and analyze mean reaction times.
5. Visualize aggregated data.

## 0: Download the Zip File

> What's a Zip File? A zip file is a compressed folder that contains one or more files. It's a common way to package and share multiple files together.

[Click here to download the reaction time `.zip` file](files/reaction_time_data.zip)



## 1: Load and Unzip the Data

To begin, ensure you have downloaded the zip file. You can unzip it manually or programmatically within Python. Here’s how to do it in Python:

```python
import zipfile
import os

# Define file paths
zip_path = 'reaction_time_data.zip' # If you've put your file in the same directory as the notebook you're working in, your path is just the file name. If not, you'll need to include the path to the file.
extract_path = '.' # This will extract the files to the current directory

# Unzip the file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
```

After running this code, you should see the extracted `.csv` files in the specified directory - this will be a lot of files!

## 2: Load CSV Files into a Pandas DataFrame

With the files extracted, we can load each `.csv` file into a DataFrame. Each row in the final DataFrame will represent a trial, with columns for relevant data.

```python
import pandas as pd
import glob
import os

# Path to the directory containing extracted .csv files
csv_files = glob.glob(os.path.join(extract_path, '*.csv'))

# Initialize an empty list to store DataFrames
dfs = []

# Loop through and read each csv file
for idx, file in enumerate(csv_files):
    data = pd.read_csv(file)

    # Extract relevant rows and columns
    # Filter rows where 'trial_type' is 'response' (indicating a reaction time trial)
    data = data[data['trial_type'] == 'image-keyboard-response']

    # Select and rename relevant columns
    df = data[['rt', 'stimulus', 'response', 'correct']].copy()
    df.rename(columns={
        'rt': 'reaction_time',
        'stimulus': 'circle_color',
        'response': 'key_pressed',
        'correct': 'accuracy'
    }, inplace=True)

    # Clean up 'circle_color' to extract only color names
    df['circle_color'] = df['circle_color'].str.extract(r'images/(\w+).png')[0]

    # Add subject_id column
    df['subject_id'] = idx + 1

    # Reorder columns to make 'subject_id' the first column
    df = df[['subject_id', 'reaction_time', 'circle_color', 'key_pressed', 'accuracy']]

    # Append the processed DataFrame
    dfs.append(df)

# Concatenate all DataFrames
all_data = pd.concat(dfs, ignore_index=True)
```

## 3: Clean and Visualize Reaction Time Data

Now that we have all trials loaded into a DataFrame, we can start visualizing the reaction time data.

### 3a. Histogram of Reaction Time Data

Use a histogram to explore the distribution of reaction times. Adjust the bin width with an interactive widget.

```python
import matplotlib.pyplot as plt
import ipywidgets as widgets

def plot_histogram(bin_width):
    plt.hist(all_data['reaction_time'].dropna(), bins=bin_width)
    plt.title('Histogram of Reaction Times')
    plt.xlabel('Reaction Time (ms)')
    plt.ylabel('Frequency')
    plt.show()

widgets.interactive(plot_histogram, bin_width=widgets.IntSlider(min=5, max=100, step=5, value=20))
```

### 3b. Box Plot of Mean Reaction Times by Accuracy

A box and whisker plot can show differences in reaction times between "true" (correct) and "false" (incorrect) responses.

!!! Tip "Seaborn"
    Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for creating attractive and informative statistical graphics. You can install Seaborn using `pip install seaborn`.

    In your notebook, you might want to run `%pip install seaborn` to install Seaborn, instead of the normal pip install.

```python
import seaborn as sns

# Plot box and whisker plot for reaction times by accuracy
sns.boxplot(x='accuracy', y='reaction_time', data=all_data)
plt.title('Reaction Times by Accuracy')
plt.xlabel('Accuracy (True or False)')
plt.ylabel('Reaction Time (ms)')
plt.show()
```

It's great to have a visualization, but it will probably be good to know the means and standard deviation values of these plots as well, let's use Pandas to calculate those!

```python
import pandas as pd

# Assuming 'all_data' is your DataFrame
true_responses = all_data[all_data['accuracy'] == True]
false_responses = all_data[all_data['accuracy'] == False]

true_mean = true_responses['reaction_time'].mean()
true_sd = true_responses['reaction_time'].std()

false_mean = false_responses['reaction_time'].mean()
false_sd = false_responses['reaction_time'].std()

# Print the mean and standard deviation values, and the counts of each group
print(f"True responses - Mean: {true_mean}, SD: {true_sd}, Count: {len(true_responses)}")
print(f"False responses - Mean: {false_mean}, SD: {false_sd}, Count: {len(false_responses)}")
```

#### Think about the data

Look at the means and standard deviations. What do you think a paired t-test would show? What problem arrises when we look at the "Count" of each data type?

## 4: Aggregate Mean Reaction Times by Participant/Subject

Next, let’s condense the data to calculate each subject's mean reaction time and the number of "true" (correct) trials out of 50.

```python
# Calculate mean reaction times and true trial counts
subject_summary = all_data.groupby('subject_id').agg(
    mean_reaction_time=('reaction_time', 'mean'),
    true_count=('accuracy', lambda x: (x == True).sum())
).reset_index()
```

## 5: Visualize Mean Reaction Time Data

### 5a. Histogram of Mean Reaction Times

Plot a histogram of mean reaction times for each participant.

```python
plt.hist(subject_summary['mean_reaction_time'], bins=20)
plt.title('Histogram of Mean Reaction Times by subject')
plt.xlabel('Mean Reaction Time (ms)')
plt.ylabel('Frequency')
plt.show()
```

### 5b. Scatterplot of Reaction Time and % "True" Responses

Plot a scatterplot to explore the relationship between subjects’ mean reaction times and their accuracy rate.

```python
# Calculate accuracy percentage
subject_summary['true_percentage'] = (subject_summary['true_count'] / 50) * 100

# Scatterplot of mean reaction time vs. true percentage
plt.scatter(subject_summary['mean_reaction_time'], subject_summary['true_percentage'])
plt.title('Mean Reaction Time vs. % True Responses')
plt.xlabel('Mean Reaction Time (ms)')
plt.ylabel('% True Responses')
plt.show()
```

## 6. Have fun with it!

Take time to play with [Seaborn](https://seaborn.pydata.org/) and [Matplotlib](https://matplotlib.org/) to create more visualizations and explore the data further. You can also experiment with different data transformations and analysis techniques to gain deeper insights!

Dig into the Pandas dataframe, look at the data, and see if you can find any interesting patterns or relationships.

```python
# Display the first few rows of the DataFrame
all_data.head()
```

You can grab different columns and plot them against each other to see if there are any relationships. For example, you could plot the reaction time against the color of the circle that was shown to the participant.

## 7. Review

In this step, you’ve learned how to handle, clean, and visualize reaction time data using pandas, matplotlib, and seaborn. In a future step, we'll look at how to analyze this data statistically to draw meaningful conclusions!

# Step 22

## **Basic Statistics**

In this step, we'll apply statistical methods to the reaction time dataset generated in the previous steps. This dataset includes data related to reaction times for trials where the independent variable (IV) is the color of a circle. Here's what we aim to accomplish:

### Objectives
1. Establish the dataset.
2. Compute basic descriptives and create plots suitable for a paired samples t-test.
3. Perform and interpret a paired samples t-test.
4. Manipulate the dataset to add an additional variable, *previous circle color*.
5. Set up and run a two-way ANOVA to investigate interactions between the current circle color and the previous circle color.

---

### 1: Establish the Dataset
We will start with the `all_data` dataset generated in Step 21. This dataset contains reaction times for trials where the circle color is the independent variable.

Go back to Step 21 to get the `all_data` dataframe, when you do you should be able to run the code below and get the following result.

Code:

```python
all_data.head()
```

Result:
```python
    subject_id	reaction_time	circle_color	key_pressed	accuracy
0	    1	        445.0	        orange	        j	       True
1	    1	        386.0	        blue	        f	       True
2	    1	        366.0	        blue	        f	       True
3	    1	        374.0	        orange	        j	       True
4	    1	        409.0	        orange	        j	       True
```

---

### 2: Descriptives and Paired Samples T-Test Preparation
To prepare for the paired samples t-test:
- Compute summary statistics for each circle color.
- Visualize the data with plots to check assumptions like normality.

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Group by circle color and calculate summary statistics
descriptives = all_data.groupby('circle_color')['reaction_time'].describe()

# Boxplot to visualize reaction times by circle color
sns.boxplot(x='circle_color', y='reaction_time', data=all_data)
plt.title('Reaction Times by Circle Color')
plt.show()

# Print descriptive statistics
print(descriptives)
```

---

### 3: Perform the Paired Samples T-Test
A paired samples t-test compares reaction times between two conditions.

!!! Tip "pip install `scipy`"
    At this point you'll most likely need to install the `scipy` package. You can do this by running `%pip install scipy` in your notebook.

    What's `scipy`? Think of it as "scientific Python" - it's a library that provides many user-friendly and efficient numerical routines andf functions that are commonly used in scientific and engineering applications.

```python
from scipy.stats import ttest_rel

# Perform paired t-test
group1 = all_data[all_data['circle_color'] == 'orange']['reaction_time'] # Orange circle
group2 = all_data[all_data['circle_color'] == 'blue']['reaction_time'] # Blue circle

t_stat, p_value = ttest_rel(group1, group2)

# Display results
print(f"Paired Samples T-Test:\nT-Statistic = {t_stat}, p-value = {p_value}")
```

**Interpretation:** Based on the p-value, determine if there is a significant difference between reaction times for orange and blue circles.

??? Tip "Check your results"
    If you ran it correctly, you should get the following output:
    ```python
    # Paired Samples T-Test:
    # T-Statistic = -0.2520879211177987, p-value = 0.8010674499745879
    ```
    The p-value is greater than 0.05, indicating that there is no significant difference between reaction times for orange and blue circles.

    Is this surprising? No not really! The data didn't appear to be significantly different in the boxplot, and we don't have a good reason to think that the color of the circle alone would affect reaction times.

---

### 4: Add *Previous Circle Color* Variable
To explore potential effects of *previous circle color*, add this column to the dataset. The first trial is excluded as it lacks a "previous" circle.

```python
# Shift the 'circle_color' column to create the 'previous_circle_color' column
all_data['previous_circle_color'] = all_data['circle_color'].shift(1)

# Remove the first trial or row of data from every subject
all_data = all_data.groupby('subject_id').apply(lambda x: x.iloc[1:]).reset_index(drop=True)

# Display the updated dataset
print(all_data.head())
```

!!! Tip "Lambda Functions"
    In the code above, we used a lambda function to remove the first trial or row of data from every subject. Lambda functions are small, anonymous functions that can have any number of arguments but only one expression. They are often used in situations where a function is needed for a short period of time.

    Be on the lookout for a "Side Quest" where you can learn more about lambda functions!

I have a hypothesis; if the previous circle color was the same as the current circle color, the reaction time will be faster. Let's see if this is true!

To make our live's easier, we'll create a new column to include a new variable, `repeat_color`, which will be `True` if the previous circle color is the same as the current circle color, and `False` otherwise.

```python
# Create a new column 'same_color' to indicate if the previous circle color is the same as the current circle color
all_data['repeat_color'] = all_data['circle_color'] == all_data['previous_circle_color']
all_data.head()
```

In the next part, we'll perform an additional t-test to see if there is a significant difference in reaction times between trials where the previous circle color is the same as the current circle color and trials where it is different.

---

### 5: Another Paired Samples T-Test

Based on the code in part 3, I'd like for you to look at the code and then think about how you'd set it up yourself. After you think/test it, continue reading below.

#### Some Snags in the Plan

A problem arrises if you simply group the data by `repeat_color` and then run the t-test. The issue is that we no longer have equal sample sizes for each group, this is because, randomly, we ended up with 250 trials where the previous circle color was the same as the current circle color, and 828 trials where they were different.

Run the following code and you'll get an `ValueError: unequal length arrays` error.

```python
# Perform paired t-test
group1 = all_data[all_data['repeat_color'] == True]['reaction_time']  # Repeat color is True
group2 = all_data[all_data['repeat_color'] == False]['reaction_time']  # Repeat color is False

t_stat, p_value = ttest_rel(group1, group2)

# Display results
print(f"Paired Samples T-Test:\nT-Statistic = {t_stat}, p-value = {p_value}")

# Boxplot visualization
plt.figure(figsize=(10, 6))
sns.boxplot(x='repeat_color', y='reaction_time', data=all_data)
plt.title('Reaction Time by Repeat Color')
plt.xlabel('Repeat Color')
plt.ylabel('Reaction Time')
plt.show()
```

We can run this block of code below to demonstrate that the two arrays are indeed unequal lengths:

```python
import numpy as np

np.shape(group1), np.shape(group2)
```

#### Fixing the Issue

One way to fix the problem (an imperfect, but fine way for quick data visualization and exploration) is to randomly sample 250 trials from the `repeat_color == False` group. This way, we'll have equal sample sizes for both groups.

Let's do that below, and then perform the t-test and plot the results.

```python
# Randomly sample 250 trials from the 'repeat_color' == False group

group2_sample = all_data[all_data['repeat_color'] == False].sample(n=250, random_state=1)['reaction_time']

t_stat, p_value = ttest_rel(group1, group2_sample)

# Display results
print(f"Paired Samples T-Test:\nT-Statistic = {t_stat}, p-value = {p_value}")

# Get descriptive statistics
group1_desc = group1.describe()
group2_desc = group2_sample.describe()

print("\nDescriptive Statistics for Group 1 (Repeat Color is True):")
print(group1_desc)

print("\nDescriptive Statistics for Group 2 (Repeat Color is False):")
print(group2_desc)

# Boxplot visualization
plt.figure(figsize=(10, 6))
sns.boxplot(x='repeat_color', y='reaction_time', data=all_data)
plt.title('Reaction Time by Repeat Color')
plt.xlabel('Repeat Color')
plt.ylabel('Reaction Time')
plt.show()
```

By making the random_state equal to 1, we ensure that the random sample is the same every time we run the code. This way, we can reproduce the results and compare them across different runs.

This should also mean you see the same result that I do: it looks like there is no significant difference between reaction times when the previous circle color is the same as the current circle color compared to when they are different. It was a cool idea though, right?!

### 6: Two-Way ANOVA

There's one more thing that I'd like for us to explore: the possible effect and interaction between subjects...

We can set up a two-way ANOVA to investigate the effects of the current circle color, the previous circle color, and their interaction on reaction times.

!!! Tip "%pip install statsmodels"
    To run the two-way ANOVA, you'll need to install the `statsmodels` package. You can do this by running `%pip install statsmodels` in your notebook.

```python
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

# Fit the two-way ANOVA model
model = ols('reaction_time ~ C(subject_id) + C(circle_color) + C(subject_id):C(circle_color)', data=all_data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Display the ANOVA table
print(anova_table)

# Boxplot visualization
plt.figure(figsize=(12, 8))
sns.boxplot(x='circle_color', y='reaction_time', hue='subject_id', data=all_data)
plt.title('Reaction Time by Circle Color and Subject ID')
plt.xlabel('Circle Color')
plt.ylabel('Reaction Time')
plt.legend(title='Subject ID', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
```

If everything has gone smoothly, your resulting ANOVA table should look like this:
```txt
                                     sum_sq      df          F        PR(>F)
C(subject_id)                  3.327539e+06    21.0  11.095641  1.533542e-33
C(circle_color)                1.209871e+03     1.0   0.084720  7.710580e-01
C(subject_id):C(circle_color)  2.686349e+05    21.0   0.895760  5.971599e-01
Residual                       1.476631e+07  1034.0        NaN           NaN
```

The last column is your p-value in scientific notation; we can see that the only significant effect is the subject ID. This is not surprising, as we would expect that different subjects would have different reaction times.

What does this mean? It means that the color of the circle and the interaction between the color of the circle and the subject ID do not have a significant effect on reaction times, but different people do have different reaction times.

Now you've run a two-way ANOVA in Python! This is a powerful tool for analyzing the effects of multiple factors on a dependent variable.

---

### Conclusion
In this step, we:

- Established the reaction time dataset and computed basic statistics.
- Conducted a paired samples t-test to evaluate differences between orange and blue circles.
- Introduced a new variable (*same circle color*), and randomly sampled to ensure equal sample sizes for a second t-test.
- Performed a two-way ANOVA and visualized all of the data.

What are some things we didn't do?

- We didn't check for normality or homogeneity of variance in the t-tests or ANOVA.
- We didn't explore other statistical tests or models that could be applied to this dataset (Logistic Regression would be great, for example).
- We didn't remove outliers, this could have changed the results of the t-tests and ANOVA.

Take a moment to think about what else you'd like to explore with this dataset. What other statistical tests or models could be applied? What additional variables could be included to enhance the analysis? If you're brave enough, try to implement some of these ideas!

# Step 23

## Data Dive I: Finding Data

Your journey into data analysis starts with finding an interesting dataset. For this step, you can either:

1. **Search for Open Datasets**: Explore open-source datasets available on platforms like [Kaggle](https://www.kaggle.com/), [Data.gov](https://www.data.gov/), or [Google Dataset Search](https://datasetsearch.research.google.com/).

2. **Download Personal Data**: Many services allow you to download your personal data (e.g., Instagram, Spotify, or Google). Make sure the downloaded data is in a workable format such as `json`, `csv`, or `txt`. If you want to work with your own data, Google how to download it from the respective service.

## Preparing for Import

Once you have your data:

- Ensure the dataset is saved locally in a known file path.
- Check the file format (e.g., `.csv`, `.json`, `.txt`) as it will guide how you load it into Python.

## Using AI to Help Format Your Data

Organizing raw data can be challenging, especially if the dataset has many columns or uses inconsistent formatting. AI tools like **ChatGPT**, **Claude**, and **Microsoft Copilot** can help you write Python code to clean and organize your data.

### Best Practices When Using AI Tools

1. **Feed Your Datafile**: Many AI tools allow you to upload your dataset directly for analysis. Uploading your file can help the AI better understand your data structure.
2. **Provide Context**: Clearly describe what you're trying to achieve, such as renaming columns, handling missing values, or filtering rows.
3. **Iterate**: If the AI-generated code doesn’t work perfectly, provide feedback and ask for adjustments.

### Example Prompts for Using AI

Here are some sample prompts to get you started:

#### Prompt 1: General Formatting

*"I have a dataset in CSV format with inconsistent column names. Here's a sample of the data: [paste or upload your dataset]. Could you help me write Python code using Pandas to clean the column names (e.g., make them lowercase and replace spaces with underscores) and handle missing values by filling them with 0?"*

#### Prompt 2: Renaming Columns

*"Here’s my dataset: [paste or upload]. I want to rename the column `Old Column Name` to `new_column_name`. Could you provide the Pandas code to do this?"*

#### Prompt 3: Filtering Rows

*"My dataset has a column called `age`. Could you write Python code using Pandas to filter out rows where the age is less than 18? Here’s the data: [paste or upload]."*

#### Prompt 4: Creating New Columns

*"I have this dataset: [paste or upload]. I’d like to create a new column that calculates the ratio of `sales` to `profit`. Could you help me write the code for that in Pandas?"*

#### Prompt 5: Data Structure Insights

*"Here’s my dataset: [paste or upload]. Could you provide a summary of the dataset, including column data types and a preview of the first few rows? Also, suggest any obvious cleaning steps that might be necessary."*

### Why Use AI?

AI tools can speed up your workflow, reduce errors, and give you creative ideas for working with your data. However, it's essential to understand the basics of Pandas so you can verify and tweak the code generated by the AI.

How do you get the basics of Pandas down? By practicing and looking things up! In previous learning steps, we've used Pandas to do a variety of tasks, such as filtering data, creating new columns, and summarizing data. Go back and look at what we did, look up function names in the Pandas documentation [(linked here)](https://pandas.pydata.org/pandas-docs/stable/index.html), and practice using Pandas on your own data.

## Importing Data into Pandas

Follow these steps to import and organize your data into a Pandas DataFrame:

### 1. Setting Up

Start by importing the necessary libraries.

```python
import pandas as pd
import json  # Only if your dataset is in JSON format

# Add more libraries if needed (e.g., os for file management)
```

### 2. Loading Data Based on File Type

#### For CSV Files:

```python
# Replace 'your_dataset.csv' with your file's name
file_path = 'your_dataset.csv'
data = pd.read_csv(file_path)

# Preview the first few rows
print(data.head())
```

#### For JSON Files:

```python
# Replace 'your_dataset.json' with your file's name
file_path = 'your_dataset.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Convert JSON data into a DataFrame
df = pd.DataFrame(data)
print(df.head())
```

#### For TXT Files (Delimited):

```python
# Replace 'your_dataset.txt' with your file's name and delimiter (e.g., '\t' for tab-delimited)
file_path = 'your_dataset.txt'
data = pd.read_csv(file_path, delimiter='\t')

# Preview the first few rows
print(data.head())
```

### 3. Cleaning and Organizing the DataFrame

Once your data is loaded, ensure it's organized and meaningful:

!!! Tip "Keep looking at your DataFrame"
    As you clean and organize your data, keep checking the DataFrame to ensure it's structured the way you want. Use `print(data.head())` to preview the first few rows and `print(data.info())` to get an overview of the columns and data types.

- **Inspect the structure**:
  ```python
  print(data.info())  # Overview of columns and data types
  ```

- **Rename columns** if needed:
  ```python
  data.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)
  ```

- **Filter unnecessary rows/columns**:
  ```python
  # Dropping a column
  data.drop(columns=['unnecessary_column'], inplace=True)
  
  # Keeping specific rows
  data = data[data['column_name'] > threshold_value]
  ```

- **Handle missing values**:
  ```python
  data.fillna(value=default_value, inplace=True)  # Fill missing values
  data.dropna(inplace=True)  # Optionally drop rows with missing values
  ```

## Conclusion

At this stage, you should have:

- Located and downloaded an interesting dataset.
- Used AI tools (optional but highly recommended!) to assist in formatting and organizing your data.
- Imported it into Python using Pandas.
- Organized the dataset to ensure meaningful rows and columns.

Once you're comfortable with the structure of your data, you're ready to dive into visualizations in Step 24!

# Step 24

In this step, we explore fine-tuning Matplotlib visualizations for enhanced customizability. We'll use the `all_data` dataset generated in Step 21 to create overlapping histograms with Probability Density Functions (PDFs) and legends. Along the way, we'll explain specific parts of the code you'll modify or customize in each section.

---

### 1. Setting Up Our Data
We start by filtering the `all_data` dataframe to create two datasets based on `circle_color`. These will serve as the reaction time data for the two groups (orange and blue).

**Dataset Setup:**

- `orange_reactiontime_df`: Contains reaction times for trials where `circle_color` is `'orange'`.
- `blue_reactiontime_df`: Contains reaction times for trials where `circle_color` is `'blue'`.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Assuming all_data is already loaded
# If you do not have it yet, go back to Step 21 and load it as instructed
all_data = pd.read_csv('reaction_time_data.csv')  # Replace with actual file path
# If you've already got `all_data` loaded, you can skip this step by commenting it out

# Create datasets for the two groups
orange_reactiontime_df = all_data[all_data['circle_color'] == 'orange']['reaction_time']
blue_reactiontime_df = all_data[all_data['circle_color'] == 'blue']['reaction_time']

# Preview the datasets
print("Orange Reaction Times:\n", orange_reactiontime_df.head())
print("Blue Reaction Times:\n", blue_reactiontime_df.head())
```

**Key Parts to Check:**

- Ensure `all_data` is loaded correctly and contains the expected columns (`reaction_time`, `circle_color`).
- Replace `'reaction_time_data.csv'` with the actual file name/path if needed.

---

### 2. Creating Independent Histograms
Now that we have two different dataframes, lSet's create histograms for the orange and blue reaction times individually.

```python
# Orange Reaction Time Histogram
plt.figure(figsize=(8, 6))
plt.hist(orange_reactiontime_df, bins=20, color='orange', alpha=0.6, label='Orange')
plt.title('Histogram of Reaction Times: Orange')
plt.xlabel('Reaction Time (ms)')
plt.ylabel('Frequency')
plt.show()

# Blue Reaction Time Histogram
plt.figure(figsize=(8, 6))
plt.hist(blue_reactiontime_df, bins=20, color='blue', alpha=0.6, label='Blue')
plt.title('Histogram of Reaction Times: Blue')
plt.xlabel('Reaction Time (ms)')
plt.ylabel('Frequency')
plt.show()
```

**Key Parts to Modify:**

- `bins=20`: Adjust the number of bins (granularity) if needed.
- `color='orange'` and `color='blue'`: Customize colors as desired.
- `alpha=0.6`: Adjust transparency (range: 0 to 1).

!!! Tip "IpyWidget to Play with `alpha` value"
    You can use an IpyWidget to interactively adjust the `alpha` value and see the visual effect it has on the histogram. 

    This will be cooler to do when we overlap our histograms later, but for now here's an example:
    
    ```python
    from ipywidgets import interact

    @interact(alpha=(0, 1, 0.05))
    def plot_histogram(alpha=0.6):
        plt.figure(figsize=(8, 6))
        plt.hist(orange_reactiontime_df, bins=20, color='orange', alpha=alpha, label='Orange')
        plt.title('Histogram of Reaction Times: Orange')
        plt.xlabel('Reaction Time (ms)')
        plt.ylabel('Frequency')
        plt.show()
    ```

    This code snippet creates an interactive slider for the `alpha` value, allowing you to see the histogram change in real-time.

    *What other ways could you use an IpyWidgets to interact with your data?*

---

### 3. Combining into a Two-Paneled Plot
Two histograms are cool, but it would be nice if they were attached/connected in some way. We can create a side-by-side comparison of the two histograms using subplots!

To do this, we'll set up a `fig` figure object with a corresponding `axs` array to hold the two subplots and then plot the histograms for orange and blue reaction times in each panel.

```python
fig, axs = plt.subplots(1, 2, figsize=(12, 6), constrained_layout=True)

# Panel 1: Orange
axs[0].hist(orange_reactiontime_df, bins=20, color='orange', alpha=0.6, label='Orange')
axs[0].set_title('Orange Reaction Times')
axs[0].set_xlabel('Reaction Time (ms)')
axs[0].set_ylabel('Frequency')

# Panel 2: Blue
axs[1].hist(blue_reactiontime_df, bins=20, color='blue', alpha=0.6, label='Blue')
axs[1].set_title('Blue Reaction Times')
axs[1].set_xlabel('Reaction Time (ms)')

plt.suptitle('Reaction Times by Circle Color')
plt.show()
```

**Key Parts to Modify:**

- `figsize=(12, 6)`: Change plot size if necessary.
- Customize subplot titles and labels as needed.

!!! Tip "figure fun" 
    You can also use the `fig` object to save your figure to a file. For example, `fig.savefig('reaction_time_histograms.png')` will save the figure as a PNG file in the current directory.

    You can also adjust the layout using `fig.tight_layout()`, or set a global title with `fig.suptitle('Overall Title')`.

---

### 4. Overlapping Histograms with PDFs
One of my favorite ways to display/compare histograms is to combine the two datasets into a single plot, overlaying histograms. We can then calculate and plot probability density function for each dataset to visualize the distribution more clearly.

!!! Tip "What's a Probability Density Function (PDF)?"
    A Probability Density Function (PDF) is a statistical function that describes the likelihood of a continuous random variable falling within a particular range. In this case, we're using the normal distribution PDF to model the reaction time data.

    The `norm.pdf()` function from `scipy.stats` calculates the PDF of a normal distribution given a set of values, mean, and standard deviation.

    The normal curve helps us visualize how the data is distributed around the mean and how likely certain values are.

```python
plt.figure(figsize=(10, 6))

# Orange Histogram and Curve
plt.hist(orange_reactiontime_df, bins=20, color='orange', alpha=0.4, label='Orange', density=True)
plt.plot(
    np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
    norm.pdf(
        np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
        np.mean(orange_reactiontime_df),
        np.std(orange_reactiontime_df),
    ),
    color='orange',
    linestyle='--',
    linewidth=2,
    label='Orange PDF',
)

# Blue Histogram and Curve
plt.hist(blue_reactiontime_df, bins=20, color='blue', alpha=0.4, label='Blue', density=True)
plt.plot(
    np.linspace(blue_reactiontime_df.min(), blue_reactiontime_df.max(), 500),
    norm.pdf(
        np.linspace(blue_reactiontime_df.min(), blue_reactiontime_df.max(), 500),
        np.mean(blue_reactiontime_df),
        np.std(blue_reactiontime_df),
    ),
    color='blue',
    linestyle='-',
    linewidth=2,
    label='Blue PDF',
)

plt.title('Overlapping Reaction Time Histograms with PDF Curves')
plt.xlabel('Reaction Time (ms)')
plt.ylabel('Density')
plt.legend()
plt.show()
```

**Key Parts to Modify:**

- Adjust the `np.linspace` range to fit the specific dataset more tightly.
- Modify `linestyle='--'` or `linewidth=2` for the curves as needed.

#### Breaking down the PDF Calculation:

The following code snippet is what calculates the PDF line for the orange histogram:

```python
plt.plot(
    np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
    norm.pdf(
        np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
        np.mean(orange_reactiontime_df),
        np.std(orange_reactiontime_df),
    ),
    color='orange',
    linestyle='--',
    linewidth=2,
    label='Orange PDF Curve',
)
```

Let's break it down piece by piece:

- `np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500)`: This creates 500 evenly spaced points between the minimum and maximum reaction times in the orange dataset. This range is used to calculate the PDF values.
- `norm.pdf(...)`: This calculates the PDF values for the given range using the mean and standard deviation of the orange dataset.
- `np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500)`: This is the range of x-values for the PDF curve, we repeat it here to ensure the x-values match the PDF values.
- `np.mean(orange_reactiontime_df)`: The mean of the orange reaction times. This is used as the center of the normal distribution.
- `np.std(orange_reactiontime_df)`: The standard deviation of the orange reaction times. This controls the spread of the normal distribution.
- color, linestyle, linewidth, label: These are used to customize the appearance of the PDF curve and how it appears in the legend (respectively).

---

### 5. Fine-Tuning and Customizing
Add legends, gridlines, and vertical lines indicating mean reaction times.

```python
plt.figure(figsize=(10, 6))

# Histograms
plt.hist(orange_reactiontime_df, bins=20, color='orange', alpha=0.5, label='Orange', density=True)
plt.hist(blue_reactiontime_df, bins=20, color='blue', alpha=0.5, label='Blue', density=True)

# PDFs
plt.plot(
    np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
    norm.pdf(
        np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
        np.mean(orange_reactiontime_df),
        np.std(orange_reactiontime_df),
    ),
    color='orange',
    linestyle='--',
    linewidth=2,
    label='Orange PDF Curve',
)
plt.plot(
    np.linspace(blue_reactiontime_df.min(), blue_reactiontime_df.max(), 500),
    norm.pdf(
        np.linspace(blue_reactiontime_df.min(), blue_reactiontime_df.max(), 500),
        np.mean(blue_reactiontime_df),
        np.std(blue_reactiontime_df),
    ),
    color='blue',
    linestyle='-',
    linewidth=2,
    label='Blue PDF Curve',
)

# Customizations
plt.title('Customized Reaction Time Histograms')
plt.xlabel('Reaction Time (ms)')
plt.ylabel('Density')
plt.grid(visible=True, which='both', linestyle='--', alpha=0.6)
plt.axvline(np.mean(orange_reactiontime_df), color='orange', linestyle='-', label='Mean Orange')
plt.axvline(np.mean(blue_reactiontime_df), color='blue', linestyle='-', label='Mean Blue')
plt.legend(loc='upper right', frameon=True, fontsize=10)

plt.show()
```

**Key Parts to Modify:**

- Adjust `plt.grid(...)` for appearance.
- Add or adjust vertical lines (`plt.axvline(...)`) for additional statistical markers.

### 6. Cleaning Up Your Figure

One thing you might notice is that at this point, our figure is pretty bloated. We really don't need all that information hanging out in the legend, for example.

We can spend some time going back into our figure and cleaning up the code to make it appear a bit nicer, and more publication-ready. We can...

- Remove unnecessary labels from the legend.
- Adjust the font size of the legend so that they're all legible.
- Remove the gridlines if they're not necessary.
- Adjust the bin size of the histograms so that they're the same width for both groups.
- Remove tick marks on the y-axis to clean up the figure.

#### First, we're going to calculate bin sizes for the histograms so that they're the same width for both groups.

```python

# Define bin size
bin_size = 50  # for example, 50 ms

# Calculate bin edges
orange_bins = np.arange(min(orange_reactiontime_df), max(orange_reactiontime_df) + bin_size, bin_size)
blue_bins = np.arange(min(blue_reactiontime_df), max(blue_reactiontime_df) + bin_size, bin_size)
```
#### Now, we'll implement these bin sizes in our histograms.

```python
plt.figure(figsize=(10, 6))

# Histograms
plt.hist(orange_reactiontime_df, bins=orange_bins, color='orange', alpha=0.5, label='Orange', density=True)
plt.hist(blue_reactiontime_df, bins=blue_bins, color='blue', alpha=0.5, label='Blue', density=True)

# PDFs
plt.plot(
    np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
    norm.pdf(
        np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
        np.mean(orange_reactiontime_df),
        np.std(orange_reactiontime_df),
    ),
    color='orange',
    linestyle='--',
    linewidth=2,
    # remove unnecessary legend label; orange = color orange, blue = blue.
)
plt.plot(
    np.linspace(blue_reactiontime_df.min(), blue_reactiontime_df.max(), 500),
    norm.pdf(
        np.linspace(blue_reactiontime_df.min(), blue_reactiontime_df.max(), 500),
        np.mean(blue_reactiontime_df),
        np.std(blue_reactiontime_df),
    ),
    color='blue',
    linestyle='-',
    linewidth=2,
)

# Customizations
plt.title('Customized Reaction Time Histograms', fontsize=20)
plt.xlabel('Reaction Time (ms)', fontsize=16)
plt.ylabel('Density', fontsize=16)
plt.grid(visible=True, which='both', linestyle='-', alpha=0.6) # Change linestyle to '-'
plt.axvline(np.mean(orange_reactiontime_df), color='orange', linestyle='-')
plt.axvline(np.mean(blue_reactiontime_df), color='blue', linestyle='-')

# Clean up the legend
plt.legend(loc='upper right', frameon=True, fontsize=12) # Increase font size
plt.tick_params(axis='both', which='both', length=0) # Hide tick marks on the edge

plt.show()
```

#### Other things to consider

There are more ways you could customize this plot...

- You could add texture to the bars of the histogram to make them more visually distinct
- You could make sure your histograms start at the same value so that the bins are perfectly aligned
- ... and more!

---

### Summary

In this *final* step of our learning path, we've explored fine-tuning Matplotlib visualizations to create publication-quality figures. By layering histograms, PDFs, and annotations, we've enhanced the clarity and visual appeal of our data representations. These techniques can be applied to a wide range of datasets and research questions, allowing you to create compelling visualizations that effectively communicate your findings.

Now you should have everything you need to create a publication-quality figure in Python!

# Step 25 - What Next?

By now, you should have completed your programming journey and the content of this course!

Take a moment to congratulate yourself on your hard work and dedication. You have learned a lot and should be proud of your accomplishments!

# First, Thank you

Being able to build and share this course material with you means a lot to me - the journey of learning to enjoy programming is exciting for me! A special thanks to the students who signed up for my first 3010 class. Without you, this wouldn't exist.

I don't expect all of you to fall in love with programming like I have, but I hope that at least you've learned about and have grown to appreciate the role that programming plays in your life.

# Looking for more?

There will be likely those among you who have experienced the "spark" of programming - that feeling of excitement when you build something that works. If you're one of those people, I want to encourage you to keep learning and growing as a programmer. This can be self-directed, and as fast or slow as you want it to be!

The feeling like you can *build anything* is incredibly exciting. In the sections below, I'm sharing the resources for learning I've found over the years. I've only been able to use a small fraction of them, but all of these places are there for you to go, learn, and dream!

## JavaScript

You might want to dig into JavaScript if you like the idea of building something awesome that lives on the web. JavaScript is the language of the web, and it's a great place to start if you want to build websites, web apps, or even mobile apps.

To learn about JavaScript, I'd recommend you first go to Mozilla's Developer Network (MDN) and check out their [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide). It's a fantastic place to start.

If you get the hang of JavaScript, you might want to check out [React](https://reactjs.org/), a JavaScript library for building user interfaces. It's a great way to build interactive web apps - and many of the apps you've used run on React.

## More Python

If you want to keep learning Python, I'd recommend you check out the [Python documentation](https://docs.python.org/3/). It's a great place to learn more about the language and its features.

There are really great libraries you can dig into as well for diving into some interesting topics in Python - one of which is Django, a web framework for building web applications. You can check out the [Django documentation](https://docs.djangoproject.com/en/3.0/) to learn more. 

## Data Science

If you're interested in data science, you might want to check out [Kaggle](https://www.kaggle.com/). It's a great place to learn about data science and machine learning, and they have a lot of great resources to help you get started.

### Machine Learning

Related to Data Science, if you're interested in machine learning, you might want to check out [TensorFlow](https://www.tensorflow.org/). It's a great library for building machine learning models, and they have a lot of great resources to help you get started.

For something a bit more "wild west", check out any of the following links:

- [OpenAI's API](https://platform.openai.com)
- [Hugging Face](https://huggingface.co/)
- [Fast.ai](https://www.fast.ai/)
- [OpenCV](https://opencv.org/) 

## Game Development

If you're interested in game development, you might want to check out [Unity](https://unity.com/). It's a great platform for building games, and they have a lot of great resources to help you get started - I've used and coached students through their tutorials and they're fantastic, check those out here: [Unity Learn](https://learn.unity.com/).

If you're interested in a slightly more difficult game development platform, you might want to check out [Unreal Engine](https://www.unrealengine.com/). It's a great platform for building games, and they have a lot of great resources to help you get started.

## Mobile Apps with Flutter

If you're interested in building mobile apps, you might want to check out [Flutter](https://flutter.dev/). It's a great platform for building mobile apps, and they have a lot of great resources to help you get started.

Flutter runs on the Dart programming language, a python-like language that's easy to learn, developed by Google. You can check out the [Dart documentation](https://dart.dev/guides) to learn more.

## Take on the Universe with Rust

If you're interested in a language that's a bit more challenging, you might want to check out [Rust](https://www.rust-lang.org/). It's a great language for building systems software, and it's designed to be safe, concurrent, and practical.

Rust is absolutely one of the most important programming languages of the future, and if you're really excited about coding, I'd definitely recommend you check it out!

If you want to dive into learning, check out [the book](https://doc.rust-lang.org/book/). 

# Finally: Free and Open Source

A final thought I want to leave you with is the power of free and open source software. The programming community - the world - is built on top of free and open source software. It's a powerful idea that anyone can use, modify, and distribute software for free.

Check out the [GNU Operating System's Philosophy page](https://www.gnu.org/philosophy/philosophy.html) and [the GNU GPL 3 license "why" page](https://www.gnu.org/licenses/why-affero-gpl.html). These both provide detailed and practical explanations of why free and open source software is so important.

The story of working in the open source space is fascinating to me, if it sounds interesting to you, I highly recommend checking out this book, [Working in Public](https://www.amazon.com/Working-Public-Making-Maintenance-Software/dp/0578675862). 

If you want to contribute to the open source community, check out [GitHub](https://github.com).