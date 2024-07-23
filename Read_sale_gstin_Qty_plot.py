import pandas as pd
import matplotlib.pyplot as plt

#Read the Excel file
df = pd.read_excel(r'C:\File_path\half_july.xlsx', sheet_name='Sales Report')

#Inspect the data
print(df.head(400))           #value can be as per seller requirement or use comparison with gstin

#Extract relevant columns (assuming columns are named 'Seller GSTIN' and 'Item Quantity')
data = df[['Seller GSTIN', 'Item Quantity']]

# Step 4: Group by 'Seller GSTIN' and sum the 'Item Quantity'
grouped_data = data.groupby('Seller GSTIN')['Item Quantity'].sum().reset_index()

# Step 5: Plot the data
plt.figure(figsize=(12, 8))
plt.bar(grouped_data['Seller GSTIN'], grouped_data['Item Quantity'], color='skyblue')
plt.xlabel('Seller GSTIN')
plt.ylabel('Total Item Quantity')
plt.title('Total Item Quantity Sold by Each Seller GSTIN')
plt.xticks(rotation=90)  # Rotate the x labels for better readability
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.show()
