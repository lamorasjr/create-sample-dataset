from create_tables import generate_customers, generate_products, generate_channels, generate_sales

num_customers = 100
num_products = 50
num_sales = 700
start_date = '2021-01-01'
end_date = '2024-12-31'
output_path = 'data/'

df_customers = generate_customers(num_customers)
df_products = generate_products(num_products)
df_channels = generate_channels()
df_sales = generate_sales(df_customers, df_products, num_sales, start_date, end_date)

df_customers.to_csv(f'{output_path}dim_customers.csv', sep=',', encoding='utf-8', index=False)
df_products.to_csv(f'{output_path}dim_products.csv', sep=',', encoding='utf-8', index=False)
df_channels.to_csv(f'{output_path}dim_channels.csv', sep=',', encoding='utf-8', index=False)
df_sales.to_csv(f'{output_path}fact_sales.csv', sep=',', encoding='utf-8', index=False)


print("The dataset files has been created successfully.")