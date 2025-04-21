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

### 1: Establish the Dataset
We will start with the `all_data` dataset generated in Step 21. This dataset contains reaction times for trials where the circle color is the independent variable.

Go back to Step 21 to get the `all_data` dataframe, when you do you should be able to run the code below and get the following result.

Code:

```python
all_data.head()
```

Result:
```python
	subject_id	reaction_time	circle_color	key_pressed	accuracy
0	    1	        445.0	        orange	        j	       True
1	    1	        386.0	        blue	        f	       True
2	    1	        366.0	        blue	        f	       True
3	    1	        374.0	        orange	        j	       True
4	    1	        409.0	        orange	        j	       True
```

---

### 2: Descriptives and Paired Samples T-Test Preparation
To prepare for the paired samples t-test:
- Compute summary statistics for each circle color.
- Visualize the data with plots to check assumptions like normality.

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Group by circle color and calculate summary statistics
descriptives = all_data.groupby('circle_color')['reaction_time'].describe()

# Boxplot to visualize reaction times by circle color
sns.boxplot(x='circle_color', y='reaction_time', data=all_data)
plt.title('Reaction Times by Circle Color')
plt.show()

# Print descriptive statistics
print(descriptives)
```

---

### 3: Perform the Paired Samples T-Test
A paired samples t-test compares reaction times between two conditions.

!!! Tip "pip install `scipy`"
    At this point you'll most likely need to install the `scipy` package. You can do this by running `%pip install scipy` in your notebook.

    What's `scipy`? Think of it as "scientific Python" - it's a library that provides many user-friendly and efficient numerical routines andf functions that are commonly used in scientific and engineering applications.

```python
from scipy.stats import ttest_rel

# Perform paired t-test
group1 = all_data[all_data['circle_color'] == 'orange']['reaction_time'] # Orange circle
group2 = all_data[all_data['circle_color'] == 'blue']['reaction_time'] # Blue circle

t_stat, p_value = ttest_rel(group1, group2)

# Display results
print(f"Paired Samples T-Test:\nT-Statistic = {t_stat}, p-value = {p_value}")
```

**Interpretation:** Based on the p-value, determine if there is a significant difference between reaction times for orange and blue circles.

??? Tip "Check your results"
    If you ran it correctly, you should get the following output:
    ```python
    # Paired Samples T-Test:
    # T-Statistic = -0.2520879211177987, p-value = 0.8010674499745879
    ```
    The p-value is greater than 0.05, indicating that there is no significant difference between reaction times for orange and blue circles.

    Is this surprising? No not really! The data didn't appear to be significantly different in the boxplot, and we don't have a good reason to think that the color of the circle alone would affect reaction times.

---

### 4: Add *Previous Circle Color* Variable
To explore potential effects of *previous circle color*, add this column to the dataset. The first trial is excluded as it lacks a "previous" circle.

```python
# Shift the 'circle_color' column to create the 'previous_circle_color' column
all_data['previous_circle_color'] = all_data['circle_color'].shift(1)

# Remove the first trial or row of data from every subject
all_data = all_data.groupby('subject_id').apply(lambda x: x.iloc[1:]).reset_index(drop=True)

# Display the updated dataset
print(all_data.head())
```

!!! Tip "Lambda Functions"
    In the code above, we used a lambda function to remove the first trial or row of data from every subject. Lambda functions are small, anonymous functions that can have any number of arguments but only one expression. They are often used in situations where a function is needed for a short period of time.

    Be on the lookout for a "Side Quest" where you can learn more about lambda functions!

I have a hypothesis; if the previous circle color was the same as the current circle color, the reaction time will be faster. Let's see if this is true!

To make our live's easier, we'll create a new column to include a new variable, `repeat_color`, which will be `True` if the previous circle color is the same as the current circle color, and `False` otherwise.

```python
# Create a new column 'same_color' to indicate if the previous circle color is the same as the current circle color
all_data['repeat_color'] = all_data['circle_color'] == all_data['previous_circle_color']
all_data.head()
```

In the next part, we'll perform an additional t-test to see if there is a significant difference in reaction times between trials where the previous circle color is the same as the current circle color and trials where it is different.

---

### 5: Another Paired Samples T-Test

Based on the code in part 3, I'd like for you to look at the code and then think about how you'd set it up yourself. After you think/test it, continue reading below.

#### Some Snags in the Plan

A problem arrises if you simply group the data by `repeat_color` and then run the t-test. The issue is that we no longer have equal sample sizes for each group, this is because, randomly, we ended up with 250 trials where the previous circle color was the same as the current circle color, and 828 trials where they were different.

Run the following code and you'll get an `ValueError: unequal length arrays` error.

```python
# Perform paired t-test
group1 = all_data[all_data['repeat_color'] == True]['reaction_time']  # Repeat color is True
group2 = all_data[all_data['repeat_color'] == False]['reaction_time']  # Repeat color is False

