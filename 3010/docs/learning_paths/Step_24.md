# Step 24: Fine-Tuning Figures in Matplotlib

In this step, we explore fine-tuning Matplotlib visualizations for enhanced customizability. We'll use the `all_data` dataset generated in Step 21 to create overlapping histograms with Probability Density Functions (PDFs) and legends. Along the way, we'll explain specific parts of the code you'll modify or customize in each section.

---

### 1. Setting Up Our Data
We start by filtering the `all_data` dataframe to create two datasets based on `circle_color`. These will serve as the reaction time data for the two groups (orange and blue).

**Dataset Setup:**

- `orange_reactiontime_df`: Contains reaction times for trials where `circle_color` is `'orange'`.
- `blue_reactiontime_df`: Contains reaction times for trials where `circle_color` is `'blue'`.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Assuming all_data is already loaded
# If you do not have it yet, go back to Step 21 and load it as instructed
all_data = pd.read_csv('reaction_time_data.csv')  # Replace with actual file path
# If you've already got `all_data` loaded, you can skip this step by commenting it out

# Create datasets for the two groups
orange_reactiontime_df = all_data[all_data['circle_color'] == 'orange']['reaction_time']
blue_reactiontime_df = all_data[all_data['circle_color'] == 'blue']['reaction_time']

# Preview the datasets
print("Orange Reaction Times:\n", orange_reactiontime_df.head())
print("Blue Reaction Times:\n", blue_reactiontime_df.head())
```

**Key Parts to Check:**

- Ensure `all_data` is loaded correctly and contains the expected columns (`reaction_time`, `circle_color`).
- Replace `'reaction_time_data.csv'` with the actual file name/path if needed.

---

### 2. Creating Independent Histograms
Now that we have two different dataframes, lSet's create histograms for the orange and blue reaction times individually.

```python
# Orange Reaction Time Histogram
plt.figure(figsize=(8, 6))
plt.hist(orange_reactiontime_df, bins=20, color='orange', alpha=0.6, label='Orange')
plt.title('Histogram of Reaction Times: Orange')
plt.xlabel('Reaction Time (ms)')
plt.ylabel('Frequency')
plt.show()

# Blue Reaction Time Histogram
plt.figure(figsize=(8, 6))
plt.hist(blue_reactiontime_df, bins=20, color='blue', alpha=0.6, label='Blue')
plt.title('Histogram of Reaction Times: Blue')
plt.xlabel('Reaction Time (ms)')
plt.ylabel('Frequency')
plt.show()
```

**Key Parts to Modify:**

- `bins=20`: Adjust the number of bins (granularity) if needed.
- `color='orange'` and `color='blue'`: Customize colors as desired.
- `alpha=0.6`: Adjust transparency (range: 0 to 1).

!!! Tip "IpyWidget to Play with `alpha` value"
    You can use an IpyWidget to interactively adjust the `alpha` value and see the visual effect it has on the histogram. 

    This will be cooler to do when we overlap our histograms later, but for now here's an example:
    
    ```python
    from ipywidgets import interact

    @interact(alpha=(0, 1, 0.05))
    def plot_histogram(alpha=0.6):
        plt.figure(figsize=(8, 6))
        plt.hist(orange_reactiontime_df, bins=20, color='orange', alpha=alpha, label='Orange')
        plt.title('Histogram of Reaction Times: Orange')
        plt.xlabel('Reaction Time (ms)')
        plt.ylabel('Frequency')
        plt.show()
    ```

    This code snippet creates an interactive slider for the `alpha` value, allowing you to see the histogram change in real-time.

    *What other ways could you use an IpyWidgets to interact with your data?*

---

### 3. Combining into a Two-Paneled Plot
Two histograms are cool, but it would be nice if they were attached/connected in some way. We can create a side-by-side comparison of the two histograms using subplots!

To do this, we'll set up a `fig` figure object with a corresponding `axs` array to hold the two subplots and then plot the histograms for orange and blue reaction times in each panel.

```python
fig, axs = plt.subplots(1, 2, figsize=(12, 6), constrained_layout=True)

# Panel 1: Orange
axs[0].hist(orange_reactiontime_df, bins=20, color='orange', alpha=0.6, label='Orange')
axs[0].set_title('Orange Reaction Times')
axs[0].set_xlabel('Reaction Time (ms)')
axs[0].set_ylabel('Frequency')

# Panel 2: Blue
axs[1].hist(blue_reactiontime_df, bins=20, color='blue', alpha=0.6, label='Blue')
axs[1].set_title('Blue Reaction Times')
axs[1].set_xlabel('Reaction Time (ms)')

