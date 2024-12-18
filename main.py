import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to SQLite
conn = sqlite3.connect("customer_data.db")

# Query for average income by marital status
query_1 = """
SELECT MaritalStatus, AVG(Income) AS AvgIncome
FROM customer_profiles
GROUP BY MaritalStatus
ORDER BY AvgIncome DESC;
"""
df_1 = pd.read_sql(query_1, conn)

# Plot the results
plt.figure(figsize=(8, 6))
sns.barplot(x='MaritalStatus', y='AvgIncome', data=df_1, palette='coolwarm')
plt.title('Average Income by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Average Income')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Query for average miles traveled by fitness level
query_2 = """
SELECT Fitness, AVG(Miles) AS AvgMiles
FROM customer_profiles
GROUP BY Fitness
ORDER BY AvgMiles DESC;
"""
df_2 = pd.read_sql(query_2, conn)

# Plot the results
plt.figure(figsize=(8, 6))
sns.barplot(x='Fitness', y='AvgMiles', data=df_2, palette='viridis')
plt.title('Average Miles Traveled by Fitness Level')
plt.xlabel('Fitness Level')
plt.ylabel('Average Miles Traveled')
plt.tight_layout()
plt.show()

# Query for product preferences by gender
query_3 = """
SELECT 
    Product, 
    Gender, 
    COUNT(*) AS ProductCount,
    (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customer_profiles WHERE Product = c.Product)) AS PercentageByGender
FROM customer_profiles c
GROUP BY Product, Gender
ORDER BY Product, PercentageByGender DESC;
"""
df_3 = pd.read_sql(query_3, conn)

# List of unique products
products = df_3['Product'].unique()

# Plotting the pie charts for each product
fig, axes = plt.subplots(1, len(products), figsize=(18, 6))

for i, product in enumerate(products):
    # Filter data for the current product
    product_data = df_3[df_3['Product'] == product]
    
    # Create the pie chart
    axes[i].pie(product_data['PercentageByGender'], labels=product_data['Gender'], autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#ff6666'])
    axes[i].set_title(f'Gender Distribution for {product}')
    axes[i].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the plot
plt.tight_layout()
plt.show()

# Query for age distribution across different usage levels
query_4 = """
SELECT 
    CASE 
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        WHEN Age BETWEEN 46 AND 60 THEN '46-60'
        ELSE '60+' 
    END AS AgeRange,
    AVG(Usage) AS AvgUsage
FROM customer_profiles
GROUP BY AgeRange
ORDER BY AgeRange;
"""
df_4 = pd.read_sql(query_4, conn)

# Plot the results
plt.figure(figsize=(8, 6))
sns.barplot(x='AgeRange', y='AvgUsage', data=df_4, palette='Blues')
plt.title('Average Usage by Age Range')
plt.xlabel('Age Range')
plt.ylabel('Average Usage')
plt.tight_layout()
plt.show()

# Close the connection
conn.close()
