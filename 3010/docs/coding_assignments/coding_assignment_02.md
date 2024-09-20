# Coding Assignment 2

> Note: You should only begin this assignment when you have completed Step 8 of the Learning Path.

This assignment will test your understanding of the concepts covered up to Step 8 of the Learning Path. You will be asked to write Python code to solve a series of problems.

I will ask you to write blocks of code that will end with certain results/functionality. As a part of your assignment, you might need to explain how the resulting functionality is useful.

## Problem 1: Conditionals - positive, negative, or zero?

Write a Python program that checks if a number is positive, negative, or zero and prints the result using [f-strings](https://www.w3schools.com/python/python_string_formatting.asp).

The code block should look something like this (you can copy and paste this into your Python notebook to work off of it, that's true for all the problems):

```python
# We should be able to enter any number here
number = 

# ... your code here ...

print( ... your code here ... ) 
# This should print whether the number is positive, negative, or zero.
```

The print statement should be informative, and explain why the output itself is useful.

## Problem 2: Odd or Even, in a loop!

Write a Python program that loops through numbers 1 to 10, checks whether each number is odd or even using a function, and then prints the result.

The code doesn't require an explanatory comment.

Work off the following code block:

```python
def is_odd_or_even(number):
    # ... your code here ...
    return result

# Loop through numbers 1 to 10, use the function in the loop.
for number in range(_, _): # Replace the underscores with the correct values that will make the range function work as we want it to.

    # ... your code here ...

```
!!! tip "Print in the Loop"
    You should print the result of the function inside the loop, so that you can see the result for each number.

## Problem 3: Filtering Students by Grades

Write a Python program that checks through two lists: one with letter grades for students and another with the students' initials. Assume that the position of each student's initials is paired with the letter grade of the same position.

The task is to print out all students who got an A or a B using a combination of loops, conditionals, and a function (include appropriate type hints for your function).

Work off of the following code block:

```python

# Example lists
grades = ['A', 'C', 'B', 'D', 'A', 'F']
initials = ['ABB', 'CDT', 'EFJ', 'GHR', 'IJK', 'LWN']

def filter_students_by_grade(grades, initials): # be sure to add type hints
    # ... your code here ...
    return # ... your code here ...

# Call the function and print the result
result = filter_students_by_grade(_, _) # Replace the underscores with the variable names
print(f"") # Add a descriptive print statement here using f-strings
# Explain why this output is useful in a comment.
```

!!! tip "If you are taking this class for credit at UC..."
    Save all of your problems as an `.ipynb` file and submit it to the appropriate assignment on Canvas.
