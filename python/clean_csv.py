import pandas as pd
import uuid

# import csv
df = pd.read_csv('./TransactionData.csv')

# view data frame datatypes
df.info()

# Check for missing data
print(df.isnull().sum())

# Check for duplicates
print(df[df.duplicated(keep=False)])

# Create a mapping from customer_id to uuid
uuid_map = {cid: uuid.uuid4() for cid in df['customer_id'].unique()}

# Assign UUID based on customer_id
df['cart_id'] = df['customer_id'].map(uuid_map)

# View all columns
pd.set_option('display.max_columns', None)

print(df)

# wrap address data in quotations because of comma
df['address'] = df['address'].apply(lambda x: f'"{x}"')

print(df['phone'])

# Remove extensions on phone numbers
df['phone'] = df['phone'].str.replace(r'[xX].*$', '', regex=True)

print(df['phone'])

# Remove non digits on phone numbers
df['phone'] = df['phone'].str.replace(r'\D', '', regex=True)

print(df['phone'])

# Keep the last ten digits of the phone number
df['phone'] = df['phone'].str[-10:]

print(df['phone'])

# Change number format
df['phone'] = df['phone'].astype(str).str.replace(r'^(\d{3})(\d{3})(\d{4})$', r'(\1) \2-\3', regex=True)

print(df['phone'])


print(df[['cart_id', 'customer_id']].head(30))

# Export to csv
df.to_csv('./Cleaned_TransactionData.csv', index=False)

# Select columns for shoppingcart csv
shopping_cart = df.get(['cart_id', 'customer_id'])

print(shopping_cart.head(30))

# Select columns for customers csv
customers = df.get(['customer_id', 'name', 'email', 'phone', 'address'])

print(customers.head(30))

# Select columns for products csv
products = df.get(['product_id', 'cart_id', 'vendor', 'product_category', 'product_name', 'quantity', 'price'])

print(products.head(30))

# Select columns for transactions csv
transactions = df.get(['transaction_id', 'customer_id', 'cart_id', 'transaction_date', 'shipping_method',
                       'total_amount'])

# drop duplicates
shopping_cart = shopping_cart.drop_duplicates()

print(transactions.head(30))

# Export shopping cart dataframe to csv
shopping_cart.to_csv('./shopping_cart.csv', index=False)

print("CSV file 'shopping_cart.csv' has been created successfully!")

# drop duplicates
customers = customers.drop_duplicates()

# Export customers dataframe to csv
customers.to_csv('./customers.csv', index=False)

print("CSV file 'customers.csv' has been created successfully!")

# drop duplicates
products = products.drop_duplicates()

# Export products dataframe to csv
products.to_csv('./products.csv', index=False)

print("CSV file 'products.csv' has been created successfully!")

# drop duplicates
transactions = transactions.drop_duplicates()

# Export transactions dataframe to csv
transactions.to_csv('./transactions.csv', index=False)

print("CSV file 'transactions.csv' has been created successfully!")
