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