# Step 8

In Step 8, we will reinforce our understanding of functions by combining them with loops, conditionals, and type hints. This step will provide opportunities to practice and see how these concepts work together.

## Simple Function

Let's start with a simple function that adds two numbers.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

In this example, `add` is a function that takes two parameters `a` and `b`, and returns their sum.

## Using a Function in a Loop

Now, let's see how we can use this function in a loop to add numbers from a list.

```python
def add(a, b):
    return a + b

numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total = add(total, number)

print(total)
```

In this example, we use the `add` function in a `for` loop to sum all the numbers in the list.

## Functions with Various Data Types

Functions can work with different data types and return various outputs. Let's see some examples.

### Example 1: Concatenating Strings

```python
def concatenate(str1, str2):
    return str1 + " " + str2

result = concatenate("Hello", "World")
print(result)
```

### Example 2: Checking Even or Odd

```python
def is_even(number):
    if number == 0:
        return False # Zero is not considered even or odd, it is an "edge case"
                     # so we'll take care of it first.
    else:
        return number % 2 == 0 # Now that zero is taken care of, 
                               # this will work fine.

result = is_even(4)
print(result)
```

### Example 3: Finding the Maximum Value

```python
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

result = find_max(10, 20)
print(result)
```

## Introducing Type Hints

Type hints allow you to specify the expected data types of function parameters and return values. They do not enforce the types but provide useful information for code readability. 

### Syntax

Below is a template for how a functino with type hints would work, note, these are not real types:

```python
def function_name(parameter: type) -> return_type:
    # code block
```

??? Tip "Why Type Hints are Important"

    Type hints improve code readability and help others understand what types of arguments a function expects and what it returns. They also assist in catching type-related errors during development.

Note, we are not changing anything about the function here. All we're doing is being *more communicative* about how the function should be used.

Below are some examples of functions with type hints.

#### Example 1: Adding Integers

```python
def add(a: int, b: int) -> int:
    return a + b

result = add(3, 5)
print(result)
```

This function is pretty simple, it takes two integers, adds them together, and returns an integer.

#### Example 2: Concatenating Strings

```python
def concatenate(str1: str, str2: str) -> str:
    return str1 + " " + str2

result = concatenate("Hello", "World")
print(result)
```

"Concatenate" means to join two things together. In this case, two strings.

This function takes two strings and returns a new string that is the concatenation of the two input strings.

