# Step 4

In Step 4, we will dive into operators and expressions in Python. Operators allow us to perform various operations on data, and expressions combine variables and operators to produce new values. Understanding these concepts is crucial for writing effective and efficient code.

## Operators in Python

Python provides several types of operators that you can use to perform different operations on data. Here are the main types of operators:

### Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

- **Addition (`+`)**: Adds two numbers.
- **Subtraction (`-`)**: Subtracts the second number from the first.
- **Multiplication (`*`)**: Multiplies two numbers.
- **Division (`/`)**: Divides the first number by the second.
- **Modulus (`%`)**: Returns the remainder of the division.
- **Exponentiation (`**`)**: Raises the first number to the power of the second.

#### Examples of Arithmetic Operators
> You can run any of these examples in an `.ipynb` inside of VSCode, or in a Colab notebook.
??? tip "What's an `.ipynb`?"
    An `.ipynb` file is a "Jupyter Notebook" file that allows you to run Python code in a cell-by-cell format. You've already been working with these in Google Colab! You can create a new `.ipynb` file in VSCode by clicking on the `New File` button in the file explorer and selecting `Python 3` as the kernel. If you want to try this out, go for it! Ask a chatbot or your professor if you get confused.

```python
# Addition
result = 5 + 3
print("5 + 3 =", result)

# Subtraction
result = 10 - 4
print("10 - 4 =", result)

# Multiplication
result = 7 * 2
print("7 * 2 =", result)

# Division
result = 15 / 3
print("15 / 3 =", result)

# Modulus
result = 10 % 3
print("10 % 3 =", result)

# Exponentiation
result = 2 ** 3
print("2 ** 3 =", result)
```

### Comparison Operators

Comparison operators are used to compare two values and return a boolean result (`True` or `False`).

- **Equal to (`==`)**: Checks if two values are equal.
- **Not equal to (`!=`)**: Checks if two values are not equal.
- **Greater than (`>`)**: Checks if the first value is greater than the second.
- **Less than (`<`)**: Checks if the first value is less than the second.
- **Greater than or equal to (`>=`)**: Checks if the first value is greater than or equal to the second.
- **Less than or equal to (`<=`)**: Checks if the first value is less than or equal to the second.

#### Examples of Comparison Operators
> You can run any of these examples in an `.ipynb` inside of VSCode, or in a Colab notebook.

```python
# Equal to
print(5 == 5)  # True

# Not equal to
print(5 != 3)  # True

# Greater than
print(7 > 4)  # True

# Less than
print(3 < 8)  # True

# Greater than or equal to
print(6 >= 6)  # True

# Less than or equal to
print(2 <= 5)  # True
```

### Logical Operators

Logical operators are used to combine conditional statements.

- **AND (`and`)**: Returns `True` if both statements are true.
- **OR (`or`)**: Returns `True` if at least one statement is true.
- **NOT (`not`)**: Reverses the result, returns `False` if the result is true.

#### Examples of Logical Operators
> You can run any of these examples in an `.ipynb` inside of VSCode, or in a Colab notebook.

```python
# AND
print(True and True)  # True
print(True and False)  # False

# OR
print(True or False)  # True
print(False or False)  # False

# NOT
print(not True)  # False
print(not False)  # True
```

## Expressions in Python

Expressions are combinations of variables, operators, and values that produce a result. They are the building blocks of any Python program.

### Combining Variables and Operators

You can combine variables and operators to create expressions. Here are some examples:
> You can run any of these examples in an `.ipynb` inside of VSCode, or in a Colab notebook.

```python
# Arithmetic expression
x = 5
y = 3
result = x + y
print("x + y =", result)

# Comparison expression
is_greater = x > y
print("x > y:", is_greater)

# Logical expression
is_true = (x > y) and (y > 0)
print("(x > y) and (y > 0):", is_true)
```
## Exercise: Working with Operators and Expressions

Now it's time to practice using operators and creating expressions. You can do this your own Colab Notebook, in an `.ipynb` file in VSCode, or in a Python file in VSCode (we haven't done this last one yet - if you'd like to try,ask a chatbot or your professor!).

Try the following exercises:

### Exercise 1: Arithmetic Operators

Write a Python program that performs the following operations and prints the results:

1. Add two numbers.
2. Subtract one number from another.
3. Multiply two numbers.
4. Divide one number by another.
5. Find the remainder of the division of two numbers.
6. Raise one number to the power of another.

### Exercise 2: Comparison Operators

Write a Python program that compares two numbers using each of the comparison operators and prints the results.

### Exercise 3: Logical Operators

Write a Python program that uses logical operators to combine multiple conditions and prints the results.

### Exercise 4: Creating Expressions

Write a Python program that combines variables and operators to create expressions. Use arithmetic, comparison, and logical operators in your expressions.

## Reflect

Think about the different types of operators and expressions you've learned. How might you use them in your own programs? What are some real-world scenarios where these concepts might be useful?

## Review

In this step, we learned about different types of operators and expressions in Python. Here's a quick recap:

- **Arithmetic Operators**: Used to perform mathematical operations.
- **Comparison Operators**: Used to compare two values and return a boolean result.
- **Logical Operators**: Used to combine conditional statements.
- **Expressions**: Combinations of variables, operators, and values that produce a result.

Understanding these concepts is essential for writing effective and efficient code in Python.
