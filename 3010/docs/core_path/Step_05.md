# Step 5

In Step 5, we will explore control structures in Python, specifically focusing on making decisions using conditional statements. Control structures allow us to control the flow of our programs, making them more dynamic and responsive to different inputs and conditions.

!!! Tip "Write as you Go"
    As you work through this step, try writing code snippets in your own Notebook either in VSCode or Google Colab. This will help you practice and reinforce what you're learning.

## Indentations in Python

Indentation is a crucial aspect of Python syntax. Unlike many other programming languages that use braces `{}` to define code blocks, Python uses indentation to determine the grouping of statements. This means that the level of indentation (spaces or tabs) is used to define the structure and flow of your code.

!!! Tip "How to make an indentation?"
    In VSCode and Google Colab, you can create an indentation by pressing the `Tab` key on your keyboard. You can also use the `Shift` + `Tab` key to remove/reverse an indentation.

    *Weirdly*, in Python, the "prefered" way to indent is to use 4 spaces. This is because it is easier to read and is more consistent across different editors and platforms - because typically, when you press `Tab`, it creates a character `\t`. HOWEVER, most IDEs like VSCode will automatically convert tabs to 4 spaces for you - for the purposes of this class, you should be fine to use the `Tab` key.

### Why Indentation Matters

Indentation is not just for readability; it is a *fundamental part* of Python's syntax (remember, "syntax" is a way of saying "the way the program is written to be understood by the machine"). Incorrect indentation can lead to syntax errors or unexpected behavior in your code.

### Rules for Indentation

1. **Consistent Indentation**: Use the same number of spaces or tabs for each level of indentation. Mixing spaces and tabs can cause errors. Most 
2. **Standard Practice**: The standard practice is to use 4 spaces for each level of indentation. Most Python editors and IDEs (like VSCode) are configured to use 4 spaces by default.
3. **Indentation Levels**: Each level of indentation represents a new block of code. For example, the code inside an `if` statement or a loop must be indented.

### Example

We will learn about `if` statements in the next section below, but here's an example to illustrate the importance of indentation. This might make more sense after you learn what an `if` statement is, but for now think of an `if` statement as a way to check if a condition is true or false.

```python
x = 10
if x > 5:
    print("x is greater than 5")
    if x > 8:
        print("x is also greater than 8")
print("This line is outside the if statement")
```

In this example:

- The first `print` statement is indented once, so it is part of the `if x > 5` block.
- The second `print` statement is indented twice, so it is part of the `if x > 8` block, which is nested inside the first `if` block.
- The final `print` statement is not indented, so it is outside of the `if` block and will always be executed.

So, remember to pay attention to your indentation when writing Python code! It changes the way the code will be executed. Now, onto more fun things!

## Conditional Statements

Conditional statements are used to perform different actions based on different conditions. The most common conditional statements in Python are `if`, `elif`, and `else`.

### The `if` Statement

The `if` statement is used to test a condition. If the condition is true, the code block inside the `if` statement is executed.

!!! Tip "Recall: Boolean Operators"
    Remember that conditional statements rely on boolean expressions to determine whether a condition is true or false. We went over boolean operators in Step 4, but here's a quick refresher:
    
    A boolean expression is an expression that evaluates to either `True` or `False`. We can make the variable `condition` in the `if` statement is a boolean expression by setting it equal to to either `True` or `False` before we run the code. You can experiment with this in your own Notebook, printing out a value within the conditional statement to see how it changes.

#### Syntax

```python
if condition:
    # code block to be executed if the condition is true
```

#### Example

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

### The `elif` Statement

The `elif` statement is short for "else if". It allows us to check multiple conditions.

#### Syntax

```python
if condition1:
    # code block to be executed if condition1 is true
elif condition2:
    # code block to be executed if condition2 is true
```

#### Example

```python
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
```

### The `else` Statement

The `else` statement catches anything that isn't caught by the preceding conditions.

#### Syntax

```python
if condition1:
    # code block to be executed if condition1 is true
elif condition2:
    # code block to be executed if condition2 is true
else:
    # code block to be executed if none of the conditions are true
```

#### Example

```python
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is 5 or less")
```

!!! Tip "Play with it!"
    In a notebook, copy and paste the code above. Then try changing the value of `x` in the example above to see how the output changes based on the conditions.

## Exercise: Making Decisions with Conditional Statements

Now it's time to practice using conditional statements. You can do this in your own Colab Notebook, in an `.ipynb` file in VSCode, or in a Python file in VSCode.

### Exercise 1: Basic `if` Statement

Write a Python program that checks if a number is positive, negative, or zero and prints the result.

??? Tip "Solution"

    Here's a simple solution to the basic `if` statement problem:

    ```python
    x = 10
    if x > 0:
        print("x is positive")
    elif x < 0:
        print("x is negative")
    else:
        print("x is zero")
    ```

### Exercise 2: Using `elif` and `else`

Write a Python program that checks the grade of a student based on their score and prints the corresponding grade (A, B, C, D, or F).

??? Tip "Solution"

    Here's a simple solution to the grade-checking problem:

    ```python
    score = 85
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
    ```

## Reflect

Think about how conditional statements can be used to control the flow of a program. What are some real-world scenarios where these concepts might be useful?

??? Tip "Sorting Data"
    Conditional statements can be used to sort data, filter out unwanted information, or make decisions based on specific criteria. For example, you might use conditional statements to categorize products based on their price, filter out invalid user inputs, or determine the eligibility of a customer for a discount.

## Review

In this step, we learned about conditional statements in Python. Here's a quick recap:

- **`if` Statement**: Used to test a condition and execute a code block if the condition is true.
- **`elif` Statement**: Allows us to check multiple conditions.
- **`else` Statement**: Catches anything that isn't caught by the preceding conditions.

Understanding these concepts is essential for writing dynamic and responsive programs in Python.
