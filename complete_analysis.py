"""
E-COMMERCE ANALYTICS - COMPLETE ANALYSIS
Real data analysis with RFM segmentation, trends, and visualizations
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)

print("=" * 60)
print("E-COMMERCE ANALYTICS - COMPLETE ANALYSIS")
print("=" * 60)

# ============================================
#  LOADING AND CLEANING DATA
# ============================================
print("\n1️1  LOADING DATA...")
df = pd.read_csv('ecommerce_data.csv')

# Convert date
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Filter for completed orders only
df_completed = df[df['Status'] == 'Completed'].copy()

print(f"✓ Total records: {len(df):,}")
print(f"✓ Completed orders: {len(df_completed):,}")
print(f"✓ Cancelled orders: {len(df) - len(df_completed):,}")
print(f"✓ Date range: {df['InvoiceDate'].min().date()} to {df['InvoiceDate'].max().date()}")

# ============================================
#  CALCULATE KEY BUSINESS METRICS
# ============================================
print("\n2️⃣  CALCULATING KEY METRICS...")

total_revenue = df_completed['Revenue'].sum()
total_orders = df_completed['InvoiceID'].nunique()
total_customers = df_completed['CustomerID'].nunique()
avg_order_value = df_completed.groupby('InvoiceID')['Revenue'].sum().mean()
total_items = df_completed['Quantity'].sum()

print(f"\n📊 KEY METRICS:")
print(f"   Total Revenue: ${total_revenue:,.2f}")
print(f"   Total Orders: {total_orders:,}")
print(f"   Total Customers: {total_customers:,}")
print(f"   Avg Order Value: ${avg_order_value:,.2f}")
print(f"   Total Items Sold: {total_items:,}")

# ============================================
#  PRODUCT ANALYSIS
# ============================================
print("\n3️⃣  TOP 10 PRODUCTS BY REVENUE...")

product_analysis = df_completed.groupby('ProductName').agg({
    'Quantity': 'sum',
    'Revenue': 'sum',
    'InvoiceID': 'count'
}).reset_index()
product_analysis.columns = ['ProductName', 'TotalQuantity', 'Revenue', 'OrderCount']
product_analysis = product_analysis.sort_values('Revenue', ascending=False)

print(f"\n{'Product':<20} {'Quantity':>10} {'Revenue':>15} {'Orders':>10}")
print("-" * 60)
for idx, row in product_analysis.head(10).iterrows():
    print(f"{row['ProductName']:<20} {row['TotalQuantity']:>10,} ${row['Revenue']:>14,.0f} {row['OrderCount']:>10,}")

# ============================================
#  CATEGORY ANALYSIS
# ============================================
print("\n4️⃣  CATEGORY PERFORMANCE...")

category_analysis = df_completed.groupby('Category').agg({
    'Revenue': 'sum',
    'InvoiceID': 'count',
    'Quantity': 'sum',
    'ProductName': 'nunique'
}).reset_index()
category_analysis.columns = ['Category', 'Revenue', 'Orders', 'Quantity', 'NumProducts']
category_analysis = category_analysis.sort_values('Revenue', ascending=False)

print(f"\n{'Category':<15} {'Revenue':>15} {'Orders':>10} {'Qty':>10} {'Products':>10}")
print("-" * 60)
for idx, row in category_analysis.iterrows():
    print(f"{row['Category']:<15} ${row['Revenue']:>14,.0f} {row['Orders']:>10,} {row['Quantity']:>10,} {row['NumProducts']:>10}")

# ============================================
#  MONTHLY TRENDS
# ============================================
print("\n5️⃣  MONTHLY REVENUE TRENDS...")

df_completed['YearMonth'] = df_completed['InvoiceDate'].dt.to_period('M')
monthly = df_completed.groupby('YearMonth').agg({
    'Revenue': 'sum',
    'InvoiceID': 'count',
    'CustomerID': 'nunique'
}).reset_index()
monthly.columns = ['YearMonth', 'Revenue', 'Orders', 'Customers']
monthly['YearMonth'] = monthly['YearMonth'].astype(str)

print(f"\n{'Month':<12} {'Revenue':>15} {'Orders':>10} {'Customers':>12}")
print("-" * 50)
for idx, row in monthly.tail(12).iterrows():
    print(f"{row['YearMonth']:<12} ${row['Revenue']:>14,.0f} {row['Orders']:>10,} {row['Customers']:>12,}")

# ============================================
#  RFM ANALYSIS (Customer Segmentation)
# ============================================
print("\n6️⃣  RFM CUSTOMER SEGMENTATION...")

today = df_completed['InvoiceDate'].max()
rfm = df_completed.groupby('CustomerID').agg({
    'InvoiceID': 'count',
    'InvoiceDate': 'max',
    'Revenue': 'sum'
}).reset_index()
rfm.columns = ['CustomerID', 'Frequency', 'LastPurchase', 'Monetary']

rfm['Recency'] = (today - rfm['LastPurchase']).dt.days

# Segment customers
def segment_customer(row):
    if row['Frequency'] >= 5 and row['Monetary'] >= rfm['Monetary'].quantile(0.75):
        return 'High Value'
    elif row['Frequency'] >= 3 or row['Monetary'] >= rfm['Monetary'].quantile(0.50):
        return 'Medium Value'
    else:
        return 'Low Value'

rfm['Segment'] = rfm.apply(segment_customer, axis=1)

print(f"\n{'Segment':<15} {'Count':>10} {'% Total':>12} {'Avg Spent':>15}")
print("-" * 52)
segment_stats = rfm['Segment'].value_counts()
for segment in ['High Value', 'Medium Value', 'Low Value']:
    count = segment_stats.get(segment, 0)
    pct = (count / len(rfm)) * 100
    avg_spent = rfm[rfm['Segment'] == segment]['Monetary'].mean()
    print(f"{segment:<15} {count:>10,} {pct:>11.1f}% ${avg_spent:>14,.0f}")

# Revenue by segment
print(f"\n{'Segment':<15} {'Total Revenue':>20} {'% of Total Revenue':>20}")
print("-" * 55)
for segment in ['High Value', 'Medium Value', 'Low Value']:
    seg_revenue = rfm[rfm['Segment'] == segment]['Monetary'].sum()
    pct_revenue = (seg_revenue / rfm['Monetary'].sum()) * 100
    print(f"{segment:<15} ${seg_revenue:>19,.0f} {pct_revenue:>19.1f}%")

# ============================================
#  GEOGRAPHIC ANALYSIS
# ============================================
print("\n7️⃣  GEOGRAPHIC PERFORMANCE...")

geo = df_completed.groupby('Country').agg({
    'Revenue': 'sum',
    'InvoiceID': 'count',
    'CustomerID': 'nunique'
}).reset_index()
geo.columns = ['Country', 'Revenue', 'Orders', 'Customers']
geo = geo.sort_values('Revenue', ascending=False)

print(f"\n{'Country':<20} {'Revenue':>15} {'Orders':>10} {'Customers':>12}")
print("-" * 60)
for idx, row in geo.head(10).iterrows():
    print(f"{row['Country']:<20} ${row['Revenue']:>14,.0f} {row['Orders']:>10,} {row['Customers']:>12,}")

# ============================================
#  CUSTOMER REPEAT ANALYSIS
# ============================================
print("\n8️⃣  CUSTOMER REPEAT PURCHASE ANALYSIS...")

customer_orders = df_completed.groupby('CustomerID')['InvoiceID'].count()
repeat_customers = (customer_orders > 1).sum()
repeat_rate = (repeat_customers / len(customer_orders)) * 100

print(f"\nOne-time customers: {(customer_orders == 1).sum():,} ({(customer_orders == 1).sum()/len(customer_orders)*100:.1f}%)")
print(f"Repeat customers: {repeat_customers:,} ({repeat_rate:.1f}%)")
print(f"Avg purchases per customer: {customer_orders.mean():.1f}")

# ============================================
#  CREATE VISUALIZATIONS
# ============================================
print("\n9️⃣  CREATING VISUALIZATIONS...")

fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

# Plot 1: Monthly Revenue Trend
ax1 = fig.add_subplot(gs[0, :])
colors = ['#2E75B6' if i % 2 == 0 else '#00B4D8' for i in range(len(monthly))]
ax1.bar(range(len(monthly)), monthly['Revenue'], color=colors, alpha=0.8)
ax1.set_title('Monthly Revenue Trend (2022-2024)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Month', fontsize=11)
ax1.set_ylabel('Revenue ($)', fontsize=11)
ax1.set_xticks(range(0, len(monthly), 3))
ax1.set_xticklabels(monthly['YearMonth'][::3], rotation=45)
ax1.grid(True, alpha=0.3, axis='y')
for i, v in enumerate(monthly['Revenue']):
    if i % 3 == 0:
        ax1.text(i, v + 10000, f'${v/1000:.0f}K', ha='center', fontsize=8)

# Plot 2: Top 10 Products
ax2 = fig.add_subplot(gs[1, 0])
top_products = product_analysis.head(10)
ax2.barh(range(len(top_products)), top_products['Revenue'], color='#70AD47', alpha=0.8)
ax2.set_yticks(range(len(top_products)))
ax2.set_yticklabels(top_products['ProductName'], fontsize=10)
ax2.set_title('Top 10 Products by Revenue', fontsize=12, fontweight='bold')
ax2.set_xlabel('Revenue ($)', fontsize=10)
ax2.invert_yaxis()
ax2.grid(True, alpha=0.3, axis='x')
for i, v in enumerate(top_products['Revenue']):
    ax2.text(v + 5000, i, f'${v/1000:.0f}K', va='center', fontsize=9)

# Plot 3: Customer Segments
ax3 = fig.add_subplot(gs[1, 1])
segment_counts = rfm['Segment'].value_counts()
colors_pie = ['#2E75B6', '#F39C12', '#E74C3C']
wedges, texts, autotexts = ax3.pie(segment_counts.values, labels=segment_counts.index, 
                                     autopct='%1.1f%%', colors=colors_pie, startangle=90,
                                     textprops={'fontsize': 10})
ax3.set_title('Customer Segment Distribution\n(RFM Analysis)', fontsize=12, fontweight='bold')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# Plot 4: Category Performance
ax4 = fig.add_subplot(gs[2, 0])
ax4.bar(category_analysis['Category'], category_analysis['Revenue'], color='#9B59B6', alpha=0.8)
ax4.set_title('Revenue by Category', fontsize=12, fontweight='bold')
ax4.set_xlabel('Category', fontsize=10)
ax4.set_ylabel('Revenue ($)', fontsize=10)
ax4.tick_params(axis='x', rotation=45)
ax4.grid(True, alpha=0.3, axis='y')
for i, v in enumerate(category_analysis['Revenue']):
    ax4.text(i, v + 20000, f'${v/1000:.0f}K', ha='center', fontsize=9)

# Plot 5: Top Countries
ax5 = fig.add_subplot(gs[2, 1])
top_countries = geo.head(8)
ax5.barh(range(len(top_countries)), top_countries['Revenue'], color='#E67E22', alpha=0.8)
ax5.set_yticks(range(len(top_countries)))
ax5.set_yticklabels(top_countries['Country'], fontsize=10)
ax5.set_title('Top 8 Countries by Revenue', fontsize=12, fontweight='bold')
ax5.set_xlabel('Revenue ($)', fontsize=10)
ax5.invert_yaxis()
ax5.grid(True, alpha=0.3, axis='x')
for i, v in enumerate(top_countries['Revenue']):
    ax5.text(v + 5000, i, f'${v/1000:.0f}K', va='center', fontsize=9)

plt.suptitle('E-Commerce Analytics Dashboard - Complete Overview', 
             fontsize=16, fontweight='bold', y=0.995)
plt.savefig('ecommerce_analytics_dashboard.png', dpi=300, bbox_inches='tight')
print("✓ Saved: ecommerce_analytics_dashboard.png")

# ============================================
# STEP 10: EXPORT DATA FOR POWER BI
# ============================================
print("\n🔟 EXPORTING DATA FOR POWER BI...")

# Monthly trends
monthly.to_csv('monthly_trends.csv', index=False)
print("✓ Saved: monthly_trends.csv")

# RFM data
rfm_export = rfm.copy()
rfm_export['LastPurchase'] = rfm_export['LastPurchase'].dt.strftime('%Y-%m-%d')
rfm_export.to_csv('customer_segments.csv', index=False)
print("✓ Saved: customer_segments.csv")

# Product performance
product_analysis.to_csv('product_performance.csv', index=False)
print("✓ Saved: product_performance.csv")

# Category performance
category_analysis.to_csv('category_performance.csv', index=False)
print("✓ Saved: category_performance.csv")

# Geographic data
geo.to_csv('geographic_analysis.csv', index=False)
print("✓ Saved: geographic_analysis.csv")

# ============================================
#  SUMMARY & INSIGHTS
# ============================================
print("\n" + "=" * 60)
print("KEY INSIGHTS & FINDINGS")
print("=" * 60)

top_product = product_analysis.iloc[0]
top_category = category_analysis.iloc[0]
high_value_revenue = rfm[rfm['Segment'] == 'High Value']['Monetary'].sum()
high_value_pct = (high_value_revenue / rfm['Monetary'].sum()) * 100

print(f"\n💡 STRATEGIC INSIGHTS:")
print(f"\n1. REVENUE CONCENTRATION")
print(f"   • Top 5 products generate: ${product_analysis.head(5)['Revenue'].sum():,.0f}")
print(f"   • % of total: {(product_analysis.head(5)['Revenue'].sum() / total_revenue) * 100:.1f}%")

print(f"\n2. CUSTOMER VALUE DISTRIBUTION")
print(f"   • High-value customers ({(rfm['Segment']=='High Value').sum()} customers):")
print(f"     - Generate: ${high_value_revenue:,.0f} ({high_value_pct:.1f}% of revenue)")
print(f"     - Avg order value: ${rfm[rfm['Segment']=='High Value']['Monetary'].mean():,.0f}")

print(f"\n3. PRODUCT PERFORMANCE")
print(f"   • Best performer: {top_product['ProductName']}")
print(f"   • Revenue: ${top_product['Revenue']:,.0f}")
print(f"   • Orders: {top_product['OrderCount']:,.0f}")

print(f"\n4. CATEGORY INSIGHTS")
print(f"   • Leading category: {top_category['Category']}")
print(f"   • Revenue: ${top_category['Revenue']:,.0f} ({(top_category['Revenue']/total_revenue)*100:.1f}%)")

print(f"\n5. GEOGRAPHIC REACH")
print(f"   • Countries served: {len(geo)}")
print(f"   • Top market: {geo.iloc[0]['Country']}")
print(f"   • Market share: {(geo.iloc[0]['Revenue']/total_revenue)*100:.1f}%")

print(f"\n6. CUSTOMER LOYALTY")
print(f"   • Repeat purchase rate: {repeat_rate:.1f}%")
print(f"   • Avg customer orders: {customer_orders.mean():.1f}")

print(f"\n7. ORDER PATTERNS")
print(f"   • Avg order value: ${avg_order_value:,.2f}")
print(f"   • Total items sold: {total_items:,}")
print(f"   • Avg items per order: {total_items / total_orders:.1f}")

print("\n" + "=" * 60)
print("✅ ANALYSIS COMPLETE!")
print("=" * 60)
print(f"\nOutput files created:")
print(f"  • ecommerce_analytics_dashboard.png (visualization)")
print(f"  • monthly_trends.csv (for Power BI)")
print(f"  • customer_segments.csv (for Power BI)")
print(f"  • product_performance.csv (for Power BI)")
print(f"  • category_performance.csv (for Power BI)")
print(f"  • geographic_analysis.csv (for Power BI)")
print(f"\nReady for Power BI import! 📊")
