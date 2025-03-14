import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_customers(number_of_records=100):
    fake_table = []
    
    for record in range(number_of_records):
        fake_table.append(
            {
                "Customer_ID": f"C{str(record + 1).zfill(4)}",
                "Customer_Name": fake.name(),
                "Email": fake.email(),
                "Phone": f'{fake.msisdn()[:2]}-{fake.msisdn()[:3]}-{fake.msisdn()[:4]}',
                "Address": fake.street_address(),
                "Customer_Segment": random.choice(["Standard", "Premium"])
            }
        )
    df = pd.DataFrame(fake_table)
    return df


def generate_products(number_of_records=30):
    fake_table = []
    for _ in range(number_of_records):

        product_unit_price = round(random.uniform(300, 10000), 2)

        fake_table.append(
            {
                "Product_ID": f"P{str(_ + 1).zfill(5)}",
                "Product_Name": f'EAN{fake.ean(length=8)}',
                "Category": random.choice(["Computers", "Laptops", "Tablets", "Phones", "SmartTVs"]),
                "Brand": random.choice(["XanSJ", "Xioume", "ReialFit", "NewBirde", "TxWS"]),
                "Unit_Price": product_unit_price,
                "Unit_Cost": round(random.uniform(product_unit_price * 0.15, product_unit_price * 0.5 ), 2),
            }
        )
    df = pd.DataFrame(fake_table)
    return df


def generate_channels():
    fake_table = []
    count_id = 0
    channels_data = {
        "Online": "e-commerce",
        "Retail": "physical stores",
        "Wholesale": "distributors"
    }
    for key, value in channels_data.items():
        fake_table.append(
            {
                "Channel_ID" : f"CH{str(count_id + 1).zfill(5)}",
                "Channel_Name" : key,
                "Description" : f'Sales through {value}'
            }
        )
        count_id += 1
    df = pd.DataFrame(fake_table)
    return df


def generate_sales(df_customers, df_products, df_channels, number_of_records=1000, start_date='2022-01-01', end_date='2024-12-31'):
    fake_table = []
    for record in range(number_of_records):
        fake_table.append(
            {
                "Sale_ID": record + 1,
                "Order_Date": random.choice(pd.date_range(start=start_date, end=end_date, freq='ME')),
                "Customer_ID": random.choice(df_customers['Customer_ID']),
                "Product_ID": random.choice(df_products['Product_ID']),
                "Channel_ID": random.choice(df_channels['Channel_ID']),
                "Quantity_Sold": random.randint(1, 10),
                "Discount_Percentage": round(random.uniform(0, 30), 2)
            }
        )
    df = pd.DataFrame(fake_table)
    return df


if __name__ == '__main__':
    df_customers = generate_customers()
    df_products = generate_products()
    df_channels = generate_channels()
    df_sales = generate_sales(df_customers, df_products, df_channels)

    print(df_customers.info())
    print(df_products.info())
    print(df_channels.info())
    print(df_sales.info())