??? Tip "Easier String Concatenation"

    [You can follow this link](https://www.w3schools.com/python/python_strings_concatenate.asp) to see more about string concatenation in Python.

#### Example 3: Checking Even or Odd

```python
def is_even(number: int) -> bool:
    if number == 0:
        return False 
    else:
        return number % 2 == 0

result = is_even(4)
print(result)

```
Note, we used this function before, all we've changes is that we now have type hints!

### What when we feed a function the wrong type?

```python
def add(a: int, b: int) -> int:
    return a + b

result = add("3", 5)  # This will produce an error...
```

This will raise a `TypeError` because we are trying to add a string and an integer, which is not allowed based on the type hints. In this case, it will also functionally break the code.

The type error will look like this:
```
TypeError: can only concatenate str (not "int") to str
```

Note, if you fed the `add()` function a *float*, even though it breaks the Type Hint, the code will still run. This is because Python is a "dynamically typed language", and it will try to do the operation you're asking it to do and only break if it can't.

So, Type Hints are not a "hard rule" in Python, but they are a great idea to follow because **code is read more often than it is written**.

## Using a Loop within a Function

You can use loops within functions to perform repetitive tasks.

### Example: Summing Numbers

```python
def sum_numbers(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

result = sum_numbers(10)
print(result)
```

The example above takes in an integer `n` and returns the sum of all numbers from 1 to `n`. It uses the range function to generate a sequence of numbers from 1 to `n` - remember that range doesn't include the last number, so we add 1 to `n` + 1 so that we include `n` in the sum.

## Combining Functions with Conditionals

You can combine functions with conditionals to perform different actions based on conditions.

### Example: Filtering Even Numbers

> NOTE: For the function below, `is_even` is a function that we defined earlier in this document. That means if you've run the `is_even` function in your `.ipynb` already, then this code will work just fine. If you haven't, you'll need to run the code block containing `is_even` function before you run this code.

```python
def filter_even(numbers: list[int]) -> list[int]:
    even_numbers = []
    for number in numbers:
        if is_even(number):
            even_numbers.append(number)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_even(numbers)
print(result)
```

This above function is great! It contains a loop that iterates over a list of numbers and uses the `is_even` function to check if each number is even. If the number is even (here, we use a conditional!), it is added to a new list called `even_numbers`, which is then returned.

This function combines a lot of what we've learned so far!

## Review

In this step, we reinforced our understanding of functions by exploring:

- **Simple Function**: Creating and using a basic function.
- **Using a Function in a Loop**: Applying a function within a loop.
- **Functions with Various Data Types**: Working with different data types and return values.
- **Introducing Type Hints**: Specifying expected data types for function parameters and return values.
- **Using a Loop within a Function**: Performing repetitive tasks within a function.
- **Combining Functions with Conditionals**: Using conditionals within functions to perform different actions.

Understanding these concepts is essential for writing robust and flexible code in Python.

## Exercises

> Rememeber: The solutions I provide are only one way to solve the problem. There are many ways to solve most coding problems! You should feel free to experiment and try different approaches.

1. **Type Hints**: Write a function called `concat` that takes two strings as parameters and returns their concatenation. Use type hints to specify the parameter and return types.

    ??? Tip "Solution"
        ```python
        def concat(str1: str, str2: str) -> str:
            return str1 + " " + str2

        result = concat("Hello", "World")
        print(result)
        ```

2. **Sum of Squares**: Write a function called `sum_of_squares` that takes an integer `n` and returns the sum of the squares of all numbers from 1 to `n`.

    ??? Tip "Solution"
        ```python
        def sum_of_squares(n: int) -> int:
            total = 0
            for i in range(1, n + 1):
                total += i ** 2
            return total

        result = sum_of_squares(5)
        print(result)
        ```

3. **Count Vowels**: Write a function called `count_vowels` that takes a string as a parameter and returns the number of vowels in the string. Use a loop to iterate over the string and count the vowels.

    ??? Tip "Solution"

        ```python
        def count_vowels(s: str) -> int:
            vowels = "aeiouAEIOU"
            count = 0
            for char in s:
                if char in vowels:
                    count += 1
            return count

        result = count_vowels("Hello, World!")
        print(result)
        ```

4. **Find Minimum**: Write a function called `find_min` that takes a list of integers and returns the smallest number in the list. Use a loop to iterate over the list and find the minimum value.


    ??? Tip "Solution"
        ```python
        def find_min(numbers: list[int]) -> int:
            min_number = numbers[0]
            for number in numbers:
                if number < min_number:
                    min_number = number
            return min_number

        numbers = [5, 3, 8, 1, 9, 2]
        result = find_min(numbers)
        print(result)
        ```

5. **Palindrome Check**: Write a function called `is_palindrome` that takes a string and returns `True` if the string is a palindrome (reads the same forwards and backwards) and `False` otherwise. Use a loop to check the characters.

    ??? Tip "Solution"

        ```python
        def is_palindrome(input_string: str) -> bool:
            input_string = input_string.lower() # This line makes it so we don't have to worry about capital letters.
            reversed_input_string = input_string[::-1]
            return input_string == reversed_input_string

        result1 = is_palindrome("radar")
        result2 = is_palindrome("hello")
        print(result1)
        print(result2)
        ```

## Bonus: Lambda Functions (One-Line Functions)

Lambda functions are small functions defined using the `lambda` keyword. They are often used for short, simple operations.

These are called "anonymous functions" because they don't have a name, we don't define ("`def`") them. They are useful when you need a simple function for a short period of time.

### Syntax

Note, the text below is a template, not real code:
```python
lambda parameters: expression
```

### Example: Squaring a Number

```python
square = lambda x: x * x
print(square(5))
```

### Example: Using Lambda with `filter`

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
```
of course, the above code has the 0 edge case... but hopefully this gives you an idea.

## Bonus Excercise: Using Lambda Functions

1. **Filtering Odd Numbers**: Use a lambda function with the `filter` function to filter out odd numbers from a list of integers.

    ??? Tip "Solution"

        ```python
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
        print(odd_numbers)
        ```

2. **Adding "1"**: With a super simple lambda function, add 1 to a number.

    ??? Tip "Solution"

        ```python
        add_one = lambda x: x + 1
        print(add_one(5))
        ```
