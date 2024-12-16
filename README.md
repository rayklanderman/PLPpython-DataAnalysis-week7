# Data Analysis and Visualization Assignment

## Objective

This assignment aims to:
- Load and analyze a dataset using the pandas library in Python
- Create simple plots and charts with the matplotlib library for visualizing the data

## Submission Requirements

Submit a Jupyter notebook (.ipynb file) or Python script (.py file) containing:
- Data loading and exploration steps
- Basic data analysis results
- Visualizations
- Any findings or observations

## Tasks

### Task 1: Load and Explore the Dataset

- Choose a CSV dataset (e.g., Iris dataset, sales dataset, or any dataset of your choice)
- Load the dataset using pandas
- Display the first few rows using `.head()`
- Explore the dataset structure:
  - Check data types
  - Identify missing values
- Clean the dataset:
  - Fill or drop missing values

### Task 2: Basic Data Analysis

- Compute basic statistics of numerical columns using `.describe()`
- Perform groupings on a categorical column
- Compute the mean of a numerical column for each group
- Identify patterns or interesting findings

### Task 3: Data Visualization

Create at least four different types of visualizations:
1. Line chart: Show trends over time (e.g., time-series of sales data)
2. Bar chart: Compare numerical values across categories (e.g., average petal length per species)
3. Histogram: Understand the distribution of a numerical column
4. Scatter plot: Visualize the relationship between two numerical columns

Customize plots with:
- Titles
- Axis labels
- Legends (where necessary)

## Additional Instructions

### Dataset Suggestions

- Use publicly available datasets from Kaggle or UCI Machine Learning Repository
- The Iris dataset can be accessed via `sklearn.datasets.load_iris()`

### Plot Customization

- Use matplotlib for basic customization
- Consider using seaborn for enhanced visual appeal

### Error Handling

- Implement exception handling for:
  - File reading errors
  - Missing data
  - Incorrect data types

### Submission Guidelines

- Ensure your submission is complete with all necessary code and explanations
- Properly label each plot
- Provide insights into the dataset through your visualizations
