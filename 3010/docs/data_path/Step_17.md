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