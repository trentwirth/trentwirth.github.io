# Step 23

## Data Dive I: Finding Data

Your journey into data analysis starts with finding an interesting dataset. For this step, you can either:

1. **Search for Open Datasets**: Explore open-source datasets available on platforms like [Kaggle](https://www.kaggle.com/), [Data.gov](https://www.data.gov/), or [Google Dataset Search](https://datasetsearch.research.google.com/).

2. **Download Personal Data**: Many services allow you to download your personal data (e.g., Instagram, Spotify, or Google). Make sure the downloaded data is in a workable format such as `json`, `csv`, or `txt`. If you want to work with your own data, Google how to download it from the respective service.

## Preparing for Import

Once you have your data:

- Ensure the dataset is saved locally in a known file path.
- Check the file format (e.g., `.csv`, `.json`, `.txt`) as it will guide how you load it into Python.

## Using AI to Help Format Your Data

Organizing raw data can be challenging, especially if the dataset has many columns or uses inconsistent formatting. AI tools like **ChatGPT**, **Claude**, and **Microsoft Copilot** can help you write Python code to clean and organize your data.

### Best Practices When Using AI Tools

1. **Feed Your Datafile**: Many AI tools allow you to upload your dataset directly for analysis. Uploading your file can help the AI better understand your data structure.
2. **Provide Context**: Clearly describe what you're trying to achieve, such as renaming columns, handling missing values, or filtering rows.
3. **Iterate**: If the AI-generated code doesn’t work perfectly, provide feedback and ask for adjustments.

### Example Prompts for Using AI

Here are some sample prompts to get you started:

#### Prompt 1: General Formatting

*"I have a dataset in CSV format with inconsistent column names. Here's a sample of the data: [paste or upload your dataset]. Could you help me write Python code using Pandas to clean the column names (e.g., make them lowercase and replace spaces with underscores) and handle missing values by filling them with 0?"*

#### Prompt 2: Renaming Columns

*"Here’s my dataset: [paste or upload]. I want to rename the column `Old Column Name` to `new_column_name`. Could you provide the Pandas code to do this?"*

#### Prompt 3: Filtering Rows

*"My dataset has a column called `age`. Could you write Python code using Pandas to filter out rows where the age is less than 18? Here’s the data: [paste or upload]."*

#### Prompt 4: Creating New Columns

*"I have this dataset: [paste or upload]. I’d like to create a new column that calculates the ratio of `sales` to `profit`. Could you help me write the code for that in Pandas?"*

#### Prompt 5: Data Structure Insights

*"Here’s my dataset: [paste or upload]. Could you provide a summary of the dataset, including column data types and a preview of the first few rows? Also, suggest any obvious cleaning steps that might be necessary."*

### Why Use AI?

AI tools can speed up your workflow, reduce errors, and give you creative ideas for working with your data. However, it's essential to understand the basics of Pandas so you can verify and tweak the code generated by the AI.

How do you get the basics of Pandas down? By practicing and looking things up! In previous learning steps, we've used Pandas to do a variety of tasks, such as filtering data, creating new columns, and summarizing data. Go back and look at what we did, look up function names in the Pandas documentation [(linked here)](https://pandas.pydata.org/pandas-docs/stable/index.html), and practice using Pandas on your own data.

## Importing Data into Pandas

Follow these steps to import and organize your data into a Pandas DataFrame:

### 1. Setting Up

Start by importing the necessary libraries.

```python
import pandas as pd
import json  # Only if your dataset is in JSON format

# Add more libraries if needed (e.g., os for file management)
```

### 2. Loading Data Based on File Type

#### For CSV Files:

```python
# Replace 'your_dataset.csv' with your file's name
file_path = 'your_dataset.csv'
data = pd.read_csv(file_path)

# Preview the first few rows
print(data.head())
```

#### For JSON Files:

```python
# Replace 'your_dataset.json' with your file's name
file_path = 'your_dataset.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Convert JSON data into a DataFrame
df = pd.DataFrame(data)
print(df.head())
```

#### For TXT Files (Delimited):

```python
# Replace 'your_dataset.txt' with your file's name and delimiter (e.g., '\t' for tab-delimited)
file_path = 'your_dataset.txt'
data = pd.read_csv(file_path, delimiter='\t')

# Preview the first few rows
print(data.head())
```

### 3. Cleaning and Organizing the DataFrame

Once your data is loaded, ensure it's organized and meaningful:

!!! Tip "Keep looking at your DataFrame"
    As you clean and organize your data, keep checking the DataFrame to ensure it's structured the way you want. Use `print(data.head())` to preview the first few rows and `print(data.info())` to get an overview of the columns and data types.

- **Inspect the structure**:
  ```python
  print(data.info())  # Overview of columns and data types
  ```

- **Rename columns** if needed:
  ```python
  data.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)
  ```

- **Filter unnecessary rows/columns**:
  ```python
  # Dropping a column
  data.drop(columns=['unnecessary_column'], inplace=True)
  
  # Keeping specific rows
  data = data[data['column_name'] > threshold_value]
  ```

- **Handle missing values**:
  ```python
  data.fillna(value=default_value, inplace=True)  # Fill missing values
  data.dropna(inplace=True)  # Optionally drop rows with missing values
  ```

## Conclusion

At this stage, you should have:

- Located and downloaded an interesting dataset.
- Used AI tools (optional but highly recommended!) to assist in formatting and organizing your data.
- Imported it into Python using Pandas.
- Organized the dataset to ensure meaningful rows and columns.

Once you're comfortable with the structure of your data, you're ready to dive into visualizations in Step 24!