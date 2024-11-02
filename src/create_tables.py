import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_customers(number_of_records):
    fake_table = []
    region_data = {
        "United States": {
            "California": ["Los Angeles", "San Francisco", "San Diego"],
            "Texas": ["Houston", "Dallas", "Austin"],
        },
        "Canada": {
            "Ontario": ["Toronto", "Ottawa", "Hamilton"],
            "Quebec": ["Montreal", "Quebec City", "Laval"],
        },
        "Germany": {
            "Bavaria": ["Munich", "Nuremberg"],
            "Berlin": ["Berlin"],
        },
        "Brazil": {
            "Rio de Janeiro": ["Rio de Janeiro", "Niteroi", "Duque de Caxias"],
            "Sao Paulo": ["Sao Paulo", "Barueri", "Campinas"],
            "Minas Gerais": ["Belo Horizonte", "Uberlandia", "Vicosa"],
        }
    }
    for record in range(number_of_records):
        country = random.choice(list(region_data.keys()))
        state = random.choice(list(region_data[country].keys()))
        city = random.choice(region_data[country][state])
        fake_table.append(
            {
                "Customer_ID": f"C{str(record + 1).zfill(4)}",
                "Customer_Name": fake.name(),
                "Email": fake.email(),
                "Phone": f'{fake.msisdn()[:2]}-{fake.msisdn()[:3]}-{fake.msisdn()[:4]}',
                "Address": fake.street_address(),
                "City": city,
                "State": state,
                "Country": country,
                "Customer_Segment": random.choice(["Standard", "Premium"])
            }
        )
    df = pd.DataFrame(fake_table)
    return df


def generate_products(number_of_records):
    fake_table = []
    for _ in range(number_of_records):
        fake_table.append(
            {
                "Product_ID": f"P{str(_ + 1).zfill(5)}",
                "Product_Name": f'EAN{fake.ean(length=8)}',
                "Category": random.choice(["Eletronics", "Peripherals", "Accessories"]),
                "Brand": random.choice(["XMSJ", "Xiome", "RealFit", "NewBee", "TWS"]),
                "Unit_Price": round(random.uniform(5, 100), 2),
                "Unit_Cost": round(random.uniform(2, 50), 2),
                "Shipping_Cost": round(random.uniform(5, 50), 2),
                "Stock_Quantity": random.randint(0, 200)
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


def generate_sales(df_customers, df_products, df_channels, number_of_records, start_date, end_date):
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
    df_customers = generate_customers(5)
    df_products = generate_products(5)
    df_channels = generate_channels()
    df_sales = generate_sales(df_customers, df_products, 15, start_date='2024-01-01', end_date='2024-12-31')
    

    print(df_customers.head())
    print("")
    print(df_customers.head())
    print("")
    print(df_channels.head())
    print(df_sales.head())
    print("")