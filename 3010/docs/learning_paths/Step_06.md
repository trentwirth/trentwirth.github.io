# Step 6

In Step 6, we will focus on problem-solving using control structures. This step will build on the concepts of conditional statements and introduce loops, which are essential for creating dynamic and efficient programs.

## Problem-Solving with Control Structures

Control structures allow us to control the flow of our programs, making them more dynamic and responsive to different inputs and conditions. In this step, we will explore how to use control structures to solve problems.

### Loops in Python

Loops are used to execute a block of code repeatedly. Python provides two types of loops: `for` loops and `while` loops.

### The `for` Loop

The `for` loop is used to iterate over a sequence of numbers and execute a block of code for each number.

!!! Tip "`list`s in Python"
    A `list` is a collection of items that can be of different types. You can create a list by placing the items inside square brackets `[]`, separated by commas. For example:

    ```python
    numbers_list = [1, 2, 3, 4, 5]
    ```

    Lists are iterable, meaning you can loop over the items in a list using a `for` loop. Python makes great use of lists and other iterable objects to simplify programming tasks!

#### Syntax

```python
numbers_list = [1, 2, 3, 4, 5]

for number in numbers_list:
    # code block to be executed for each number in the list
```
#### Example

```python
numbers_list = [1, 2, 3, 4, 5]
for number in numbers_list:
    print(number)
```

??? Tip "The `range()` Function"
    The `range()` function is commonly used with `for` loops to generate a sequence of numbers. It takes three arguments: `start`, `stop`, and `step`. For example, `range(1, 6, 2)` generates the sequence `1, 3, 5`.

    You can also use `range()` with a single argument to generate a sequence starting from 0. For example, `range(5)` generates the sequence `0, 1, 2, 3, 4`. 

    You can use the `range()` function to iterate over a specific range of numbers in a `for` loop, like this: 

    ```python
    for i in range(1, 6):
        print(i)
    ```

#### Another Example

Just like you can loop over a list of numbers, you can loop over a string in Python. When you feed in a string to a `for` loop, it will iterate over each character in the string.

```python
for character in "This will print vertically":
    print(character)
```

### The `while` Loop

The `while` loop is used to execute a block of code as long as a condition is true.

#### Syntax

```python
while condition:
    # code block to be executed as long as the condition is true
```

#### Example

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

!!! Tip "The `+=` Operator"
    The `+=` operator is used to increment (add) the value of a variable. This is a shorter way to write 
    ```python
    variable = variable + 1
    ```
    
    `-=` can be used to decrement (subtract) the value of a variable, as well as `*=`, `/=`, and `**=` for multiplication, division, and exponentiation, respectively.

### Combining Loops and Conditional Statements

You can combine loops and conditional statements to create more complex control structures.

#### Example

```python
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers_list:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
```

## Exercise: Problem-Solving with Control Structures

Now it's time to practice using loops and conditional statements to solve problems. You can do this in your own Colab Notebook, in an `.ipynb` file in VSCode, or in a Python file in VSCode.

### Exercise 1: Simple Loops

Write a Python program that prints the numbers from 1 to 5 using a `for` loop, then do it again for a `while` loop.

??? Tip "Solution"
    Here's a simple solution to the simple loops problem:
    
    ```python
    # Using a for loop
    numbers_list = [1, 2, 3, 4, 5]
    for i in numbers_list:
        print(i)
    ```

    ```python
    # Using a while loop
    count = 1
    while count < 6:
        print(count)
        count += 1
    ```

### Exercise 2: Sum of Numbers

Write a Python program that calculates the sum of numbers from 1 to 10.

??? Tip "Hint"
    You can use a `for` loop combined with the `range()` function to iterate over the numbers from 1 to 10 and calculate the sum. You could also implement the `+=` operator to increment the sum for each number.

??? Tip "Solution"
    Here's a simple solution to the sum of numbers problem:
    
    ```python
    total = 0
    for i in range(1, 11):
        total += i
    print(f"The sum of numbers from 1 to 10 is: {total}")
    ```

### Exercise 3: FizzBuzz

Write a Python program that prints the numbers from 1 to 20. For multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

??? Tip "Solution"
    Here's a simple solution to the FizzBuzz problem:
    
    ```python
    for i in range(1, 21):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    ```
### Exercise 4: Counting Vowels

Write a Python program that counts the number of vowels in a given string.

??? Tip "Hint" 
    You can use a for loop to iterate over each character in the string and a conditional statement to check if the character is a vowel.

??? Tip "Solution" 
    Here is one solution to the problem:
    ```python
    string = "This is a sample string"
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    print(f"The number of vowels in the string is: {count}")
    ```

### Exercise 5: Reverse a String

Write a Python program that reverses a given string using a for loop.

??? Tip "Hint" 
    You can use a for loop to iterate over the string in reverse order and build a new string.

??? Tip "Solution" 
    Here's a possible solution:
    ```python
    string = "Hello, World!"
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    print(f"The reversed string is: {reversed_string}")
    ```

    *Think*: Why does this solution work?

### Exercise 6: Multiplication Table with F-Strings

Write a Python program that generates a multiplication table for numbers 1-5, using f-strings.

??? Tip "Hint" 
    You can use nested `for` loops to generate the multiplication table for numbers 1-5.

??? Tip "Solution"
    Here's a possible solution:
    ```python
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i} x {j} = {i * j}") # Print a new line after each row
    ```

    This solution uses nested `for` loops to generate the multiplication table for numbers 1-5. The outer loop iterates over the numbers 1-5 for the first multiplier, and the inner loop iterates over the numbers 1-5 again for the second number, generating a table of all multiplication results.

## Reflect

Think about how loops and conditional statements can be used to solve problems. What are some real-world scenarios where these concepts might be useful?

??? Tip "Automating Repetitive Tasks"
    Loops and conditional statements are essential for automating repetitive tasks and handling different conditions in programs. For example, you can use loops to process large datasets, iterate over files in a directory, or perform calculations based on specific conditions. Conditional statements can be used to control the flow of a program, handle user inputs, or make decisions based on certain criteria.

    Another tool, `functions`, can also be used to automate repetitive tasks. We'll learn about functions in the next step!

## Review

In this step, we learned about loops and how to use them in combination with conditional statements to solve problems. Here's a quick recap:

- **`for` Loop**: Used to iterate over a sequence of numbers and execute a block of code for each number.
- **`while` Loop**: Used to execute a block of code as long as a condition is true.
- **Combining Loops and Conditional Statements**: Allows for more complex control structures and problem-solving.

Understanding these concepts is essential for writing dynamic and efficient programs in Python.