plt.suptitle('Reaction Times by Circle Color')
plt.show()
```

**Key Parts to Modify:**

- `figsize=(12, 6)`: Change plot size if necessary.
- Customize subplot titles and labels as needed.

!!! Tip "figure fun" 
    You can also use the `fig` object to save your figure to a file. For example, `fig.savefig('reaction_time_histograms.png')` will save the figure as a PNG file in the current directory.

    You can also adjust the layout using `fig.tight_layout()`, or set a global title with `fig.suptitle('Overall Title')`.

---

### 4. Overlapping Histograms with PDFs
One of my favorite ways to display/compare histograms is to combine the two datasets into a single plot, overlaying histograms. We can then calculate and plot probability density function for each dataset to visualize the distribution more clearly.

!!! Tip "What's a Probability Density Function (PDF)?"
    A Probability Density Function (PDF) is a statistical function that describes the likelihood of a continuous random variable falling within a particular range. In this case, we're using the normal distribution PDF to model the reaction time data.

    The `norm.pdf()` function from `scipy.stats` calculates the PDF of a normal distribution given a set of values, mean, and standard deviation.

    The normal curve helps us visualize how the data is distributed around the mean and how likely certain values are.

```python
plt.figure(figsize=(10, 6))

# Orange Histogram and Curve
plt.hist(orange_reactiontime_df, bins=20, color='orange', alpha=0.4, label='Orange', density=True)
plt.plot(
    np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
    norm.pdf(
        np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
        np.mean(orange_reactiontime_df),
        np.std(orange_reactiontime_df),
    ),
    color='orange',
    linestyle='--',
    linewidth=2,
    label='Orange PDF',
)

# Blue Histogram and Curve
plt.hist(blue_reactiontime_df, bins=20, color='blue', alpha=0.4, label='Blue', density=True)
plt.plot(
    np.linspace(blue_reactiontime_df.min(), blue_reactiontime_df.max(), 500),
    norm.pdf(
        np.linspace(blue_reactiontime_df.min(), blue_reactiontime_df.max(), 500),
        np.mean(blue_reactiontime_df),
        np.std(blue_reactiontime_df),
    ),
    color='blue',
    linestyle='-',
    linewidth=2,
    label='Blue PDF',
)

plt.title('Overlapping Reaction Time Histograms with PDF Curves')
plt.xlabel('Reaction Time (ms)')
plt.ylabel('Density')
plt.legend()
plt.show()
```

**Key Parts to Modify:**

- Adjust the `np.linspace` range to fit the specific dataset more tightly.
- Modify `linestyle='--'` or `linewidth=2` for the curves as needed.

#### Breaking down the PDF Calculation:

The following code snippet is what calculates the PDF line for the orange histogram:

```python
plt.plot(
    np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
    norm.pdf(
        np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
        np.mean(orange_reactiontime_df),
        np.std(orange_reactiontime_df),
    ),
    color='orange',
    linestyle='--',
    linewidth=2,
    label='Orange PDF Curve',
)
```

Let's break it down piece by piece:

- `np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500)`: This creates 500 evenly spaced points between the minimum and maximum reaction times in the orange dataset. This range is used to calculate the PDF values.
- `norm.pdf(...)`: This calculates the PDF values for the given range using the mean and standard deviation of the orange dataset.
- `np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500)`: This is the range of x-values for the PDF curve, we repeat it here to ensure the x-values match the PDF values.
- `np.mean(orange_reactiontime_df)`: The mean of the orange reaction times. This is used as the center of the normal distribution.
- `np.std(orange_reactiontime_df)`: The standard deviation of the orange reaction times. This controls the spread of the normal distribution.
- color, linestyle, linewidth, label: These are used to customize the appearance of the PDF curve and how it appears in the legend (respectively).

---

### 5. Fine-Tuning and Customizing
Add legends, gridlines, and vertical lines indicating mean reaction times.

```python
plt.figure(figsize=(10, 6))

# Histograms
plt.hist(orange_reactiontime_df, bins=20, color='orange', alpha=0.5, label='Orange', density=True)
plt.hist(blue_reactiontime_df, bins=20, color='blue', alpha=0.5, label='Blue', density=True)

