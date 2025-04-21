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