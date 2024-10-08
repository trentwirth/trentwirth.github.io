# Step 7

In Step 7, we will explore functions in Python. Functions are reusable blocks of code that perform a specific task. They help us organize our code, make it more readable, and avoid repetition.

## Defining Functions

To define a function in Python, we use the `def` keyword (short for "define") followed by the function name and parentheses `()`. 

Inside the parentheses, we can specify parameters, or "inputs", that the function can accept. The function body is indented and contains the code that will be executed when the function is called.

### Syntax

```python
def function_name(parameters):
    # code block to be executed
```

### Example

```python
def greet(name):
    print(f"Hello, {name}!")
```

In this example, `greet` is the function name, and `name` is a parameter. The function prints a greeting message using the provided name.

## Calling Functions

To call a function, we use the function name followed by parentheses `()`. If the function accepts parameters, we pass the arguments inside the parentheses.

### Example

```python
greet("Alice")
```

This will output:

``` 
Hello, Alice!
```


## Return Statement

Functions can return a value using the `return` statement. This allows us to capture the result of a function and use it in other parts of our code.

### Example

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

This will output:

```
8
```

## Default Parameters

We can define default values for parameters in a function. If an argument is not provided when the function is called, the default value will be used.

### Example

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()
```

This will output:

```
Hello, World!
```

by default, the function uses "World" as the name. If we call the function without providing a name, it will use the default value, like this:

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet("Alice")

```

This will output:

``` 
Hello, Alice!
```

Try it yourself!


## Keyword Arguments

We can more flexibly use functions by telling the function what we want to use as input when we call that function.

Let's imagine a scenario where we have a "describe_pet" function that takes two parameters: "animal_type" and "pet_name", the function might look like this:

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")
```

We can specify the inputs, or "arguments", when we call the function by setting them equal to the parameter names. 

!!! Tip "Parameters & Arguments"
    The parameter is the name we give to the input in the function definition, and the argument is the actual value we pass to the function.

Here is an example of specifying that I have a dog named Rufus:
```python

describe_pet(animal_type="dog", pet_name="Rufus")
```

Note that when I specify the arguments (inputs), I can change the order and the function will work just fine:

```python
describe_pet(pet_name="Django", animal_type="dog")
```

So, in the code below, I can define the function and use the function twice in a row, changing the order of the arguments:

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type="dog", pet_name="Sherlock")
describe_pet(pet_name="Watson", animal_type="cat")
```

This will output:

```
I have a dog named Sherlock. I have a cat named Watson.
```


## Exercises

1. **Define a Function**: Write a function called `square` that takes a number as a parameter and returns its square.

    ??? Tip "Solution"
        ```python
        def square(number):
            return number * number

        result = square(5)
        print(result)
        ```

2. **Call a Function**: Write a function called `multiply` that takes two numbers as parameters and returns their product. Call the function with different arguments and print the results.

    ??? Tip "Solution"
        ```python
        def multiply(a, b):
            return a * b

        result1 = multiply(3, 4)
        result2 = multiply(5, 2)
        print(result1)
        print(result2)
        ```

3. **Default Parameters**: Write a function called `greet_user` that takes a name as a parameter and prints a greeting message. If no name is provided, it should use "User" as the default name.

    ??? Tip "Solution"
        ```python
        def greet_user(name="User"):
            print(f"Hello, {name}!")

        greet_user("Alice")
        greet_user()
        ```

4. **Keyword Arguments**: Write a function called `make_sandwich` that takes a list of ingredients and prints a message describing the sandwich. Call the function using keyword arguments to specify the ingredients in different orders.

    ??? Tip "Solution"
        ```python
        def make_sandwich(ingredients):
            print("Sandwich with:")
            for ingredient in ingredients:
                print(f"- {ingredient}")

        make_sandwich(ingredients=["bread", "cheese", "tomato"])
        make_sandwich(ingredients=["tomato", "bread", "cheese"])
        ```

## Reflect

Think about how functions can help you organize your code and make it more reusable. What are some real-world scenarios where you might use functions?

## Review

In this step, we learned about functions in Python. Here's a quick recap:

- **Defining Functions**: Use the `def` keyword to define a function.
- **Calling Functions**: Use the function name followed by parentheses to call a function.
- **Return Statement**: Use the `return` statement to return a value from a function.
- **Default Parameters**: Define default values for parameters in a function.
- **Keyword Arguments**: Specify arguments using parameter names when calling a function.

Understanding these concepts is essential for writing organized and reusable code in Python.
