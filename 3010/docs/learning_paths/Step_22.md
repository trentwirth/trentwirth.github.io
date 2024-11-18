# Step 22

## **Basic Statistics**

In this step, we'll apply statistical methods to the reaction time dataset generated in the previous steps. This dataset includes data related to reaction times for trials where the independent variable (IV) is the color of a circle. Here's what we aim to accomplish:

### Objectives
1. Establish the dataset.
2. Compute basic descriptives and create plots suitable for a paired samples t-test.
3. Perform and interpret a paired samples t-test.
4. Manipulate the dataset to add an additional variable, *previous circle color*.
5. Set up and run a two-way ANOVA to investigate interactions between the current circle color and the previous circle color.

---

### Step 1: Establish the Dataset
We begin by loading the dataset used in the previous step.

```python
import pandas as pd

# Assuming the reaction time dataset from Step 21 is saved as 'reaction_times.csv'
data = pd.read_csv('reaction_times.csv')

# Display the first few rows to confirm structure
print(data.head())
```

---

### Step 2: Descriptives and Paired Samples T-Test Preparation
To prepare for the paired samples t-test:
- Compute summary statistics for each circle color.
- Visualize the data with plots to check assumptions like normality.

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Group by circle color and calculate summary statistics
descriptives = data.groupby('circle_color')['reaction_time'].describe()

# Boxplot to visualize reaction times by circle color
sns.boxplot(x='circle_color', y='reaction_time', data=data)
plt.title('Reaction Times by Circle Color')
plt.show()

# Print descriptive statistics
print(descriptives)
```

---

### Step 3: Perform the Paired Samples T-Test
A paired samples t-test compares reaction times between two conditions.

```python
from scipy.stats import ttest_rel

# Perform paired t-test
group1 = data[data['circle_color'] == 'red']['reaction_time']
group2 = data[data['circle_color'] == 'blue']['reaction_time']

t_stat, p_value = ttest_rel(group1, group2)

# Display results
print(f"Paired Samples T-Test:\nT-Statistic = {t_stat}, p-value = {p_value}")
```

**Interpretation:** Based on the p-value, determine if there is a significant difference between reaction times for red and blue circles.

---

### Step 4: Add *Previous Circle Color* Variable
To explore potential effects of *previous circle color*, add this column to the dataset. The first trial is excluded as it lacks a "previous" circle.

```python
# Shift the 'circle_color' column to create the 'previous_circle_color' column
data['previous_circle_color'] = data['circle_color'].shift(1)

# Drop the first row as it lacks a previous circle color
data = data.dropna().reset_index(drop=True)

# Display the updated dataset
print(data.head())
```

---

### Step 5: Two-Way ANOVA
Now, we'll investigate the effects of the current and previous circle colors using a two-way ANOVA. We hypothesize that the interaction of these variables might influence reaction times.

#### Setting Up the Analysis
```python
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# Define the model
model = ols('reaction_time ~ C(circle_color) * C(previous_circle_color)', data=data).fit()

# Perform the ANOVA
anova_results = anova_lm(model, typ=2)

# Display ANOVA table
print(anova_results)
```

---

### Step 6: Visualizing the Interaction
Visualize the interaction effect between the current and previous circle colors.

```python
# Interaction plot
sns.pointplot(
    x='circle_color', 
    y='reaction_time', 
    hue='previous_circle_color', 
    data=data,
    ci=None
)
plt.title('Interaction Between Current and Previous Circle Colors')
plt.show()
```

---

### Conclusion
In this step, we:
1. Established the reaction time dataset and computed basic statistics.
2. Conducted a paired samples t-test to evaluate differences between red and blue circles.
3. Introduced a new variable (*previous circle color*) and examined its influence alongside the current circle color.
4. Performed a two-way ANOVA and visualized the interaction effect.

These analyses provide insights into how circle color, both current and previous, may influence reaction times.
