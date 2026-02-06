import json
import csv

# Load JSON data from file
with open('./TransactionData.json', 'r') as f:
    json_data = json.load(f)

# Define CSV column headers
headers = [
    'transaction_id', 'transaction_date', 'shipping_method', 'total_amount',
    'product_id', 'vendor', 'product_category', 'product_name', 'quantity', 'price',
    'customer_id', 'name', 'email', 'phone', 'address'
]


# Convert JSON to CSV
def json_to_csv(json_data, output_file='./TransactionData.csv'):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write headers
        writer.writerow(headers)

        # Process each transaction
        for transaction in json_data:
            # Get transaction-level data
            transaction_id = transaction.get('transaction_id', '')
            transaction_date = transaction.get('transaction_date', '')
            shipping_method = transaction.get('shipping_method', '')
            total_amount = transaction.get('total_amount', '')

            # Get customer data
            customer = transaction.get('customer', {})
            customer_id = customer.get('customer_id', '')
            name = customer.get('name', '')
            email = customer.get('email', '')
            phone = customer.get('phone', '')
            address = customer.get('address', '')

            # Process each product in shopping cart
            shopping_cart = transaction.get('shopping_cart', [])
            for product in shopping_cart:
                product_id = product.get('product_id', '')
                vendor = product.get('vendor: ', '')
                product_category = product.get('product_category', '')
                product_name = product.get('product_name', '')
                quantity = product.get('quantity', '')
                price = product.get('price', '')

                # Write row with all data
                writer.writerow([
                    transaction_id, transaction_date, shipping_method, total_amount,
                    product_id, vendor, product_category, product_name, quantity, price,
                    customer_id, name, email, phone, address
                ])


# Convert and save to CSV
json_to_csv(json_data)
print("CSV file 'TransactionData.csv' has been created successfully!")
