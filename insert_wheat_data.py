"""
Direct Data Insertion Script for Inventory Dashboard
This script directly inserts wheat data into your app's storage file
"""

import json
import os
from datetime import datetime

# Storage Configuration (same as in your app)
STORAGE_DIR = os.path.join(os.path.expanduser("~"), ".local", "share", "InventoryDashboard")
STORAGE_FILE = os.path.join(STORAGE_DIR, "data.json")

# Ensure storage directory exists
os.makedirs(STORAGE_DIR, exist_ok=True)

# Your wheat data
wheat_data = [
    {"date": "24/10/2025", "product_name": "Wheat", "quantity_received": 150, "quantity_sold": 23, "cost_price": 1488.00, "selling_price": 1650.00},
    {"date": "26/11/2025", "product_name": "Wheat", "quantity_received": 0, "quantity_sold": 19, "cost_price": 1488.00, "selling_price": 1650.00},
    {"date": "27/11/2025", "product_name": "Wheat", "quantity_received": 0, "quantity_sold": 10, "cost_price": 1488.00, "selling_price": 1650.00},
    {"date": "28/11/2025", "product_name": "Wheat", "quantity_received": 0, "quantity_sold": 14.5, "cost_price": 1488.00, "selling_price": 1650.00},
    {"date": "29/11/2025", "product_name": "Wheat", "quantity_received": 0, "quantity_sold": 18.5, "cost_price": 1488.00, "selling_price": 1650.00},
    {"date": "30/11/2025", "product_name": "Wheat", "quantity_received": 0, "quantity_sold": 3, "cost_price": 1488.00, "selling_price": 1650.00},
    {"date": "01/12/2025", "product_name": "Wheat", "quantity_received": 0, "quantity_sold": 12, "cost_price": 1488.00, "selling_price": 1650.00},
    {"date": "02/12/2025", "product_name": "Wheat", "quantity_received": 0, "quantity_sold": 20, "cost_price": 1488.00, "selling_price": 1600.00},
    {"date": "03/12/2025", "product_name": "Wheat", "quantity_received": 0, "quantity_sold": 8, "cost_price": 1488.00, "selling_price": 1650.00},
    {"date": "04/12/2025", "product_name": "Wheat", "quantity_received": 0, "quantity_sold": 22, "cost_price": 1488.00, "selling_price": 1600.00},
    {"date": "05/12/2025", "product_name": "Wheat", "quantity_received": 12, "quantity_sold": 12, "cost_price": 1580.00, "selling_price": 1650.00},
    {"date": "06/12/2025", "product_name": "Wheat", "quantity_received": 8, "quantity_sold": 8, "cost_price": 1590.00, "selling_price": 1650.00},
    {"date": "07/12/2025", "product_name": "Wheat", "quantity_received": 15, "quantity_sold": 15, "cost_price": 1580.00, "selling_price": 1650.00},
    {"date": "08/12/2025", "product_name": "Wheat", "quantity_received": 10, "quantity_sold": 10, "cost_price": 1520.00, "selling_price": 1650.00},
    {"date": "11/12/2025", "product_name": "Wheat", "quantity_received": 10, "quantity_sold": 4, "cost_price": 1520.00, "selling_price": 1650.00},
    {"date": "12/12/2025", "product_name": "Wheat", "quantity_received": 0, "quantity_sold": 5, "cost_price": 1520.00, "selling_price": 1650.00},
    {"date": "13/12/2025", "product_name": "Wheat", "quantity_received": 0, "quantity_sold": 1, "cost_price": 1520.00, "selling_price": 1650.00}
]

def calculate_stock_left(transactions, product, qty_received, qty_sold):
    """Calculate stock left based on previous transactions"""
    product_transactions = [t for t in transactions if t['Product Name'] == product]
    if product_transactions:
        previous_stock = product_transactions[-1]['Stock Left']
    else:
        previous_stock = 0
    
    new_stock = previous_stock + qty_received - qty_sold
    return new_stock

def process_wheat_data():
    """Process wheat data and create proper transactions"""
    
    # Load existing data if any
    existing_data = {"products": ["Wheat", "Urea", "DAP", "Sarson", "Cow Feed", "Gandyal", "Him Cal", "Liv 52"], "transactions": []}
    
    if os.path.exists(STORAGE_FILE):
        try:
            with open(STORAGE_FILE, 'r') as f:
                existing_data = json.load(f)
        except:
            pass
    
    transactions = existing_data.get('transactions', [])
    products = existing_data.get('products', ["Wheat", "Urea", "DAP", "Sarson", "Cow Feed", "Gandyal", "Him Cal", "Liv 52"])
    
    # Add Wheat to products if not present
    if "Wheat" not in products:
        products.append("Wheat")
    
    print(f"Processing {len(wheat_data)} wheat transactions...")
    
    for record in wheat_data:
        # Calculate fields
        stock_left = calculate_stock_left(transactions, "Wheat", record['quantity_received'], record['quantity_sold'])
        total_purchase = record['quantity_received'] * record['cost_price']
        total_sales = record['quantity_sold'] * record['selling_price']
        profit = (record['selling_price'] - record['cost_price']) * record['quantity_sold']
        
        # Create transaction record
        transaction = {
            'Date': record['date'],
            'Product Name': record['product_name'],
            'Quantity Received': record['quantity_received'],
            'Quantity Sold': record['quantity_sold'],
            'Stock Left': stock_left,
            'Cost Price': record['cost_price'],
            'Selling Price': record['selling_price'],
            'Total Purchase': total_purchase,
            'Total Sales': total_sales,
            'Profit': profit,
            'Remarks': ''
        }
        
        transactions.append(transaction)
        print(f"✅ Added: {record['date']} - Stock: {stock_left}")
    
    # Save to storage file
    final_data = {
        'products': products,
        'transactions': transactions
    }
    
    with open(STORAGE_FILE, 'w') as f:
        json.dump(final_data, f, indent=4)
    
    print(f"\n🎉 SUCCESS! Added {len(wheat_data)} wheat transactions to your app!")
    print(f"📁 Data saved to: {STORAGE_FILE}")
    print(f"📊 Total transactions now: {len(transactions)}")
    print("\n🚀 Now run your Streamlit app to see the data!")

if __name__ == "__main__":
    try:
        process_wheat_data()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure you have the correct permissions and the directory exists.")