# Step 24: Fine-Tuning Figures in Matplotlib

In this step, we explore fine-tuning Matplotlib visualizations for enhanced customizability. We'll use the `all_data` dataset generated in Step 21 to create overlapping histograms with normality curves and legends. Along the way, we'll explain specific parts of the code you'll modify or customize in each section.

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
Let's create histograms for the orange and blue reaction times individually.

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

---

### 3. Combining into a Two-Paneled Plot
Create a side-by-side comparison of the two histograms using subplots.

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

---

### 4. Overlapping Histograms with Normality Curves
Combine the two datasets into a single plot, overlaying histograms with normality curves.

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
    label='Orange Normal Curve',
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
    linestyle='--',
    linewidth=2,
    label='Blue Normal Curve',
)

plt.title('Overlapping Reaction Time Histograms with Normality Curves')
plt.xlabel('Reaction Time (ms)')
plt.ylabel('Density')
plt.legend()
plt.show()
```

**Key Parts to Modify:**

- Adjust the `np.linspace` range to fit the specific dataset more tightly.
- Modify `linestyle='--'` or `linewidth=2` for the curves as needed.

---

### 5. Fine-Tuning and Customizing
Add legends, gridlines, and vertical lines indicating mean reaction times.

```python
plt.figure(figsize=(10, 6))

# Histograms
plt.hist(orange_reactiontime_df, bins=20, color='orange', alpha=0.5, label='Orange', density=True)
plt.hist(blue_reactiontime_df, bins=20, color='blue', alpha=0.5, label='Blue', density=True)

# Normality Curves
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
    label='Orange Normal Curve',
)
plt.plot(
    np.linspace(blue_reactiontime_df.min(), blue_reactiontime_df.max(), 500),
    norm.pdf(
        np.linspace(blue_reactiontime_df.min(), blue_reactiontime_df.max(), 500),
        np.mean(blue_reactiontime_df),
        np.std(blue_reactiontime_df),
    ),
    color='blue',
    linestyle='--',
    linewidth=2,
    label='Blue Normal Curve',
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


---

### Summary
- **Dynamic Dataset Filtering**: Use the `circle_color` column to segment data dynamically.
- **Customizable Visualizations**: Adjust plot elements like colors, transparency, and line styles for clarity.
- **Fine-Tuned Visualizations**: Create publication-quality visualizations by layering data and annotations.