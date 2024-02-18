import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('sales_data.csv')

# Display the first few rows of the dataset
print(data.head())

# Basic statistics
total_sales = data['Sales'].sum()
average_sales = data['Sales'].mean()
max_sales = data['Sales'].max()
min_sales = data['Sales'].min()

print(f'Total Sales: ${total_sales}')
print(f'Average Sales: ${average_sales}')
print(f'Maximum Sales: ${max_sales}')
print(f'Minimum Sales: ${min_sales}')

# Visualization
monthly_sales = data.groupby('Month')['Sales'].sum()
monthly_sales.plot(kind='bar', xlabel='Month', ylabel='Total Sales ($)',
                    title='Monthly Sales', color='skyblue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
