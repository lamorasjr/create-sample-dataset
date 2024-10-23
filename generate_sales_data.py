import pandas as pd
from faker import Faker
import random
import numpy as np

fake = Faker()

# Number of records to generate
num_customers = 100
num_products = 50
num_territories = 10
num_sales = 500
num_promotions = 5
num_channels = 3
num_dates = 12

# Generate Dim_Customers
customers = []
for _ in range(num_customers):
    customers.append({
        "Customer_ID": f"C{str(_ + 1).zfill(3)}",
        "Customer_Name": fake.name(),
        "Email": fake.email(),
        "Phone": fake.phone_number(),
        "Address": fake.street_address(),
        "City": fake.city(),
        "State_Province": fake.state(),
        "Country": fake.country(),
        "Customer_Segment": random.choice(["Retail", "Wholesale"])
    })

df_customers = pd.DataFrame(customers)

# Generate Dim_Products
products = []
for _ in range(num_products):
    products.append({
        "Product_ID": f"P{str(_ + 1).zfill(3)}",
        "Product_Name": fake.word().capitalize() + " " + fake.word().capitalize(),
        "Category": random.choice(["Widgets", "Gadgets", "Doodads"]),
        "Brand": fake.company(),
        "Price": round(random.uniform(5, 100), 2),
        "Cost": round(random.uniform(2, 50), 2),
        "Stock_Quantity": random.randint(0, 200)
    })

df_products = pd.DataFrame(products)

# Generate Dim_Territory
territories = []
for _ in range(num_territories):
    territories.append({
        "Territory_ID": f"T{str(_ + 1).zfill(3)}",
        "Region": random.choice(["North America", "Europe", "Asia"]),
        "Country": fake.country(),
        "City": fake.city(),
        "State_Province": fake.state(),
    })

df_territories = pd.DataFrame(territories)


# Generate Dim_Sales_Channel
channels = []
for _ in range(num_channels):
    channels.append({
        "Channel_ID": f"CH{str(_ + 1).zfill(3)}",
        "Channel_Name": random.choice(["Online", "Retail", "Wholesale"]),
        "Description": "Sales through " + random.choice(["e-commerce", "physical stores", "distributors"])
    })

df_channels = pd.DataFrame(channels)

# Generate Dim_Promotions
promotions = []
for _ in range(num_promotions):
    start_date = fake.date_between(start_date='-1y', end_date='today')
    end_date = fake.date_between(start_date=start_date, end_date='+30d')
    promotions.append({
        "Promotion_ID": f"PR{str(_ + 1).zfill(3)}",
        "Promotion_Name": fake.catch_phrase(),
        "Start_Date": start_date,
        "End_Date": end_date,
        "Discount_Percentage": random.randint(5, 30)
    })

df_promotions = pd.DataFrame(promotions)

# Generate Fact_Sales
sales = []
for _ in range(num_sales):
    sales.append({
        "Sale_ID": _ + 1,
        "Order_Date": random.choice(pd.date_range(start='2023-01-01', periods=num_dates, freq='ME')),
        "Customer_ID": random.choice(df_customers['Customer_ID']),
        "Product_ID": random.choice(df_products['Product_ID']),
        "Territory_ID": random.choice(df_territories['Territory_ID']),
        "Quantity_Sold": random.randint(1, 10),
        "Total_Sales_Amount": round(random.uniform(20, 1000), 2),
        "Discount_Amount": round(random.uniform(0, 100), 2),
        "Shipping_Cost": round(random.uniform(5, 50), 2),
    })

df_sales = pd.DataFrame(sales)

# Export DataFrames to CSV
df_customers.to_csv('data/dim_customers.csv', index=False)
df_products.to_csv('data/dim_products.csv', index=False)
df_territories.to_csv('data/dim_territory.csv', index=False)
df_channels.to_csv('data/dim_sales_channel.csv', index=False)
df_promotions.to_csv('data/dim_promotions.csv', index=False)
df_sales.to_csv('data/fact_sales.csv', index=False)

print("CSV files created successfully.")
