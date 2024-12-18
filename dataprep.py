import sqlite3
import pandas as pd

# Load the CSV data
df = pd.read_csv("aerofit_treadmill_data.csv")

# Connect to SQLite (or any other database)
conn = sqlite3.connect("customer_data.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customer_profiles (
    Product TEXT,
    Age INTEGER,
    Gender TEXT,
    Education INTEGER,
    MaritalStatus TEXT,
    Usage INTEGER,
    Fitness INTEGER,
    Income INTEGER,
    Miles INTEGER
)
""")

# Insert data into the table
for row in df.itertuples(index=False):
    cursor.execute("""
    INSERT INTO customer_profiles (Product, Age, Gender, Education, MaritalStatus, Usage, Fitness, Income, Miles)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, row)

# Commit and close the connection
conn.commit()
conn.close()
