import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('sample-sales-data.csv')

# Display the first few rows
print("First 5 rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean the dataset
df_cleaned = df.dropna()  # Dropping rows with missing values

# Basic statistics
print("\nBasic Statistics:")
print(df_cleaned.describe())

# Group by 'PRODUCTLINE' and calculate total sales
sales_by_product = df_cleaned.groupby('PRODUCTLINE')['SALES'].sum().reset_index()

# Sort in descending order
sales_by_product = sales_by_product.sort_values(by='SALES', ascending=False)

# Plotting

# Line chart: Sales over time
df_cleaned['ORDERDATE'] = pd.to_datetime(df_cleaned['ORDERDATE'])
df_cleaned['YearMonth'] = df_cleaned['ORDERDATE'].dt.to_period('M')
monthly_sales = df_cleaned.groupby('YearMonth')['SALES'].sum()

plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line')
plt.title('Monthly Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

# Bar chart: Total sales by product line
plt.figure(figsize=(10, 6))
sns.barplot(x='PRODUCTLINE', y='SALES', data=sales_by_product)
plt.title('Total Sales by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Histogram: Distribution of sales
plt.figure(figsize=(10, 6))
sns.histplot(df_cleaned['SALES'], bins=30, kde=True)
plt.title('Distribution of Sales')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')
plt.show()

# Scatter plot: Sales vs. Quantity Ordered
plt.figure(figsize=(10, 6))
sns.scatterplot(x='QUANTITYORDERED', y='SALES', data=df_cleaned)
plt.title('Sales vs. Quantity Ordered')
plt.xlabel('Quantity Ordered')
plt.ylabel('Sales Amount')
plt.show()