# PDFs
plt.plot(
    np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
    norm.pdf(
        np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
        np.mean(orange_reactiontime_df),
        np.std(orange_reactiontime_df),
    ),
    color='orange',
    linestyle='--',
    linewidth=2,
    label='Orange PDF Curve',
)
plt.plot(
    np.linspace(blue_reactiontime_df.min(), blue_reactiontime_df.max(), 500),
    norm.pdf(
        np.linspace(blue_reactiontime_df.min(), blue_reactiontime_df.max(), 500),
        np.mean(blue_reactiontime_df),
        np.std(blue_reactiontime_df),
    ),
    color='blue',
    linestyle='-',
    linewidth=2,
    label='Blue PDF Curve',
)

# Customizations
plt.title('Customized Reaction Time Histograms')
plt.xlabel('Reaction Time (ms)')
plt.ylabel('Density')
plt.grid(visible=True, which='both', linestyle='--', alpha=0.6)
plt.axvline(np.mean(orange_reactiontime_df), color='orange', linestyle='-', label='Mean Orange')
plt.axvline(np.mean(blue_reactiontime_df), color='blue', linestyle='-', label='Mean Blue')
plt.legend(loc='upper right', frameon=True, fontsize=10)

plt.show()
```

**Key Parts to Modify:**

- Adjust `plt.grid(...)` for appearance.
- Add or adjust vertical lines (`plt.axvline(...)`) for additional statistical markers.

### 6. Cleaning Up Your Figure

One thing you might notice is that at this point, our figure is pretty bloated. We really don't need all that information hanging out in the legend, for example.

We can spend some time going back into our figure and cleaning up the code to make it appear a bit nicer, and more publication-ready. We can...

- Remove unnecessary labels from the legend.
- Adjust the font size of the legend so that they're all legible.
- Remove the gridlines if they're not necessary.
- Adjust the bin size of the histograms so that they're the same width for both groups.
- Remove tick marks on the y-axis to clean up the figure.

#### First, we're going to calculate bin sizes for the histograms so that they're the same width for both groups.

```python

# Define bin size
bin_size = 50  # for example, 50 ms

# Calculate bin edges
orange_bins = np.arange(min(orange_reactiontime_df), max(orange_reactiontime_df) + bin_size, bin_size)
blue_bins = np.arange(min(blue_reactiontime_df), max(blue_reactiontime_df) + bin_size, bin_size)
```
#### Now, we'll implement these bin sizes in our histograms.

```python
plt.figure(figsize=(10, 6))

# Histograms
plt.hist(orange_reactiontime_df, bins=orange_bins, color='orange', alpha=0.5, label='Orange', density=True)
plt.hist(blue_reactiontime_df, bins=blue_bins, color='blue', alpha=0.5, label='Blue', density=True)

# PDFs
plt.plot(
    np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
    norm.pdf(
        np.linspace(orange_reactiontime_df.min(), orange_reactiontime_df.max(), 500),
        np.mean(orange_reactiontime_df),
        np.std(orange_reactiontime_df),
    ),
    color='orange',
    linestyle='--',
    linewidth=2,
    # remove unnecessary legend label; orange = color orange, blue = blue.
)
plt.plot(
    np.linspace(blue_reactiontime_df.min(), blue_reactiontime_df.max(), 500),
    norm.pdf(
        np.linspace(blue_reactiontime_df.min(), blue_reactiontime_df.max(), 500),
        np.mean(blue_reactiontime_df),
        np.std(blue_reactiontime_df),
    ),
    color='blue',
    linestyle='-',
    linewidth=2,
)

# Customizations
plt.title('Customized Reaction Time Histograms', fontsize=20)
plt.xlabel('Reaction Time (ms)', fontsize=16)
plt.ylabel('Density', fontsize=16)
plt.grid(visible=True, which='both', linestyle='-', alpha=0.6) # Change linestyle to '-'
plt.axvline(np.mean(orange_reactiontime_df), color='orange', linestyle='-')
plt.axvline(np.mean(blue_reactiontime_df), color='blue', linestyle='-')

# Clean up the legend
plt.legend(loc='upper right', frameon=True, fontsize=12) # Increase font size
plt.tick_params(axis='both', which='both', length=0) # Hide tick marks on the edge

plt.show()
```

#### Other things to consider

There are more ways you could customize this plot...

- You could add texture to the bars of the histogram to make them more visually distinct
- You could make sure your histograms start at the same value so that the bins are perfectly aligned
- ... and more!

---

### Summary

In this *final* step of our learning path, we've explored fine-tuning Matplotlib visualizations to create publication-quality figures. By layering histograms, PDFs, and annotations, we've enhanced the clarity and visual appeal of our data representations. These techniques can be applied to a wide range of datasets and research questions, allowing you to create compelling visualizations that effectively communicate your findings.

Now you should have everything you need to create a publication-quality figure in Python!