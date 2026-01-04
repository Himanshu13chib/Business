"""
Professional Inventory & Business Intelligence Dashboard
Agricultural Business Management System
Author: Senior Python Full-Stack Developer
Style: Elon Musk Professional - Minimalist, Efficient, Robust
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
from io import BytesIO

# Page Configuration
st.set_page_config(
    page_title="Inventory & BI Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional CSS Styling
st.markdown("""
<style>
    /* Main App Styling */
    .main {
        background-color: #0E1117;
    }
    
    /* Headers */
    h1 {
        color: #00D9FF;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 300;
        letter-spacing: -1px;
    }
    
    h2, h3 {
        color: #FFFFFF;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 300;
    }
    
    /* KPI Cards */
    .kpi-card {
        background: linear-gradient(135deg, #1E1E1E 0%, #2D2D2D 100%);
        border-left: 4px solid #00D9FF;
        border-radius: 8px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    .kpi-value {
        font-size: 36px;
        font-weight: 700;
        color: #00D9FF;
        margin: 0;
    }
    
    .kpi-label {
        font-size: 14px;
        color: #A0A0A0;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin: 0;
    }
    
    /* Table Styling - Excel-like */
    .dataframe {
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 13px;
        border-collapse: collapse;
        width: 100%;
        background-color: #FFFFFF;
    }
    
    .dataframe thead tr {
        background-color: #2C5F7C;
        color: #FFFFFF;
        text-align: left;
        font-weight: 600;
    }
    
    .dataframe th {
        padding: 12px 15px;
        border: 1px solid #DDDDDD;
    }
    
    .dataframe td {
        padding: 10px 15px;
        border: 1px solid #DDDDDD;
        color: #000000;
    }
    
    .dataframe tbody tr {
        background-color: #FFFFFF;
    }
    
    .dataframe tbody tr:nth-of-type(even) {
        background-color: #F3F3F3;
    }
    
    .dataframe tbody tr:hover {
        background-color: #E8F4F8;
        cursor: pointer;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background-color: #1E1E1E;
    }
    
    /* Metric Cards */
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, #1E1E1E 0%, #2D2D2D 100%);
        border-left: 4px solid #00D9FF;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00D9FF 0%, #0099CC 100%);
        color: #000000;
        font-weight: 600;
        border: none;
        border-radius: 6px;
        padding: 10px 24px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: linear-gradient(90deg, #00E5FF 0%, #00B3E6 100%);
        box-shadow: 0 6px 12px rgba(0, 217, 255, 0.4);
        transform: translateY(-2px);
    }
    
    /* Input Fields */
    .stTextInput>div>div>input,
    .stNumberInput>div>div>input,
    .stSelectbox>div>div>select,
    .stDateInput>div>div>input {
        background-color: #2D2D2D;
        color: #FFFFFF;
        border: 1px solid #404040;
        border-radius: 6px;
    }
    
    /* Success Messages */
    .stSuccess {
        background-color: #1E3A1E;
        color: #00FF00;
        border-left: 4px solid #00FF00;
    }
</style>
""", unsafe_allow_html=True)

# Data File Paths
import json
from pathlib import Path

# Storage Configuration
STORAGE_DIR = os.path.join(os.path.expanduser("~"), ".local", "share", "InventoryDashboard")
STORAGE_FILE = os.path.join(STORAGE_DIR, "data.json")

# Ensure storage directory exists
os.makedirs(STORAGE_DIR, exist_ok=True)

# Helper Functions for Storage
def load_storage():
    """Load data from JSON storage"""
    if os.path.exists(STORAGE_FILE):
        try:
            with open(STORAGE_FILE, 'r') as f:
                data = json.load(f)
            return data
        except Exception as e:
            st.error(f"Error reading storage: {e}")
            return None
    return None

def save_storage(products, df):
    """Save data to JSON storage"""
    try:
        data = {
            'products': products,
            'transactions': df.to_dict('records')
        }
        with open(STORAGE_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        st.error(f"Error saving storage: {e}")
        return False

# Default Product List (Initial Options)
DEFAULT_PRODUCTS = ["Wheat", "Urea", "DAP", "Sarson", "Cow Feed", "Gandyal", "Him Cal", "Liv 52"]

# Product Management Functions
def load_products():
    """Load products from JSON storage or use defaults"""
    data = load_storage()
    if data and 'products' in data:
        return data['products']
    return DEFAULT_PRODUCTS.copy()

def save_products(products_list):
    """Save products list to JSON storage"""
    # We need to preserve existing transactions when saving products
    # Get current df from session state if available, or load from disk
    if 'df' in st.session_state:
        df = st.session_state.df
    else:
        # Fallback if saving products before df is initialized
        data = load_storage()
        if data and 'transactions' in data:
            df = pd.DataFrame(data['transactions'])
        else:
            df = create_empty_dataframe()
            
    return save_storage(products_list, df)

def add_product(products_list, new_product):
    """Add a new product to the list"""
    if new_product and new_product.strip():
        new_product = new_product.strip()
        if new_product not in products_list:
            products_list.append(new_product)
            return True, f"✅ '{new_product}' added successfully!"
        else:
            return False, f"⚠️ '{new_product}' already exists!"
    return False, "⚠️ Product name cannot be empty!"

def remove_product(products_list, product_to_remove):
    """Remove a product from the list"""
    if product_to_remove in products_list:
        products_list.remove(product_to_remove)
        return True, f"✅ '{product_to_remove}' removed successfully!"
    return False, f"⚠️ Product not found!"

# Load Products
if 'products' not in st.session_state:
    st.session_state.products = load_products()

# Initialize Data
def init_data():
    """Initialize or load existing data"""
    data = load_storage()
    if data and 'transactions' in data:
        try:
            df = pd.DataFrame(data['transactions'])
            # Ensure safe handling of empty dataframes or missing columns
            if df.empty:
                return create_empty_dataframe()
            return df
        except Exception as e:
            st.error(f"Error loading data: {e}")
            return create_empty_dataframe()
    else:
        return create_empty_dataframe()

def create_empty_dataframe():
    """Create empty dataframe with required columns"""
    return pd.DataFrame(columns=[
        'Date', 'Product Name', 'Quantity Received', 'Quantity Sold', 
        'Stock Left', 'Cost Price', 'Selling Price', 'Total Purchase', 
        'Total Sales', 'Profit', 'Remarks'
    ])

def save_data(df):
    """Save dataframe to JSON storage"""
    # We need to preserve existing products
    if 'products' in st.session_state:
        products = st.session_state.products
    else:
        products = load_products()
        
    return save_storage(products, df)

def calculate_stock_left(df, product, qty_received, qty_sold):
    """Calculate stock left based on previous transactions"""
    product_df = df[df['Product Name'] == product]
    if len(product_df) > 0:
        previous_stock = product_df.iloc[-1]['Stock Left']
    else:
        previous_stock = 0
    
    new_stock = previous_stock + qty_received - qty_sold
    return new_stock

def add_transaction(df, date, product, qty_received, qty_sold, cost_price, selling_price, remarks):
    """Add new transaction with auto-calculations"""
    # Calculate fields
    stock_left = calculate_stock_left(df, product, qty_received, qty_sold)
    total_purchase = qty_received * cost_price
    total_sales = qty_sold * selling_price
    profit = (selling_price - cost_price) * qty_sold
    
    # Create new row
    new_row = {
        'Date': date,
        'Product Name': product,
        'Quantity Received': qty_received,
        'Quantity Sold': qty_sold,
        'Stock Left': stock_left,
        'Cost Price': cost_price,
        'Selling Price': selling_price,
        'Total Purchase': total_purchase,
        'Total Sales': total_sales,
        'Profit': profit,
        'Remarks': remarks
    }
    
    # Append to dataframe
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    return df

def create_excel_separate_sheets(df, products_list):
    """Create Excel file with separate sheet for each product"""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        # Create a sheet for each product
        for product in products_list:
            product_df = df[df['Product Name'] == product]
            if len(product_df) > 0:
                product_df.to_excel(writer, sheet_name=product[:31], index=False)  # Excel sheet name limit is 31 chars
        
        # Create a summary sheet with all data
        df.to_excel(writer, sheet_name='All Products', index=False)
    
    output.seek(0)
    return output

def delete_transaction(df, product, date):
    """Delete transaction for specific product and date, then recalculate stock"""
    # Find matching transactions
    mask = (df['Product Name'] == product) & (df['Date'] == date)
    
    if not df[mask].empty:
        # Get the index of the transaction to delete
        delete_idx = df[mask].index[0]
        
        # Delete the transaction
        df = df.drop(delete_idx).reset_index(drop=True)
        
        # Recalculate stock for all subsequent transactions of this product
        product_df = df[df['Product Name'] == product]
        if len(product_df) > 0:
            # Recalculate stock left for each transaction
            for idx in product_df.index:
                if idx == product_df.index[0]:
                    # First transaction of this product
                    df.at[idx, 'Stock Left'] = df.at[idx, 'Quantity Received'] - df.at[idx, 'Quantity Sold']
                else:
                    # Get previous transaction's stock
                    prev_idx = product_df.index[product_df.index.get_loc(idx) - 1]
                    prev_stock = df.at[prev_idx, 'Stock Left']
                    df.at[idx, 'Stock Left'] = prev_stock + df.at[idx, 'Quantity Received'] - df.at[idx, 'Quantity Sold']
        
        return df, True, "✅ Transaction deleted and stock recalculated!"
    else:
        return df, False, "⚠️ No transaction found for selected product and date!"

# Load Data
if 'df' not in st.session_state:
    st.session_state.df = init_data()

# ========================================
# SIDEBAR NAVIGATION
# ========================================
st.sidebar.title("🎯 Navigation")
page = st.sidebar.radio("Go to", ["📊 Dashboard", "📝 Data Entry", "📋 Ledger View", "📈 Profit Analysis", "🏭 Product Management"])

st.sidebar.markdown("---")
st.sidebar.title("🏷️ Product Filter")
selected_product = st.sidebar.selectbox(
    "Select Product",
    ["All Products"] + st.session_state.products,
    help="Filter view by specific product (Separate Hotel Logic)"
)

# Filter data based on selected product
if selected_product == "All Products":
    filtered_df = st.session_state.df
else:
    filtered_df = st.session_state.df[st.session_state.df['Product Name'] == selected_product]

# ========================================
# PAGE: DASHBOARD (Analytics)
# ========================================
if page == "📊 Dashboard":
    st.title("📊 Business Intelligence Dashboard")
    
    if len(filtered_df) == 0:
        st.warning("⚠️ No data available. Please add transactions in the Data Entry section.")
    else:
        # KPI Cards
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_sales = filtered_df['Total Sales'].sum()
            st.metric("💰 Total Sales", f"₹{total_sales:,.2f}")
        
        with col2:
            total_profit = filtered_df['Profit'].sum()
            st.metric("📈 Total Profit", f"₹{total_profit:,.2f}")
        
        with col3:
            if selected_product == "All Products":
                st.metric("📦 Products", len(st.session_state.products))
            else:
                current_stock = filtered_df.iloc[-1]['Stock Left'] if len(filtered_df) > 0 else 0
                st.metric("📦 Current Stock", f"{current_stock:,.0f} units")
        
        with col4:
            total_transactions = len(filtered_df)
            st.metric("🔄 Transactions", total_transactions)
        
        st.markdown("---")
        
        # Charts Section
        chart_col1, chart_col2 = st.columns(2)
        
        with chart_col1:
            st.subheader("📉 Stock Depletion Over Time")
            if selected_product != "All Products":
                # Line chart for stock depletion
                fig_stock = go.Figure()
                fig_stock.add_trace(go.Scatter(
                    x=list(range(1, len(filtered_df) + 1)),
                    y=filtered_df['Stock Left'],
                    mode='lines+markers',
                    name='Stock Left',
                    line=dict(color='#00D9FF', width=3),
                    marker=dict(size=8, color='#00D9FF')
                ))
                fig_stock.update_layout(
                    template='plotly_dark',
                    xaxis_title='Transaction Number',
                    yaxis_title='Stock Left (Units)',
                    hovermode='x unified',
                    height=400
                )
                st.plotly_chart(fig_stock, use_container_width=True)
            else:
                st.info("Select a specific product to view stock depletion chart")
        
        with chart_col2:
            st.subheader("🥧 Profit Margin by Product")
            # Pie chart for profit distribution
            profit_by_product = st.session_state.df.groupby('Product Name')['Profit'].sum().reset_index()
            profit_by_product = profit_by_product[profit_by_product['Profit'] > 0]
            
            if len(profit_by_product) > 0:
                fig_profit = px.pie(
                    profit_by_product,
                    values='Profit',
                    names='Product Name',
                    hole=0.4,
                    color_discrete_sequence=px.colors.sequential.Turbo
                )
                fig_profit.update_layout(
                    template='plotly_dark',
                    height=400
                )
                st.plotly_chart(fig_profit, use_container_width=True)
            else:
                st.info("No profit data available yet")
        
        st.markdown("---")
        
        # Additional Analytics
        st.subheader("📊 Product Performance Summary")
        
        if selected_product == "All Products":
            summary_df = st.session_state.df.groupby('Product Name').agg({
                'Quantity Received': 'sum',
                'Quantity Sold': 'sum',
                'Total Purchase': 'sum',
                'Total Sales': 'sum',
                'Profit': 'sum'
            }).reset_index()
            
            # Add current stock for each product
            current_stocks = []
            for product in summary_df['Product Name']:
                product_data = st.session_state.df[st.session_state.df['Product Name'] == product]
                if len(product_data) > 0:
                    current_stocks.append(product_data.iloc[-1]['Stock Left'])
                else:
                    current_stocks.append(0)
            
            summary_df['Current Stock'] = current_stocks
            
            # Reorder columns
            summary_df = summary_df[['Product Name', 'Current Stock', 'Quantity Received', 
                                    'Quantity Sold', 'Total Purchase', 'Total Sales', 'Profit']]
            
            st.dataframe(summary_df, use_container_width=True, hide_index=True)
        else:
            st.info(f"Viewing detailed data for {selected_product} in Ledger View")

# ========================================
# PAGE: DATA ENTRY
# ========================================
elif page == "📝 Data Entry":
    st.title("📝 Data Entry Portal")
    
    # Tab selection for Single vs Bulk entry
    entry_tab = st.radio(
        "Select Entry Method",
        ["📝 Single Transaction", "📊 Bulk Import"],
        horizontal=True
    )
    
    if entry_tab == "📝 Single Transaction":
        st.markdown("### Add New Transaction")
        
        with st.form("transaction_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            date_input = st.date_input("📅 Date", datetime.now())
            product = st.selectbox("🏷️ Product Name", st.session_state.products)
            qty_received = st.number_input("📦 Quantity Received", min_value=0.0, value=0.0, step=1.0)
            qty_sold = st.number_input("🛒 Quantity Sold", min_value=0.0, value=0.0, step=1.0)
            cost_price = st.number_input("💵 Cost Price (per unit)", min_value=0.0, value=0.0, step=0.01)
        
        with col2:
            selling_price = st.number_input("💰 Selling Price (per unit)", min_value=0.0, value=0.0, step=0.01)
            remarks = st.text_area("📝 Remarks", "")
            
            # Show calculated preview
            st.markdown("### 📊 Transaction Preview")
            preview_stock = calculate_stock_left(st.session_state.df, product, qty_received, qty_sold)
            preview_purchase = qty_received * cost_price
            preview_sales = qty_sold * selling_price
            preview_profit = (selling_price - cost_price) * qty_sold
            
            st.info(f"""
            **Stock After Transaction:** {preview_stock:,.2f} units  
            **Total Purchase:** ₹{preview_purchase:,.2f}  
            **Total Sales:** ₹{preview_sales:,.2f}  
            **Profit:** ₹{preview_profit:,.2f}
            """)
        
        submitted = st.form_submit_button("✅ Add Transaction", use_container_width=True)
        
        if submitted:
            # Convert date to DD/MM/YYYY format
            date_str = date_input.strftime('%d/%m/%Y')
            
            # Add transaction
            st.session_state.df = add_transaction(
                st.session_state.df,
                date_str,
                product,
                qty_received,
                qty_sold,
                cost_price,
                selling_price,
                remarks
            )
            
            # Save to file
            if save_data(st.session_state.df):
                st.success("✅ Transaction added successfully!")
                st.balloons()
            else:
                st.error("❌ Failed to save transaction")
    
    elif entry_tab == "📊 Bulk Import":
        st.markdown("### Bulk Import Transactions")
        st.info("💡 Import multiple transactions at once using JSON format")
        
        # JSON input area
        json_input = st.text_area(
            "📋 Paste JSON Data",
            height=300,
            placeholder='[{"date": "24/10/2025", "product_name": "Wheat", "quantity_received": 150, "quantity_sold": 23, "cost_price": 1488.00, "selling_price": 1650.00, "remarks": ""}]',
            help="Paste your JSON data here. Each record should have: date, product_name, quantity_received, quantity_sold, cost_price, selling_price, remarks (optional)"
        )
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            if st.button("🔍 Preview Data", use_container_width=True):
                if json_input.strip():
                    try:
                        import json
                        data = json.loads(json_input)
                        
                        # Convert to DataFrame for preview
                        preview_df = pd.DataFrame(data)
                        
                        # Validate required columns
                        required_cols = ['date', 'product_name', 'quantity_received', 'quantity_sold', 'cost_price', 'selling_price']
                        missing_cols = [col for col in required_cols if col not in preview_df.columns]
                        
                        if missing_cols:
                            st.error(f"❌ Missing required columns: {', '.join(missing_cols)}")
                        else:
                            st.success(f"✅ Found {len(preview_df)} valid records")
                            st.dataframe(preview_df, use_container_width=True)
                            
                    except json.JSONDecodeError as e:
                        st.error(f"❌ Invalid JSON format: {str(e)}")
                    except Exception as e:
                        st.error(f"❌ Error processing data: {str(e)}")
                else:
                    st.warning("⚠️ Please paste JSON data first")
        
        with col2:
            if st.button("✅ Import All Records", use_container_width=True, type="primary"):
                if json_input.strip():
                    try:
                        import json
                        data = json.loads(json_input)
                        
                        success_count = 0
                        error_count = 0
                        
                        for record in data:
                            try:
                                # Extract data with defaults
                                date_str = record.get('date', '')
                                product = record.get('product_name', '')
                                qty_received = float(record.get('quantity_received', 0))
                                qty_sold = float(record.get('quantity_sold', 0))
                                cost_price = float(record.get('cost_price', 0))
                                selling_price = float(record.get('selling_price', 0))
                                remarks = record.get('remarks', '')
                                
                                # Validate product exists
                                if product not in st.session_state.products:
                                    st.session_state.products.append(product)
                                    save_products(st.session_state.products)
                                
                                # Add transaction
                                st.session_state.df = add_transaction(
                                    st.session_state.df,
                                    date_str,
                                    product,
                                    qty_received,
                                    qty_sold,
                                    cost_price,
                                    selling_price,
                                    remarks
                                )
                                success_count += 1
                                
                            except Exception as e:
                                error_count += 1
                                st.error(f"❌ Error in record {success_count + error_count}: {str(e)}")
                        
                        # Save all data
                        if save_data(st.session_state.df):
                            st.success(f"✅ Successfully imported {success_count} records!")
                            if error_count > 0:
                                st.warning(f"⚠️ {error_count} records had errors")
                            st.balloons()
                        else:
                            st.error("❌ Failed to save imported data")
                            
                    except json.JSONDecodeError as e:
                        st.error(f"❌ Invalid JSON format: {str(e)}")
                    except Exception as e:
                        st.error(f"❌ Error during import: {str(e)}")
                else:
                    st.warning("⚠️ Please paste JSON data first")
        
        # Sample format help
        st.markdown("---")
        st.subheader("📋 JSON Format Guide")
        st.code('''
[
  {
    "date": "24/10/2025",
    "product_name": "Wheat",
    "quantity_received": 150,
    "quantity_sold": 23,
    "cost_price": 1488.00,
    "selling_price": 1650.00,
    "remarks": "Optional notes"
  }
]
        ''', language='json')
        
        st.markdown("**Required Fields:** date, product_name, quantity_received, quantity_sold, cost_price, selling_price")
        st.markdown("**Optional Fields:** remarks")
    
    # Show recent transactions (for both tabs)
    st.markdown("---")
    st.subheader("📋 Recent Transactions")
    if len(st.session_state.df) > 0:
        recent_df = st.session_state.df.tail(10).iloc[::-1]  # Last 10 in reverse
        st.dataframe(recent_df, use_container_width=True, hide_index=True)
    else:
        st.info("No transactions yet")

# ========================================
# PAGE: LEDGER VIEW
# ========================================
elif page == "📋 Ledger View":
    st.title("📋 Inventory Ledger")
    
    if selected_product != "All Products":
        st.markdown(f"### 🏷️ Product: {selected_product}")
    
    if len(filtered_df) == 0:
        st.warning("⚠️ No transactions found for the selected filter.")
    else:
        # Display options
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        
        with col1:
            st.markdown(f"**Total Records:** {len(filtered_df)}")
        
        with col2:
            if st.button("📥 CSV"):
                csv = filtered_df.to_csv(index=False)
                st.download_button(
                    label="💾 Download CSV",
                    data=csv,
                    file_name=f"ledger_{selected_product}_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv"
                )
        
        with col3:
            if st.button("📊 Excel (Separate)"):
                excel_data = create_excel_separate_sheets(st.session_state.df, st.session_state.products)
                st.download_button(
                    label="💾 Download Excel",
                    data=excel_data,
                    file_name=f"inventory_separate_sheets_{datetime.now().strftime('%Y%m%d')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        
        with col4:
            if st.button("🔄 Refresh"):
                st.session_state.df = init_data()
                st.success("Data refreshed!")
        
        # Format numeric columns for display
        display_df = filtered_df.copy()
        numeric_cols = ['Quantity Received', 'Quantity Sold', 'Stock Left', 
                       'Cost Price', 'Selling Price', 'Total Purchase', 'Total Sales', 'Profit']
        
        for col in numeric_cols:
            if col in display_df.columns:
                display_df[col] = display_df[col].apply(lambda x: f"{x:,.2f}")
        
        # Display table
        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
            height=600
        )
        
        # Summary Statistics
        st.markdown("---")
        st.subheader("📊 Summary Statistics")
        
        sum_col1, sum_col2, sum_col3, sum_col4 = st.columns(4)
        
        with sum_col1:
            st.metric("📦 Total Received", f"{filtered_df['Quantity Received'].sum():,.2f}")
        
        with sum_col2:
            st.metric("🛒 Total Sold", f"{filtered_df['Quantity Sold'].sum():,.2f}")
        
        with sum_col3:
            st.metric("💰 Total Revenue", f"₹{filtered_df['Total Sales'].sum():,.2f}")
        
        with sum_col4:
            st.metric("📈 Total Profit", f"₹{filtered_df['Profit'].sum():,.2f}")
        
        # Delete Transaction Section
        st.markdown("---")
        st.subheader("🗑️ Delete Transaction")
        st.warning("⚠️ Use this carefully! Deleting a transaction will recalculate stock levels for all subsequent transactions.")
        
        # Initialize deletion state
        if 'delete_confirm' not in st.session_state:
            st.session_state.delete_confirm = False
        if 'delete_product_selected' not in st.session_state:
            st.session_state.delete_product_selected = None
        if 'delete_date_selected' not in st.session_state:
            st.session_state.delete_date_selected = None
        
        del_col1, del_col2, del_col3 = st.columns([2, 2, 1])
        
        with del_col1:
            # Get products that have transactions
            products_with_transactions = st.session_state.df['Product Name'].unique().tolist() if len(st.session_state.df) > 0 else []
            
            if products_with_transactions:
                delete_product = st.selectbox(
                    "Select Product",
                    products_with_transactions,
                    key="delete_product_select",
                    help="Select the product for which you want to delete a transaction"
                )
            else:
                st.info("No transactions available to delete")
                delete_product = None
        
        with del_col2:
            if delete_product:
                # Get dates for selected product
                product_dates = st.session_state.df[st.session_state.df['Product Name'] == delete_product]['Date'].unique().tolist()
                
                if product_dates:
                    delete_date = st.selectbox(
                        "Select Date",
                        product_dates,
                        key="delete_date_select",
                        help="Select the date of the transaction to delete"
                    )
                else:
                    st.info("No dates available for this product")
                    delete_date = None
            else:
                delete_date = None
        
        with del_col3:
            st.write("")  # Spacing
            st.write("")  # Spacing
            if delete_product and delete_date:
                if not st.session_state.delete_confirm:
                    # First click - Request confirmation
                    if st.button("🗑️ Delete", type="primary", use_container_width=True, key="delete_btn"):
                        st.session_state.delete_confirm = True
                        st.session_state.delete_product_selected = delete_product
                        st.session_state.delete_date_selected = delete_date
                        st.rerun()
                else:
                    # Confirmation mode - Show confirm/cancel
                    if st.button("⚠️ Confirm", type="primary", use_container_width=True, key="confirm_btn"):
                        new_df, success, message = delete_transaction(
                            st.session_state.df.copy(),
                            st.session_state.delete_product_selected,
                            st.session_state.delete_date_selected
                        )
                        
                        if success:
                            st.session_state.df = new_df
                            if save_data(st.session_state.df):
                                st.success(message)
                                st.session_state.delete_confirm = False
                                st.session_state.delete_product_selected = None
                                st.session_state.delete_date_selected = None
                                st.rerun()
                            else:
                                st.error("Failed to save changes")
                                st.session_state.delete_confirm = False
                        else:
                            st.warning(message)
                            st.session_state.delete_confirm = False
        
        # Show preview if in confirmation mode
        if st.session_state.delete_confirm and st.session_state.delete_product_selected and st.session_state.delete_date_selected:
            st.markdown("---")
            st.warning(f"⚠️ **Confirm Deletion:** {st.session_state.delete_product_selected} | {st.session_state.delete_date_selected}")
            
            preview_df = st.session_state.df[
                (st.session_state.df['Product Name'] == st.session_state.delete_product_selected) & 
                (st.session_state.df['Date'] == st.session_state.delete_date_selected)
            ]
            
            if not preview_df.empty:
                st.dataframe(preview_df, use_container_width=True, hide_index=True)
                
                col1, col2 = st.columns(2)
                with col2:
                    if st.button("❌ Cancel", use_container_width=True, key="cancel_btn"):
                        st.session_state.delete_confirm = False
                        st.session_state.delete_product_selected = None
                        st.session_state.delete_date_selected = None
                        st.rerun()

# ========================================
# PAGE: PROFIT ANALYSIS
# ========================================
elif page == "📈 Profit Analysis":
    st.title("📈 Comprehensive Profit Analysis")
    
    if len(st.session_state.df) == 0:
        st.warning("⚠️ No data available for analysis. Please add transactions first.")
    else:
        # Tab selection for Individual vs Combined
        analysis_tab = st.radio(
            "Select Analysis Type",
            ["📊 Individual Product Analysis", "🎯 Final Combined Analysis"],
            horizontal=True
        )
        
        st.markdown("---")
        
        # ========================================
        # INDIVIDUAL PRODUCT ANALYSIS
        # ========================================
        if analysis_tab == "📊 Individual Product Analysis":
            st.subheader("📊 Product-Wise Profit Analysis")
            
            # Product selector
            products_with_data = st.session_state.df['Product Name'].unique().tolist()
            
            if len(products_with_data) == 0:
                st.info("No products with transaction data yet.")
            else:
                selected_analysis_product = st.selectbox(
                    "Select Product for Analysis",
                    products_with_data,
                    help="Choose a product to view detailed profit analysis"
                )
                
                # Filter data for selected product
                product_data = st.session_state.df[st.session_state.df['Product Name'] == selected_analysis_product]
                
                st.markdown(f"### 📦 Analysis for: **{selected_analysis_product}**")
                st.markdown("---")
                
                # KPI Cards for this product
                kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
                
                with kpi_col1:
                    total_received = product_data['Quantity Received'].sum()
                    st.metric("📦 Total Received", f"{total_received:,.0f} units")
                
                with kpi_col2:
                    total_sold = product_data['Quantity Sold'].sum()
                    st.metric("🛒 Total Sold", f"{total_sold:,.0f} units")
                
                with kpi_col3:
                    current_stock = product_data.iloc[-1]['Stock Left']
                    st.metric("📊 Current Stock", f"{current_stock:,.0f} units")
                
                with kpi_col4:
                    total_transactions = len(product_data)
                    st.metric("🔄 Transactions", total_transactions)
                
                st.markdown("---")
                
                # Financial Metrics
                st.subheader("💰 Financial Performance")
                
                fin_col1, fin_col2, fin_col3, fin_col4 = st.columns(4)
                
                with fin_col1:
                    total_purchase = product_data['Total Purchase'].sum()
                    st.metric("💵 Total Investment", f"₹{total_purchase:,.2f}")
                
                with fin_col2:
                    total_revenue = product_data['Total Sales'].sum()
                    st.metric("💰 Total Revenue", f"₹{total_revenue:,.2f}")
                
                with fin_col3:
                    total_profit = product_data['Profit'].sum()
                    st.metric("📈 Total Profit", f"₹{total_profit:,.2f}")
                
                with fin_col4:
                    profit_margin = (total_profit / total_revenue * 100) if total_revenue > 0 else 0
                    st.metric("📊 Profit Margin", f"{profit_margin:.1f}%")
                
                st.markdown("---")
                
                # Charts for this product
                chart_col1, chart_col2 = st.columns(2)
                
                with chart_col1:
                    st.subheader("📉 Stock Movement Over Time")
                    fig_stock = go.Figure()
                    fig_stock.add_trace(go.Scatter(
                        x=list(range(1, len(product_data) + 1)),
                        y=product_data['Stock Left'],
                        mode='lines+markers',
                        name='Stock Level',
                        line=dict(color='#00D9FF', width=3),
                        marker=dict(size=8, color='#00D9FF'),
                        fill='tozeroy',
                        fillcolor='rgba(0, 217, 255, 0.2)'
                    ))
                    fig_stock.update_layout(
                        template='plotly_dark',
                        xaxis_title='Transaction Number',
                        yaxis_title='Stock (Units)',
                        hovermode='x unified',
                        height=400
                    )
                    st.plotly_chart(fig_stock, use_container_width=True)
                
                with chart_col2:
                    st.subheader("💰 Cumulative Profit")
                    cumulative_profit = product_data['Profit'].cumsum()
                    fig_profit = go.Figure()
                    fig_profit.add_trace(go.Scatter(
                        x=list(range(1, len(product_data) + 1)),
                        y=cumulative_profit,
                        mode='lines+markers',
                        name='Cumulative Profit',
                        line=dict(color='#00FF7F', width=3),
                        marker=dict(size=8, color='#00FF7F'),
                        fill='tozeroy',
                        fillcolor='rgba(0, 255, 127, 0.2)'
                    ))
                    fig_profit.update_layout(
                        template='plotly_dark',
                        xaxis_title='Transaction Number',
                        yaxis_title='Cumulative Profit (₹)',
                        hovermode='x unified',
                        height=400
                    )
                    st.plotly_chart(fig_profit, use_container_width=True)
                
                st.markdown("---")
                
                # Transaction History Table
                st.subheader("📋 Transaction History")
                display_cols = ['Date', 'Quantity Received', 'Quantity Sold', 'Stock Left', 
                               'Cost Price', 'Selling Price', 'Total Purchase', 'Total Sales', 'Profit', 'Remarks']
                st.dataframe(product_data[display_cols], use_container_width=True, hide_index=True)
                
                # Download individual product report
                st.markdown("---")
                st.subheader("📥 Export Product Report")
                
                excel_single = BytesIO()
                with pd.ExcelWriter(excel_single, engine='openpyxl') as writer:
                    product_data.to_excel(writer, sheet_name=selected_analysis_product[:31], index=False)
                excel_single.seek(0)
                
                st.download_button(
                    label=f"📊 Download {selected_analysis_product} Report (Excel)",
                    data=excel_single,
                    file_name=f"{selected_analysis_product}_analysis_{datetime.now().strftime('%Y%m%d')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )
        
        # ========================================
        # FINAL COMBINED ANALYSIS
        # ========================================
        else:
            st.subheader("🎯 Final Combined Analysis - All Products")
            
            # Overall KPIs
            st.markdown("### 📊 Overall Business Performance")
            
            overall_col1, overall_col2, overall_col3, overall_col4, overall_col5 = st.columns(5)
            
            with overall_col1:
                total_products = len(st.session_state.df['Product Name'].unique())
                st.metric("🏷️ Active Products", total_products)
            
            with overall_col2:
                total_investment = st.session_state.df['Total Purchase'].sum()
                st.metric("💵 Total Investment", f"₹{total_investment:,.0f}")
            
            with overall_col3:
                total_revenue = st.session_state.df['Total Sales'].sum()
                st.metric("💰 Total Revenue", f"₹{total_revenue:,.0f}")
            
            with overall_col4:
                total_profit = st.session_state.df['Profit'].sum()
                st.metric("📈 Total Profit", f"₹{total_profit:,.0f}")
            
            with overall_col5:
                overall_margin = (total_profit / total_revenue * 100) if total_revenue > 0 else 0
                st.metric("📊 Overall Margin", f"{overall_margin:.1f}%")
            
            st.markdown("---")
            
            # Product-wise comparison
            st.subheader("📊 Product-Wise Comparison")
            
            comparison_df = st.session_state.df.groupby('Product Name').agg({
                'Quantity Received': 'sum',
                'Quantity Sold': 'sum',
                'Total Purchase': 'sum',
                'Total Sales': 'sum',
                'Profit': 'sum'
            }).reset_index()
            
            # Add current stock and profit margin
            current_stocks = []
            profit_margins = []
            for product in comparison_df['Product Name']:
                product_df = st.session_state.df[st.session_state.df['Product Name'] == product]
                current_stocks.append(product_df.iloc[-1]['Stock Left'])
                margin = (comparison_df[comparison_df['Product Name'] == product]['Profit'].values[0] / 
                         comparison_df[comparison_df['Product Name'] == product]['Total Sales'].values[0] * 100) \
                         if comparison_df[comparison_df['Product Name'] == product]['Total Sales'].values[0] > 0 else 0
                profit_margins.append(margin)
            
            comparison_df['Current Stock'] = current_stocks
            comparison_df['Profit Margin %'] = profit_margins
            
            # Reorder columns
            comparison_df = comparison_df[['Product Name', 'Current Stock', 'Quantity Received', 'Quantity Sold',
                                          'Total Purchase', 'Total Sales', 'Profit', 'Profit Margin %']]
            
            # Format for display
            display_comparison = comparison_df.copy()
            for col in ['Current Stock', 'Quantity Received', 'Quantity Sold']:
                display_comparison[col] = display_comparison[col].apply(lambda x: f"{x:,.0f}")
            for col in ['Total Purchase', 'Total Sales', 'Profit']:
                display_comparison[col] = display_comparison[col].apply(lambda x: f"₹{x:,.2f}")
            display_comparison['Profit Margin %'] = display_comparison['Profit Margin %'].apply(lambda x: f"{x:.1f}%")
            
            st.dataframe(display_comparison, use_container_width=True, hide_index=True)
            
            st.markdown("---")
            
            # Visualizations
            viz_col1, viz_col2 = st.columns(2)
            
            with viz_col1:
                st.subheader("💰 Revenue by Product")
                fig_revenue = px.bar(
                    comparison_df,
                    x='Product Name',
                    y='Total Sales',
                    color='Profit',
                    color_continuous_scale='Turbo',
                    labels={'Total Sales': 'Revenue (₹)', 'Profit': 'Profit (₹)'}
                )
                fig_revenue.update_layout(
                    template='plotly_dark',
                    height=400,
                    xaxis_tickangle=-45
                )
                st.plotly_chart(fig_revenue, use_container_width=True)
            
            with viz_col2:
                st.subheader("📈 Profit Distribution")
                fig_profit_pie = px.pie(
                    comparison_df,
                    values='Profit',
                    names='Product Name',
                    hole=0.4,
                    color_discrete_sequence=px.colors.sequential.Turbo
                )
                fig_profit_pie.update_layout(
                    template='plotly_dark',
                    height=400
                )
                st.plotly_chart(fig_profit_pie, use_container_width=True)
            
            st.markdown("---")
            
            # Top Performers
            st.subheader("🏆 Top Performers")
            
            perf_col1, perf_col2, perf_col3 = st.columns(3)
            
            with perf_col1:
                st.markdown("**💰 Highest Revenue**")
                top_revenue = comparison_df.nlargest(3, 'Total Sales')[['Product Name', 'Total Sales']]
                for idx, row in top_revenue.iterrows():
                    st.write(f"🥇 {row['Product Name']}: ₹{row['Total Sales']:,.2f}")
            
            with perf_col2:
                st.markdown("**📈 Highest Profit**")
                top_profit = comparison_df.nlargest(3, 'Profit')[['Product Name', 'Profit']]
                for idx, row in top_profit.iterrows():
                    st.write(f"🥇 {row['Product Name']}: ₹{row['Profit']:,.2f}")
            
            with perf_col3:
                st.markdown("**📊 Best Margin**")
                top_margin = comparison_df.nlargest(3, 'Profit Margin %')[['Product Name', 'Profit Margin %']]
                for idx, row in top_margin.iterrows():
                    st.write(f"🥇 {row['Product Name']}: {row['Profit Margin %']:.1f}%")
            
            st.markdown("---")
            
            # Download Combined Report
            st.subheader("📥 Export Combined Report")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Excel with separate sheets
                excel_combined = create_excel_separate_sheets(st.session_state.df, st.session_state.products)
                st.download_button(
                    label="📊 Download All Products (Separate Sheets)",
                    data=excel_combined,
                    file_name=f"all_products_separate_{datetime.now().strftime('%Y%m%d')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )
            
            with col2:
                # Excel with summary
                excel_summary = BytesIO()
                with pd.ExcelWriter(excel_summary, engine='openpyxl') as writer:
                    comparison_df.to_excel(writer, sheet_name='Summary', index=False)
                    st.session_state.df.to_excel(writer, sheet_name='All Transactions', index=False)
                excel_summary.seek(0)
                
                st.download_button(
                    label="📊 Download Summary Report",
                    data=excel_summary,
                    file_name=f"summary_report_{datetime.now().strftime('%Y%m%d')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )

# ========================================
# PAGE: PRODUCT MANAGEMENT
# ========================================
elif page == "🏭 Product Management":
    st.title("🏭 Product Management Portal")
    st.markdown("### Add or Remove Products Dynamically")
    
    # Add New Product Section
    st.markdown("---")
    st.subheader("➕ Add New Product")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        new_product_name = st.text_input(
            "📦 Product Name",
            placeholder="Enter new product name (e.g., Rice, Mustard Oil)",
            help="Enter the name of the product you want to add"
        )
    
    with col2:
        st.write("")  # Spacing
        st.write("")  # Spacing
        if st.button("✅ Add Product", use_container_width=True):
            success, message = add_product(st.session_state.products, new_product_name)
            if success:
                if save_products(st.session_state.products):
                    st.success(message)
                    st.balloons()
                else:
                    st.error("Failed to save product list")
            else:
                st.warning(message)
    
    # Current Products Section
    st.markdown("---")
    st.subheader("📋 Current Products")
    
    if len(st.session_state.products) > 0:
        # Create a nice display of products
        st.markdown(f"**Total Products:** {len(st.session_state.products)}")
        
        # Display in a grid
        cols_per_row = 3
        for i in range(0, len(st.session_state.products), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, col in enumerate(cols):
                idx = i + j
                if idx < len(st.session_state.products):
                    product = st.session_state.products[idx]
                    with col:
                        # Product card
                        st.markdown(f"""
                        <div style='background: linear-gradient(135deg, #1E1E1E 0%, #2D2D2D 100%);
                                    border-left: 4px solid #00D9FF;
                                    border-radius: 8px;
                                    padding: 15px;
                                    margin: 10px 0;
                                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);'>
                            <p style='color: #00D9FF; font-size: 18px; font-weight: 600; margin: 0;'>🏷️ {product}</p>
                        </div>
                        """, unsafe_allow_html=True)
        
        # Remove Product Section
        st.markdown("---")
        st.subheader("🗑️ Remove Product")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            product_to_remove = st.selectbox(
                "Select Product to Remove",
                st.session_state.products,
                help="WARNING: Removing a product will not delete its transaction history"
            )
        
        with col2:
            st.write("")  # Spacing
            st.write("")  # Spacing
            if st.button("🗑️ Remove", use_container_width=True):
                # Check if product has transactions
                has_transactions = len(st.session_state.df[st.session_state.df['Product Name'] == product_to_remove]) > 0
                
                if has_transactions:
                    st.warning(f"⚠️ '{product_to_remove}' has existing transactions. Are you sure?")
                    if st.button("⚠️ Confirm Removal", type="primary"):
                        success, message = remove_product(st.session_state.products, product_to_remove)
                        if success:
                            if save_products(st.session_state.products):
                                st.success(message)
                                st.info("Note: Transaction history for this product is preserved in the ledger.")
                            else:
                                st.error("Failed to save product list")
                        else:
                            st.error(message)
                else:
                    success, message = remove_product(st.session_state.products, product_to_remove)
                    if success:
                        if save_products(st.session_state.products):
                            st.success(message)
                        else:
                            st.error("Failed to save product list")
                    else:
                        st.error(message)
        
        # Product Statistics
        st.markdown("---")
        st.subheader("📊 Product Statistics")
        
        # Show which products have transactions
        products_with_data = st.session_state.df['Product Name'].unique().tolist() if len(st.session_state.df) > 0 else []
        products_without_data = [p for p in st.session_state.products if p not in products_with_data]
        
        stat_col1, stat_col2 = st.columns(2)
        
        with stat_col1:
            st.metric("📦 Products with Transactions", len(products_with_data))
            if products_with_data:
                st.write("✅ " + ", ".join(products_with_data))
        
        with stat_col2:
            st.metric("📦 Products without Transactions", len(products_without_data))
            if products_without_data:
                st.write("⚪ " + ", ".join(products_without_data))
    
    else:
        st.warning("⚠️ No products available. Add some products to get started!")
    
    # Reset to Defaults
    st.markdown("---")
    st.subheader("🔄 Reset Options")
    
    if st.button("🔄 Reset to Default Products", help="Restore original 8 agricultural products"):
        st.session_state.products = DEFAULT_PRODUCTS.copy()
        if save_products(st.session_state.products):
            st.success("✅ Product list reset to defaults!")
            st.info("Default products: " + ", ".join(DEFAULT_PRODUCTS))
        else:
            st.error("Failed to save product list")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style='text-align: center; color: #606060; font-size: 12px;'>
    <p><strong>Professional Inventory Dashboard</strong></p>
    <p>Agricultural Business Intelligence</p>
    <p style='color: #00D9FF;'>Built with Streamlit & Plotly</p>
</div>
""", unsafe_allow_html=True)
