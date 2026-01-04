"""
Complete Data Insertion Script for Inventory Dashboard
This script inserts both Wheat and DAP data into your app's storage file
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

# Your DAP data
dap_data = [
    {"date": "26/11/2025", "product_name": "DAP", "quantity_received": 90, "quantity_sold": 18, "cost_price": 1334.00, "selling_price": 1500.00},
    {"date": "27/11/2025", "product_name": "DAP", "quantity_received": 0, "quantity_sold": 7, "cost_price": 1334.00, "selling_price": 1500.00},
    {"date": "28/11/2025", "product_name": "DAP", "quantity_received": 0, "quantity_sold": 10, "cost_price": 1334.00, "selling_price": 1500.00},
    {"date": "30/11/2025", "product_name": "DAP", "quantity_received": 0, "quantity_sold": 6, "cost_price": 1334.00, "selling_price": 1500.00},
    {"date": "01/12/2025", "product_name": "DAP", "quantity_received": 0, "quantity_sold": 8, "cost_price": 1334.00, "selling_price": 1500.00},
    {"date": "02/12/2025", "product_name": "DAP", "quantity_received": 0, "quantity_sold": 2, "cost_price": 1334.00, "selling_price": 1500.00},
    {"date": "03/12/2025", "product_name": "DAP", "quantity_received": 0, "quantity_sold": 2, "cost_price": 1334.00, "selling_price": 1500.00},
    {"date": "06/12/2025", "product_name": "DAP", "quantity_received": 0, "quantity_sold": 2, "cost_price": 1334.00, "selling_price": 1500.00},
    {"date": "07/12/2025", "product_name": "DAP", "quantity_received": 0, "quantity_sold": 1, "cost_price": 1334.00, "selling_price": 1500.00},
    {"date": "10/12/2025", "product_name": "DAP", "quantity_received": 0, "quantity_sold": 3, "cost_price": 1334.00, "selling_price": 1500.00},
    {"date": "13/12/2025", "product_name": "DAP", "quantity_received": 0, "quantity_sold": 2, "cost_price": 1334.00, "selling_price": 1500.00},
    {"date": "17/12/2025", "product_name": "DAP", "quantity_received": 0, "quantity_sold": 1, "cost_price": 1334.00, "selling_price": 1500.00},
    {"date": "18/12/2025", "product_name": "DAP", "quantity_received": 0, "quantity_sold": 2, "cost_price": 1334.00, "selling_price": 1500.00},
    {"date": "20/12/2025", "product_name": "DAP", "quantity_received": 0, "quantity_sold": 1, "cost_price": 1334.00, "selling_price": 1500.00},
    {"date": "24/12/2025", "product_name": "DAP", "quantity_received": 0, "quantity_sold": 2, "cost_price": 1344.00, "selling_price": 1500.00}
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

def process_product_data(product_data, product_name, transactions):
    """Process data for a specific product"""
    print(f"\n📦 Processing {len(product_data)} {product_name} transactions...")
    
    for record in product_data:
        # Calculate fields
        stock_left = calculate_stock_left(transactions, product_name, record['quantity_received'], record['quantity_sold'])
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
        print(f"✅ {record['date']}: Received {record['quantity_received']}, Sold {record['quantity_sold']}, Stock: {stock_left}")
    
    return transactions

def insert_all_data():
    """Insert both Wheat and DAP data"""
    
    # Load existing data if any
    existing_data = {
        "products": ["Wheat", "Urea", "DAP", "Sarson", "Cow Feed", "Gandyal", "Him Cal", "Liv 52"], 
        "transactions": []
    }
    
    if os.path.exists(STORAGE_FILE):
        try:
            with open(STORAGE_FILE, 'r') as f:
                existing_data = json.load(f)
                print(f"📁 Found existing data with {len(existing_data.get('transactions', []))} transactions")
        except Exception as e:
            print(f"⚠️ Could not load existing data: {e}")
    
    transactions = existing_data.get('transactions', [])
    products = existing_data.get('products', ["Wheat", "Urea", "DAP", "Sarson", "Cow Feed", "Gandyal", "Him Cal", "Liv 52"])
    
    # Ensure products are in the list
    for product in ["Wheat", "DAP"]:
        if product not in products:
            products.append(product)
    
    print(f"🚀 Starting data insertion...")
    print(f"📊 Current transactions: {len(transactions)}")
    
    # Process Wheat data
    transactions = process_product_data(wheat_data, "Wheat", transactions)
    
    # Process DAP data
    transactions = process_product_data(dap_data, "DAP", transactions)
    
    # Save to storage file
    final_data = {
        'products': products,
        'transactions': transactions
    }
    
    with open(STORAGE_FILE, 'w') as f:
        json.dump(final_data, f, indent=4)
    
    print(f"\n🎉 SUCCESS! Data insertion completed!")
    print(f"📁 Data saved to: {STORAGE_FILE}")
    print(f"📦 Products: {len(products)} ({', '.join(products)})")
    print(f"📊 Total transactions: {len(transactions)}")
    print(f"🌾 Wheat transactions: {len([t for t in transactions if t['Product Name'] == 'Wheat'])}")
    print(f"🧪 DAP transactions: {len([t for t in transactions if t['Product Name'] == 'DAP'])}")
    print("\n🚀 Now run your Streamlit app to see all the data!")
    print("   Command: streamlit run app.py")

if __name__ == "__main__":
    try:
        insert_all_data()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure you have the correct permissions and the directory exists.")
        import traceback
        traceback.print_exc()