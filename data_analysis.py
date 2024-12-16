# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Function to load the dataset
def load_dataset(filename):
    try:
        # Check if file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Dataset file '{filename}' not found.")
        
        # Load the dataset
        dataset = pd.read_csv('sales_data.csv')
        print("Dataset loaded successfully!")
        return dataset
    except Exception as e:
        print(f"Error: {e}")
        exit()

# Function to explore the dataset
def explore_dataset(dataset):
    print("\nFirst 5 Rows of the Dataset:")
    print(dataset.head())

    print("\nDataset Information:")
    print(dataset.info())

    print("\nChecking for Missing Values:")
    print(dataset.isnull().sum())

    # Fill or drop missing values (if any)
    if dataset.isnull().sum().any():
        print("Filling missing values...")
        dataset.fillna(0, inplace=True)

# Function to analyze the dataset
def analyze_dataset(dataset):
    print("\nBasic Statistics:")
    print(dataset.describe())

    print("\nAverage Units Sold by Region:")
    avg_units_by_region = dataset.groupby("Region")["Units Sold"].mean()
    print(avg_units_by_region)

    print("\nAverage Revenue by Product:")
    avg_revenue_by_product = dataset.groupby("Product")["Revenue"].mean()
    print(avg_revenue_by_product)

# Function to visualize the dataset
def visualize_dataset(dataset):
    print("\nCreating Visualizations...")

    # Line chart: Trend of Revenue over Time
    plt.figure(figsize=(10, 5))
    plt.plot(pd.to_datetime(dataset['Date']), dataset['Revenue'], marker='o', color='b')
    plt.title("Revenue Over Time")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('line_chart_revenue.png')  # Save the plot as an image
    plt.show()

    # Bar chart: Average Units Sold by Product
    plt.figure(figsize=(8, 5))
    sns.barplot(x="Product", y="Units Sold", data=dataset, ci=None, palette="viridis")
    plt.title("Average Units Sold by Product")
    plt.xlabel("Product")
    plt.ylabel("Units Sold")
    plt.tight_layout()
    plt.savefig('bar_chart_units_sold.png')  # Save the plot as an image
    plt.show()

    # Histogram: Distribution of Revenue
    plt.figure(figsize=(8, 5))
    plt.hist(dataset["Revenue"], bins=10, color='orange', edgecolor='black')
    plt.title("Revenue Distribution")
    plt.xlabel("Revenue")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig('histogram_revenue.png')  # Save the plot as an image
    plt.show()

    # Scatter plot: Relationship between Units Sold and Revenue
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x="Units Sold", y="Revenue", data=dataset, hue="Region", palette="deep")
    plt.title("Units Sold vs Revenue")
    plt.xlabel("Units Sold")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig('scatter_units_vs_revenue.png')  # Save the plot as an image
    plt.show()

# Main function
if __name__ == "__main__":
    # Specify the dataset filename
    dataset_file = "sales_data.csv"
    
    # Load the dataset
    dataset = load_dataset(dataset_file)

    # Explore the dataset
    explore_dataset(dataset)

    # Analyze the dataset
    analyze_dataset(dataset)

    # Visualize the dataset
    visualize_dataset(dataset)

    print("\nAnalysis complete! Visualizations saved as images.")
