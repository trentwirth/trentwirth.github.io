# Step 21

In this step, we will process and visualize the reaction time data we collected in `Step 20` using Pandas! We will get this data from a zip file containing many `.csv` files, where each file contains data from a participant in a reaction time experiment. 

You will learn to:

1. Load a zip file of data into Python.
2. Extract and load all `.csv` files into a single pandas DataFrame.
3. Clean the data to isolate relevant variables. Visualize "raw" reaction time data.
4. Aggregate data by participant and analyze mean reaction times.
5. Visualize aggregated data.

## 0: Download the Zip File

> What's a Zip File? A zip file is a compressed folder that contains one or more files. It's a common way to package and share multiple files together.

[Click here to download the reaction time `.zip` file](files/reaction_time_data.zip)



## 1: Load and Unzip the Data

To begin, ensure you have downloaded the zip file. You can unzip it manually or programmatically within Python. Here’s how to do it in Python:

```python
import zipfile
import os

# Define file paths
zip_path = 'reaction_time_data.zip' # If you've put your file in the same directory as the notebook you're working in, your path is just the file name. If not, you'll need to include the path to the file.
extract_path = '.' # This will extract the files to the current directory

# Unzip the file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
```

After running this code, you should see the extracted `.csv` files in the specified directory - this will be a lot of files!

## 2: Load CSV Files into a Pandas DataFrame

With the files extracted, we can load each `.csv` file into a DataFrame. Each row in the final DataFrame will represent a trial, with columns for relevant data.

```python
import pandas as pd
import glob
import os

# Path to the directory containing extracted .csv files
csv_files = glob.glob(os.path.join(extract_path, '*.csv'))

# Initialize an empty list to store DataFrames
dfs = []

# Loop through and read each csv file
for idx, file in enumerate(csv_files):
    data = pd.read_csv(file)

    # Extract relevant rows and columns
    # Filter rows where 'trial_type' is 'response' (indicating a reaction time trial)
    data = data[data['trial_type'] == 'image-keyboard-response']

    # Select and rename relevant columns
    df = data[['rt', 'stimulus', 'response', 'correct']].copy()
    df.rename(columns={
        'rt': 'reaction_time',
        'stimulus': 'circle_color',
        'response': 'key_pressed',
        'correct': 'accuracy'
    }, inplace=True)

    # Clean up 'circle_color' to extract only color names
    df['circle_color'] = df['circle_color'].str.extract(r'images/(\w+).png')[0]

    # Add subject_id column
    df['subject_id'] = idx + 1

    # Reorder columns to make 'subject_id' the first column
    df = df[['subject_id', 'reaction_time', 'circle_color', 'key_pressed', 'accuracy']]

    # Append the processed DataFrame
    dfs.append(df)

# Concatenate all DataFrames
all_data = pd.concat(dfs, ignore_index=True)
```

## 3: Clean and Visualize Reaction Time Data

Now that we have all trials loaded into a DataFrame, we can start visualizing the reaction time data.

### 3a. Histogram of Reaction Time Data

Use a histogram to explore the distribution of reaction times. Adjust the bin width with an interactive widget.

```python
import matplotlib.pyplot as plt
import ipywidgets as widgets

def plot_histogram(bin_width):
    plt.hist(all_data['reaction_time'].dropna(), bins=bin_width)
    plt.title('Histogram of Reaction Times')
    plt.xlabel('Reaction Time (ms)')
    plt.ylabel('Frequency')
    plt.show()

widgets.interactive(plot_histogram, bin_width=widgets.IntSlider(min=5, max=100, step=5, value=20))
```

### 3b. Box Plot of Mean Reaction Times by Accuracy

A box and whisker plot can show differences in reaction times between "true" (correct) and "false" (incorrect) responses.

!!! Tip "Seaborn"
    Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for creating attractive and informative statistical graphics. You can install Seaborn using `pip install seaborn`.

    In your notebook, you might want to run `%pip install seaborn` to install Seaborn, instead of the normal pip install.

```python
import seaborn as sns

# Plot box and whisker plot for reaction times by accuracy
sns.boxplot(x='accuracy', y='reaction_time', data=all_data)
plt.title('Reaction Times by Accuracy')
plt.xlabel('Accuracy (True or False)')
plt.ylabel('Reaction Time (ms)')
plt.show()
```

It's great to have a visualization, but it will probably be good to know the means and standard deviation values of these plots as well, let's use Pandas to calculate those!

```python
import pandas as pd

# Assuming 'all_data' is your DataFrame
true_responses = all_data[all_data['accuracy'] == True]
false_responses = all_data[all_data['accuracy'] == False]

true_mean = true_responses['reaction_time'].mean()
true_sd = true_responses['reaction_time'].std()

false_mean = false_responses['reaction_time'].mean()
false_sd = false_responses['reaction_time'].std()

# Print the mean and standard deviation values, and the counts of each group
print(f"True responses - Mean: {true_mean}, SD: {true_sd}, Count: {len(true_responses)}")
print(f"False responses - Mean: {false_mean}, SD: {false_sd}, Count: {len(false_responses)}")
```

#### Think about the data

Look at the means and standard deviations. What do you think a paired t-test would show? What problem arrises when we look at the "Count" of each data type?

## 4: Aggregate Mean Reaction Times by Participant/Subject

Next, let’s condense the data to calculate each subject's mean reaction time and the number of "true" (correct) trials out of 50.

```python
# Calculate mean reaction times and true trial counts
subject_summary = all_data.groupby('subject_id').agg(
    mean_reaction_time=('reaction_time', 'mean'),
    true_count=('accuracy', lambda x: (x == True).sum())
).reset_index()
```

## 5: Visualize Mean Reaction Time Data

### 5a. Histogram of Mean Reaction Times

Plot a histogram of mean reaction times for each participant.

```python
plt.hist(subject_summary['mean_reaction_time'], bins=20)
plt.title('Histogram of Mean Reaction Times by subject')
plt.xlabel('Mean Reaction Time (ms)')
plt.ylabel('Frequency')
plt.show()
```

### 5b. Scatterplot of Reaction Time and % "True" Responses

Plot a scatterplot to explore the relationship between subjects’ mean reaction times and their accuracy rate.

```python
# Calculate accuracy percentage
subject_summary['true_percentage'] = (subject_summary['true_count'] / 50) * 100

# Scatterplot of mean reaction time vs. true percentage
plt.scatter(subject_summary['mean_reaction_time'], subject_summary['true_percentage'])
plt.title('Mean Reaction Time vs. % True Responses')
plt.xlabel('Mean Reaction Time (ms)')
plt.ylabel('% True Responses')
plt.show()
```

## 6. Have fun with it!

Take time to play with [Seaborn](https://seaborn.pydata.org/) and [Matplotlib](https://matplotlib.org/) to create more visualizations and explore the data further. You can also experiment with different data transformations and analysis techniques to gain deeper insights!

Dig into the Pandas dataframe, look at the data, and see if you can find any interesting patterns or relationships.

```python
# Display the first few rows of the DataFrame
all_data.head()
```

You can grab different columns and plot them against each other to see if there are any relationships. For example, you could plot the reaction time against the color of the circle that was shown to the participant.

## 7. Review

In this step, you’ve learned how to handle, clean, and visualize reaction time data using pandas, matplotlib, and seaborn. In a future step, we'll look at how to analyze this data statistically to draw meaningful conclusions!