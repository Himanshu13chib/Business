# 📊 Professional Inventory & Business Intelligence Dashboard

**Agricultural Business Management System**

A minimalist, efficient, and robust inventory management dashboard built with Python, Streamlit, Pandas, and Plotly.

---

## 🎯 Features

### 🏗️ Core Functionality
- **11-Column Data Structure** with auto-calculations
- **Product Portal System** (Separate Hotel Logic) - Filter by individual products
- **Smart Auto-Calculations**:
  - Stock Left (Previous Stock + Received - Sold)
  - Total Purchase (Qty Received × Cost Price)  
  - Total Sales (Qty Sold × Selling Price)
  - Profit ((Selling Price - Cost Price) × Qty Sold)

### 📱 Three-Page Interface
1. **📊 Dashboard** - Analytics & KPI Cards
2. **📝 Data Entry** - Transaction input form
3. **📋 Ledger View** - Excel-style data table

### 📈 Analytics & Visualizations
- **KPI Cards**: Total Sales, Total Profit, Current Stock, Transaction Count
- **Stock Depletion Chart** (Plotly Line Chart)
- **Profit Margin Pie Chart** (Plotly)
- **Product Performance Summary Table**

### 🎨 Design
- Professional "Elon Musk" style - Minimalist & Efficient
- Dark theme with cyan accents (#00D9FF)
- Excel-style table formatting
- Responsive layout
- Smooth hover effects and animations

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Navigate to project directory**
   ```bash
   cd C:\Users\asus\.gemini\antigravity\scratch\inventory-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the dashboard**
   - The app will automatically open in your default browser
   - Default URL: `http://localhost:8501`

---

## 📖 Usage Guide

### 1️⃣ Data Entry
1. Navigate to **📝 Data Entry** from sidebar
2. Fill in the transaction form:
   - **Date**: Select transaction date
   - **Product Name**: Choose from 8 agricultural products
   - **Quantity Received**: Enter purchase quantity
   - **Quantity Sold**: Enter sales quantity
   - **Cost Price**: Per unit cost
   - **Selling Price**: Per unit selling price
   - **Remarks**: Optional notes
3. Click **"✅ Add Transaction"**
4. View transaction preview before submission

### 2️⃣ Product Filtering (Separate Hotel Logic)
- Use the **🏷️ Product Filter** in the sidebar
- Select a product to view:
  - Only that product's transactions
  - Product-specific analytics
  - Isolated stock levels
- Select "All Products" for global view

### 3️⃣ Dashboard Analytics
- View **KPI Cards**:
  - 💰 Total Sales
  - 📈 Total Profit
  - 📦 Current Stock (product-specific)
  - 🔄 Transaction Count
- Analyze **Charts**:
  - Stock Depletion Over Time (line chart)
  - Profit Margin by Product (pie chart)
- Review **Product Performance Summary**

### 4️⃣ Ledger View
- View complete transaction history
- Export data as CSV
- See summary statistics:
  - Total Received
  - Total Sold
  - Total Revenue
  - Total Profit

---

## 🗂️ Data Structure

### Columns
| Column | Type | Description |
|--------|------|-------------|
| Date | Date | DD/MM/YYYY format |
| Product Name | Dropdown | 8 agricultural products |
| Quantity Received | Number | Purchase quantity |
| Quantity Sold | Number | Sales quantity |
| Stock Left | Auto-calc | Running balance |
| Cost Price | Number | Per unit cost |
| Selling Price | Number | Per unit price |
| Total Purchase | Auto-calc | Qty × Cost |
| Total Sales | Auto-calc | Qty × Selling |
| Profit | Auto-calc | (Selling - Cost) × Qty |
| Remarks | Text | Optional notes |

### Products
- Wheat
- Urea
- DAP
- Sarson
- Cow Feed
- Gandyal
- Him Cal
- Liv 52

---

## 🧠 Smart Logic

### Stock Calculation
```python
New Stock = Previous Stock + Quantity Received - Quantity Sold
```

### Calculations
- **Total Purchase** = Quantity Received × Cost Price
- **Total Sales** = Quantity Sold × Selling Price  
- **Profit** = (Selling Price - Cost Price) × Quantity Sold

### Product Isolation
- Each product maintains independent stock levels
- Filtering shows only selected product data
- No cross-contamination between products

---

## 💾 Data Storage

- **Format**: CSV (inventory_data.csv)
- **Location**: Same directory as app.py
- **Auto-save**: After each transaction
- **Export**: Download filtered data as CSV

---

## 🎨 Customization

### Adding Products
Edit the `PRODUCTS` list in `app.py`:
```python
PRODUCTS = ["Wheat", "Urea", "DAP", "Sarson", "Cow Feed", "Gandyal", "Him Cal", "Liv 52"]
```

### Changing Theme Colors
Modify CSS in the `st.markdown()` section:
```python
# Primary accent color
color: #00D9FF;  # Cyan
```

---

## 🛠️ Technical Stack

- **Frontend**: Streamlit 1.29.0
- **Data Processing**: Pandas 2.1.4
- **Visualizations**: Plotly 5.18.0
- **Database**: CSV (Excel compatible)
- **Style**: Custom CSS

---

## 📁 Project Structure

```
inventory-dashboard/
│
├── app.py                  # Main application
├── requirements.txt        # Python dependencies
├── inventory_data.csv      # Data storage (auto-created)
└── README.md              # This file
```

---

## 🚨 Troubleshooting

### App won't start
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Data not saving
- Check file permissions in the directory
- Ensure `inventory_data.csv` isn't open in Excel

### Charts not displaying
- Verify Plotly installation: `pip install plotly --upgrade`
- Clear browser cache and refresh

---

## 🔒 Best Practices

1. **Regular Backups**: Export CSV data regularly
2. **Data Validation**: Review transaction previews before submission
3. **Product Filter**: Use product filtering for accurate analysis
4. **Remarks**: Add notes for important transactions

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the usage guide
3. Verify data structure matches requirements

---

## ⚡ Performance

- **Optimized**: Handles thousands of transactions
- **Fast Loading**: CSV-based storage
- **Responsive**: Real-time calculations
- **Efficient**: Minimal resource usage

---

**Built with the "Elon Musk Professional" philosophy:**  
*Minimalist • Efficient • Robust • Highly Visual*

---

**Version**: 1.0.0  
**Last Updated**: December 2025
