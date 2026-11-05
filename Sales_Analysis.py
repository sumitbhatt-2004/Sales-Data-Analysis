import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')
print(df)

# Shape of the DataFrame
print("Shape of the DataFrame:", df.shape)
# Columns in the DataFrame
print("Columns in the DataFrame:", df.columns)
# data types of each column
print("Data types of each column:\n", df.dtypes)

# Summary statistics of the DataFrame
print("Summary statistics of the DataFrame:\n", df.describe())

# checking the duplicates in the DataFrame
duplicates = df.duplicated()
print("Number of duplicate rows in the DataFrame:", duplicates.sum()) # so we are able to see how many duplicates are there in the DataFrame

# if there are any duplicates, we can drop them
if duplicates.any():
    df.drop_duplicates(inplace=True)
    print("Duplicate rows dropped from the DataFrame.")


# checking for missing values in the DataFrame
missing_values = df.isnull().sum()
print("Missing values in the DataFrame:\n", missing_values) # so we are able to see how many missing values are there in the DataFrame

# if there are any missing values, we can fill them with the mean of the column
if missing_values.any():
    df.fillna(df.mean(), inplace=True)
    print("Missing values filled with mean of the column.") 

# Now we can perform some basic analysis on the sales data we have cleaned. For example, we can calculate the total sales, average sales, and visualize the sales data.
# Calculating total revenue
total_revenue = df['Total_Sales'].sum()
print("Total revenue:", total_revenue)

# Calculating average revenue
average_revenue = df['Total_Sales'].mean()
print("Average revenue:", average_revenue)

# Now we will Find the top 5 products with the highest sales
top_products = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(5)
print("Top 5 products with the highest sales:\n", top_products)

# visualizing the top 5 products with the highest sales
top_products.plot(kind='bar', color='skyblue')
plt.title('Top 5 Products with Highest Sales')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Now we will find the best region with the highest sales
top_region = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False).head(2)
print("Best region with the highest sales:\n", top_region)

# visualizing the best region with the highest sales
top_region.plot(kind='bar', color='lightgreen')
plt.title('Best Region with Highest Sales') 
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Insights and Recommendations:
# 1. The total revenue generated from sales is [12365048]. This indicates the overall performance of the sales team and the effectiveness of the marketing strategies.
# 2. The average revenue per sale is [123650.48]. This can help in understanding the average value of each transaction and can be used to set sales targets.
# 3. The top 5 products with the highest sales are [Laptop,Tablet,Phone,Headphones,Monitor]. This information can be used to focus marketing efforts on these products and potentially increase sales further.
# 4. The best region with the highest sales is [North,South]. This information can be used to allocate resources and marketing efforts to the most profitable regions, potentially increasing overall sales performance.
 

