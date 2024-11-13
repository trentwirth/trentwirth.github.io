# Step 19

In this step, we’ll explore **Pandas**, a powerful Python library for data manipulation and analysis. Pandas provides tools to explore, manipulate, and analyze datasets efficiently, which is essential for behavioral scientists working with real-world data.

We’ll use a CSV file named `happiness correlation data-2.csv`, which you can download below. Each row represents data from one participant, with columns capturing various aspects like age, work hours, GPA, life satisfaction, and more.

## 0. Download the Dataset

[Click this link to download the data](<files/happiness correlation data-2.csv>)

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