"""
Complete Data Insertion Script for Inventory Dashboard
This script inserts Wheat, DAP, and Urea data into your app's storage file
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

# Your Urea data
urea_data = [
    {"date": "24/10/2025", "product_name": "Urea", "quantity_received": 303, "quantity_sold": 5, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "25/10/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 13, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "26/10/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 1, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "27/10/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 2, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "28/10/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 1, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "29/10/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 3, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "30/10/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 2, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "31/10/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 1, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "01/11/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 2, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "02/11/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 1, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "03/11/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 2, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "04/11/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 7, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "05/11/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 21, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "06/11/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 7, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "07/11/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 18, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "08/11/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 3, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "09/11/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 24, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "10/11/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 4, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "11/11/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 9, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "12/11/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 4, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "13/11/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 2, "cost_price": 261.50, "selling_price": 300.00},
    {"date": "16/11/2025", "product_name": "Urea", "quantity_received": 0, "quantity_sold": 7, "cost_price": 261.50, "selling_price": 300.00}
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

def insert_complete_data():
    """Insert Wheat, DAP, and Urea data"""
    
    # Clear existing data and start fresh
    existing_data = {
        "products": ["Wheat", "Urea", "DAP", "Sarson", "Cow Feed", "Gandyal", "Him Cal", "Liv 52"], 
        "transactions": []
    }
    
    transactions = []
    products = ["Wheat", "Urea", "DAP", "Sarson", "Cow Feed", "Gandyal", "Him Cal", "Liv 52"]
    
    print(f"🚀 Starting complete data insertion...")
    print(f"📊 Starting fresh with 0 transactions")
    
    # Process all products in chronological order
    all_data = []
    
    # Add all transactions with dates for sorting
    for record in wheat_data:
        all_data.append((record['date'], 'Wheat', record))
    for record in dap_data:
        all_data.append((record['date'], 'DAP', record))
    for record in urea_data:
        all_data.append((record['date'], 'Urea', record))
    
    # Sort by date
    from datetime import datetime
    all_data.sort(key=lambda x: datetime.strptime(x[0], '%d/%m/%Y'))
    
    print(f"\n📅 Processing {len(all_data)} transactions in chronological order...")
    
    for date_str, product_name, record in all_data:
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
        print(f"✅ {date_str} - {product_name}: Stock {stock_left}")
    
    # Save to storage file
    final_data = {
        'products': products,
        'transactions': transactions
    }
    
    with open(STORAGE_FILE, 'w') as f:
        json.dump(final_data, f, indent=4)
    
    print(f"\n🎉 SUCCESS! Complete data insertion finished!")
    print(f"📁 Data saved to: {STORAGE_FILE}")
    print(f"📦 Products: {len(products)} ({', '.join(products)})")
    print(f"📊 Total transactions: {len(transactions)}")
    print(f"🌾 Wheat transactions: {len([t for t in transactions if t['Product Name'] == 'Wheat'])}")
    print(f"🧪 DAP transactions: {len([t for t in transactions if t['Product Name'] == 'DAP'])}")
    print(f"🧪 Urea transactions: {len([t for t in transactions if t['Product Name'] == 'Urea'])}")
    print("\n🚀 Now run your Streamlit app to see all the data!")
    print("   Command: python -m streamlit run app.py")

if __name__ == "__main__":
    try:
        insert_complete_data()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure you have the correct permissions and the directory exists.")
        import traceback
        traceback.print_exc()