t_stat, p_value = ttest_rel(group1, group2)

# Display results
print(f"Paired Samples T-Test:\nT-Statistic = {t_stat}, p-value = {p_value}")

# Boxplot visualization
plt.figure(figsize=(10, 6))
sns.boxplot(x='repeat_color', y='reaction_time', data=all_data)
plt.title('Reaction Time by Repeat Color')
plt.xlabel('Repeat Color')
plt.ylabel('Reaction Time')
plt.show()
```

We can run this block of code below to demonstrate that the two arrays are indeed unequal lengths:

```python
import numpy as np

np.shape(group1), np.shape(group2)
```

#### Fixing the Issue

One way to fix the problem (an imperfect, but fine way for quick data visualization and exploration) is to randomly sample 250 trials from the `repeat_color == False` group. This way, we'll have equal sample sizes for both groups.

Let's do that below, and then perform the t-test and plot the results.

```python
# Randomly sample 250 trials from the 'repeat_color' == False group

group2_sample = all_data[all_data['repeat_color'] == False].sample(n=250, random_state=1)['reaction_time']

t_stat, p_value = ttest_rel(group1, group2_sample)

# Display results
print(f"Paired Samples T-Test:\nT-Statistic = {t_stat}, p-value = {p_value}")

# Get descriptive statistics
group1_desc = group1.describe()
group2_desc = group2_sample.describe()

print("\nDescriptive Statistics for Group 1 (Repeat Color is True):")
print(group1_desc)

print("\nDescriptive Statistics for Group 2 (Repeat Color is False):")
print(group2_desc)

# Boxplot visualization
plt.figure(figsize=(10, 6))
sns.boxplot(x='repeat_color', y='reaction_time', data=all_data)
plt.title('Reaction Time by Repeat Color')
plt.xlabel('Repeat Color')
plt.ylabel('Reaction Time')
plt.show()
```

By making the random_state equal to 1, we ensure that the random sample is the same every time we run the code. This way, we can reproduce the results and compare them across different runs.

This should also mean you see the same result that I do: it looks like there is no significant difference between reaction times when the previous circle color is the same as the current circle color compared to when they are different. It was a cool idea though, right?!

### 6: Two-Way ANOVA

There's one more thing that I'd like for us to explore: the possible effect and interaction between subjects...

We can set up a two-way ANOVA to investigate the effects of the current circle color, the previous circle color, and their interaction on reaction times.

!!! Tip "%pip install statsmodels"
    To run the two-way ANOVA, you'll need to install the `statsmodels` package. You can do this by running `%pip install statsmodels` in your notebook.

```python
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

# Fit the two-way ANOVA model
model = ols('reaction_time ~ C(subject_id) + C(circle_color) + C(subject_id):C(circle_color)', data=all_data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Display the ANOVA table
print(anova_table)

# Boxplot visualization
plt.figure(figsize=(12, 8))
sns.boxplot(x='circle_color', y='reaction_time', hue='subject_id', data=all_data)
plt.title('Reaction Time by Circle Color and Subject ID')
plt.xlabel('Circle Color')
plt.ylabel('Reaction Time')
plt.legend(title='Subject ID', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
```

If everything has gone smoothly, your resulting ANOVA table should look like this:
```txt
                                     sum_sq      df          F        PR(>F)
C(subject_id)                  3.327539e+06    21.0  11.095641  1.533542e-33
C(circle_color)                1.209871e+03     1.0   0.084720  7.710580e-01
C(subject_id):C(circle_color)  2.686349e+05    21.0   0.895760  5.971599e-01
Residual                       1.476631e+07  1034.0        NaN           NaN
```

The last column is your p-value in scientific notation; we can see that the only significant effect is the subject ID. This is not surprising, as we would expect that different subjects would have different reaction times.

What does this mean? It means that the color of the circle and the interaction between the color of the circle and the subject ID do not have a significant effect on reaction times, but different people do have different reaction times.

Now you've run a two-way ANOVA in Python! This is a powerful tool for analyzing the effects of multiple factors on a dependent variable.

---

### Conclusion
In this step, we:

- Established the reaction time dataset and computed basic statistics.
- Conducted a paired samples t-test to evaluate differences between orange and blue circles.
- Introduced a new variable (*same circle color*), and randomly sampled to ensure equal sample sizes for a second t-test.
- Performed a two-way ANOVA and visualized all of the data.

What are some things we didn't do?

- We didn't check for normality or homogeneity of variance in the t-tests or ANOVA.
- We didn't explore other statistical tests or models that could be applied to this dataset (Logistic Regression would be great, for example).
- We didn't remove outliers, this could have changed the results of the t-tests and ANOVA.

Take a moment to think about what else you'd like to explore with this dataset. What other statistical tests or models could be applied? What additional variables could be included to enhance the analysis? If you're brave enough, try to implement some of these ideas!