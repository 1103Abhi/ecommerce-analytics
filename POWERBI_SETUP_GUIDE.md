# POWER BI DASHBOARD SETUP GUIDE
## E-Commerce Analytics Dashboard (6 Pages)

---

## 📋 OVERVIEW

This guide walks you through creating a **professional 6-page Power BI dashboard** using the provided CSV files.

**Time Required:** 2-3 hours  
**Difficulty:** Beginner to Intermediate  
**CSV Files Needed:**
- monthly_trends.csv
- customer_segments.csv
- product_performance.csv
- category_performance.csv
- geographic_analysis.csv
- ecommerce_data.csv (main dataset)

---

## 🎯 DASHBOARD STRUCTURE

| Page | Purpose | # Visuals | Target Audience |
|------|---------|----------|-----------------|
| **1. Executive Summary** | KPIs & overview | 6 visuals | C-Level executives |
| **2. Revenue Analysis** | Trends & products | 5 visuals | Finance team |
| **3. Customer Insights** | Segmentation & RFM | 5 visuals | Marketing team |
| **4. Product Performance** | Rankings & details | 5 visuals | Product managers |
| **5. Geographic Analysis** | Market breakdown | 5 visuals | Regional managers |
| **6. Trends & Patterns** | Growth & patterns | 4 visuals | Analysts |

**Total:** 30 visuals | 6 pages | 20+ KPIs

---

## 🚀 STEP 1: LOAD DATA INTO POWER BI (15 mins)

### Create New Report
1. Open **Power BI Desktop**
2. Click **Get Data** → **Text/CSV**
3. Navigate to `ecommerce_data.csv`
4. Load the data

### Import Additional CSVs
Repeat for each CSV:
- `monthly_trends.csv`
- `customer_segments.csv`
- `product_performance.csv`
- `category_performance.csv`
- `geographic_analysis.csv`

### Data Cleaning (Quick Check)
1. Go to **Power Query Editor**
2. Check **Data Type** for date columns:
   - Change to **Date** if needed
3. Remove any blank rows
4. Click **Close & Apply**

---

## 📊 PAGE 1: EXECUTIVE SUMMARY (20 mins)

**Purpose:** One-page overview for leadership

### Visual 1: Total Revenue (Card)
```
Field: Sum(Revenue)
Format: Currency ($)
Title: "Total Revenue"
Expected: $4,717,895
```

**How to Create:**
1. Insert → **Card**
2. Drag `Revenue` to Values
3. Format: Currency
4. Title: "Total Revenue"

### Visual 2: Total Orders (Card)
```
Field: Count(InvoiceID)
Format: Number
Title: "Total Orders"
Expected: 8,027
```

### Visual 3: Total Customers (Card)
```
Field: Count(CustomerID)
Format: Number
Title: "Total Customers"
Expected: 2,397
```

### Visual 4: Average Order Value (Card)
```
Field: Average(Revenue)
Format: Currency
Title: "Avg Order Value"
Expected: $587.75
```

### Visual 5: Repeat Customer Rate (Card)
```
Calculation: Customers with >1 order / Total customers × 100
Format: Percentage
Title: "Repeat Customer Rate"
Expected: 87%
```

**How to Calculate:**
1. Go to **Data** tab
2. New Measure: 
   ```
   Repeat Rate = 
   DIVIDE(
       CALCULATE(DISTINCTCOUNT(ecommerce_data[CustomerID]), 
                 FILTER(ecommerce_data, DISTINCTCOUNT(ecommerce_data[InvoiceID]) > 1)),
       DISTINCTCOUNT(ecommerce_data[CustomerID])
   ) * 100
   ```
3. Format as Percentage

### Visual 6: Status Filter
- Add **Slicer** for Status column
- Show only "Completed" by default
- Format as **Buttons**

### Layout Tips
- Arrange in 3 rows × 2 columns
- Use consistent card colors: **Light blue (#E7F3FF)**
- Font size: 24pt for numbers, 12pt for labels
- Add one main color: **#2E75B6 (Dark Blue)**

---

## 📈 PAGE 2: REVENUE ANALYSIS (25 mins)

### Visual 1: Monthly Revenue Trend (Line Chart)
```
X-axis: YearMonth (from monthly_trends.csv)
Y-axis: Sum(Revenue)
Title: "Monthly Revenue Trend (36 Months)"
Colors: Blue gradient
```

**Steps:**
1. Insert → **Line Chart**
2. Axis: `YearMonth` from monthly_trends
3. Values: `Sum(Revenue)`
4. Data Labels: ON
5. Add **Trend line** (Analytics → Trend line)

### Visual 2: Top 10 Products (Bar Chart - Horizontal)
```
Y-axis: ProductName
X-axis: Revenue
Sort: Revenue (Descending)
Title: "Top 10 Products by Revenue"
Colors: Green (#70AD47)
```

**Import from:** product_performance.csv (Top 10)

### Visual 3: Monthly Orders Count (Column Chart)
```
X-axis: YearMonth
Y-axis: Count(Orders)
Title: "Order Volume by Month"
Colors: Orange
```

**From:** monthly_trends.csv

### Visual 4: Revenue Distribution (Pie/Donut)
```
Values: Revenue
Legend: Category (from ecommerce_data)
Title: "Revenue by Category"
Colors: Distinct colors per category
```

### Visual 5: Top Products Table
```
Columns: ProductName | Revenue | Orders | % of Total
Sort: Revenue DESC
Format: Currency for Revenue, Number for Orders
```

### Page Filters
- Add **Date Slicer** (InvoiceDate)
- Add **Category Slicer** (dropdown)
- Add **Country Slicer** (buttons)

---

## 👥 PAGE 3: CUSTOMER INSIGHTS (25 mins)

### Visual 1: Customer Segment Distribution (Pie Chart)
```
Values: Count(CustomerID)
Legend: Segment (High Value, Medium Value, Low Value)
Title: "Customer Distribution by Segment"
Colors: 
  - High Value: #2E75B6 (Blue)
  - Medium Value: #F39C12 (Orange)
  - Low Value: #E74C3C (Red)
Data Labels: % of Total
```

**Data From:** customer_segments.csv

### Visual 2: Revenue by Segment (Bar Chart)
```
X-axis: Segment
Y-axis: Sum(Monetary)
Title: "Revenue Contribution by Segment"
Colors: Match segment colors above
```

### Visual 3: Top 20 Customers (Table)
```
Columns: CustomerID | Frequency | Monetary | Last_Purchase | Segment
Sort: Monetary DESC
Format: Currency for Monetary, Date for Last_Purchase
```

### Visual 4: RFM Scatter Plot (Scatter Chart - Advanced)
```
X-axis: Recency (Days)
Y-axis: Monetary (Value)
Size: Frequency (Bubble size)
Legend: Segment (colors)
Title: "RFM Analysis - Customer Positioning"
```

### Visual 5: Segment Summary Cards
Create 3 cards stacked vertically:
- High Value customers count
- Medium Value customers count  
- Low Value customers count

### Visual 6: Customer Loyalty Gauge
```
Value: Repeat Rate (%)
Target: 85%
Title: "Repeat Purchase Rate"
Color: Green if >85%, Yellow if 75-85%, Red if <75%
```

---

## 🛍️ PAGE 4: PRODUCT PERFORMANCE (25 mins)

### Visual 1: Top 10 Products (Horizontal Bar)
```
Data From: product_performance.csv
Y-axis: ProductName
X-axis: Revenue
Title: "Top 10 Products by Revenue"
Colors: Purple (#9B59B6)
Data Labels: Show revenue values
```

### Visual 2: Product Details Table
```
Columns: ProductName | Category | TotalQuantity | Revenue | OrderCount
Sort: Revenue DESC
Format: 
  - Revenue: Currency
  - OrderCount: Whole number with 000 separator
Conditional Formatting: Revenue column (gradient)
```

### Visual 3: Category Performance (Stacked Bar)
```
X-axis: Category
Y-axis: Revenue
Color by: Product (Top 5 per category)
Title: "Top Products by Category"
```

### Visual 4: Product Count by Category (Column)
```
X-axis: Category
Y-axis: Count(ProductName)
Title: "Number of Products by Category"
Colors: Teal
```

### Visual 5: Best Performer KPI Card
```
Calculation: Product with highest revenue
Value: Laptop
Revenue: $1,182,000
Title: "Best Performing Product"
```

### Page Filters
- Category slicer
- Product name slicer (if dataset supports)

---

## 🌍 PAGE 5: GEOGRAPHIC ANALYSIS (20 mins)

### Visual 1: Revenue by Country (Map - if available)
```
Location: Country
Values: Sum(Revenue)
Title: "Geographic Market Share"
Colors: Blue intensity (darker = higher revenue)
```

**Steps:**
1. Insert → **Map**
2. Location: `Country` from geographic_analysis
3. Bubble size: `Sum(Revenue)`
4. Zoom in on Europe & USA

### Visual 2: Top Countries Bar Chart
```
Y-axis: Country (Top 10)
X-axis: Revenue
Title: "Revenue by Country"
Colors: Orange (#E67E22)
Sort: Revenue DESC
```

### Visual 3: Geographic Metrics Table
```
Columns: Country | Revenue | Orders | Customers | Market_Share
Sort: Revenue DESC
Format: 
  - Revenue: Currency
  - Market_Share: Percentage
Conditional: Market share gradient
```

### Visual 4: Market Share Breakdown (Pie)
```
Values: Revenue
Legend: Country (Top 6)
Title: "Market Share Distribution"
Colors: 6 distinct colors
```

### Visual 5: Customer Distribution (Column)
```
X-axis: Country
Y-axis: Count(Customers)
Title: "Active Customers by Country"
Colors: Green
```

---

## 📊 PAGE 6: TRENDS & PATTERNS (20 mins)

### Visual 1: Monthly Order Count Trend (Line)
```
X-axis: YearMonth
Y-axis: Count(Orders)
Title: "Order Volume Trend"
Colors: Blue
Add trend line
```

### Visual 2: Growth Rate Gauge
```
Calculation: Month-over-month growth
Value: Current month vs. Previous month
Format: Percentage
Target: 5% growth
Status: Green if above target
```

**DAX Calculation:**
```
MoM Growth % = 
VAR CurrentMonth = MAX(monthly_trends[YearMonth])
VAR PreviousMonth = CALCULATE(SUM(monthly_trends[Revenue]), 
                               monthly_trends[YearMonth] = 
                               DATEADD(EOMONTH(CurrentMonth, -1), 0, DAY))
RETURN
DIVIDE(
    SUM(monthly_trends[Revenue]) - PreviousMonth,
    PreviousMonth
) * 100
```

### Visual 3: Year-over-Year Comparison (Column)
```
X-axis: Month (1-12)
Y-axis: Revenue
Series: Year
Title: "YoY Revenue Comparison"
Colors: Different colors per year
```

### Visual 4: Top Trends Summary (Text Cards)
Create text cards with:
- "Highest revenue month: May 2024 - $156,115"
- "Lowest revenue month: Sept 2024 - $101,015"
- "Avg monthly revenue: $196,579"
- "Customer growth rate: +15% YoY"

### Visual 5: Seasonality Heatmap (Table)
```
Rows: Month
Columns: Year
Values: Revenue
Conditional formatting: Color gradient
Title: "Monthly Revenue Heatmap"
```

### Filter Page
- Date range slicer (Recency filter)
- Segment slicer
- Category slicer
- Status filter (Completed only)

---

## 🎨 FORMATTING BEST PRACTICES

### Colors
- **Primary:** #2E75B6 (Dark Blue)
- **Accent:** #F39C12 (Orange)
- **Success:** #70AD47 (Green)
- **Alert:** #E74C3C (Red)
- **Neutral:** #95A5A6 (Gray)

### Number Formatting
```
Currency: $#,##0
Decimal: #,##0.0
Percentage: 0.0%
Thousands: #,##0,
Million: #,##0,, "M"
```

### Font Guidelines
- **Title:** Bold, 14pt, #2E75B6
- **Subtitle:** Normal, 11pt, #595959
- **Labels:** Normal, 10pt, #595959
- **Values:** Bold, 12pt, #000000

### Background
- Light: #F5F5F5 or white
- Dark theme: Dark gray #2F2F2F

### Card Design
- Border: Thin, light gray
- Shadow: Subtle drop shadow
- Rounded corners: 4px

---

## 🔧 INTERACTIVE ELEMENTS

### Slicers (Filters) Setup

**Date Range Slicer:**
1. Insert → **Slicer**
2. Field: `InvoiceDate`
3. Type: **Between**
4. Style: Modern
5. Placement: Top of page

**Segment Slicer:**
1. Insert → **Slicer**
2. Field: `Segment`
3. Type: **Buttons**
4. Selection: Single select
5. Size: Small

**Category Slicer:**
1. Insert → **Slicer**
2. Field: `Category`
3. Type: **Dropdown**
4. Default: "All"

### Cross-Filter Setup
All visuals should filter based on slicers:
1. Select visual
2. Format → **Interaction**
3. Slicer → Filter (checkmark)

---

## 💾 SAVING & EXPORTING

### Save File
1. **File** → **Save**
2. Filename: `ecommerce_analytics_dashboard.pbix`
3. Location: Project folder

### Export Dashboard
1. File → **Export** → **PDF**
2. Export each page separately
3. Save to `visualizations/` folder

### Export Data
1. Right-click visual → **Export data**
2. Format: CSV or Excel
3. Use for stakeholder reports

---

## 📱 MOBILE OPTIMIZATION (Optional)

### Create Mobile View
1. View → **Mobile Layout**
2. Adjust for narrow screen (380px)
3. Stack visuals vertically
4. Enlarge touch targets
5. Simplify number of visuals

### Recommended for Mobile
- KPI cards (large)
- Top products (simple bar)
- Segment distribution (pie)
- Trend line (scrollable)

---

## ✅ QUALITY CHECKLIST

Before sharing dashboard:

- [ ] All visuals have titles
- [ ] All numbers are formatted correctly
- [ ] Slicers work across all pages
- [ ] Colors are consistent
- [ ] Data labels are visible
- [ ] No #ERROR or missing values
- [ ] Report is saved
- [ ] Performance is acceptable (<3 sec load)
- [ ] Mobile view is responsive
- [ ] Exported PDFs look professional

---

## 🚀 SHARING & PUBLISHING

### Share on Power BI Service (Free)
1. Publish → Power BI Service
2. Share with colleagues
3. Create shareable link

### Embed in Website (Premium)
1. Publish report
2. Get embed code
3. Add to website/portfolio

### Export for Portfolio
1. Export as PDF (all pages)
2. Screenshot key visuals
3. Include in GitHub repo

---

## 🎓 ADVANCED FEATURES (Optional)

### Add Tooltips
1. Select visual
2. Format → **Tooltip page**
3. Create custom tooltip page
4. Add relevant cards

### Add Bookmarks
1. View → **Bookmarks**
2. Create bookmark for each scenario
3. Use for guided analytics

### Add Buttons
1. Insert → **Button**
2. Link to other pages
3. Create navigation dashboard

### Add R/Python Visuals
1. Insert → **R/Python visual**
2. Add predictive model
3. Show forecasts

---

## 📊 EXPECTED RESULTS

Your completed dashboard should show:

| KPI | Expected Value |
|-----|-----------------|
| Total Revenue | $4,717,895 |
| Total Orders | 8,027 |
| Avg Order Value | $587.75 |
| Repeat Rate | 87% |
| Top Product | Laptop |
| Top Country | Germany (18.3%) |
| High-Value Customers | 290 (12.1%) |
| Electronics Revenue | $2,896,750 (61.4%) |

---

## 🎬 TIME BREAKDOWN

| Task | Time | Difficulty |
|------|------|-----------|
| Load & clean data | 15 min | Easy |
| Page 1 - Executive | 20 min | Easy |
| Page 2 - Revenue | 25 min | Easy |
| Page 3 - Customer | 25 min | Intermediate |
| Page 4 - Product | 25 min | Easy |
| Page 5 - Geographic | 20 min | Easy |
| Page 6 - Trends | 20 min | Intermediate |
| Formatting & polish | 30 min | Easy |
| **TOTAL** | **3 hours** | **Beginner-Intermediate** |

---

## 🆘 TROUBLESHOOTING

### Issue: Columns not showing in Power BI
**Solution:**
1. Go to Data view
2. Check column names match CSV headers
3. Right-click column → Include in report

### Issue: Dates showing as numbers
**Solution:**
1. Right-click date column
2. Change Type → Date
3. Format → Date format

### Issue: Slicer not filtering visuals
**Solution:**
1. Select slicer
2. Format → Interaction
3. Check "Filter" for target visuals
4. Click Apply

### Issue: Performance is slow
**Solution:**
1. Reduce data rows (filter data)
2. Summarize before loading
3. Use aggregated CSV files
4. Disable unnecessary visuals

---

## 💡 PRO TIPS

1. **Use variables for consistency** - Define once, use multiple times
2. **Create calculated columns strategically** - Don't overdo it
3. **Optimize visuals** - Less is more
4. **Document your DAX** - Future you will thank you
5. **Test on different devices** - Desktop, tablet, mobile
6. **Get feedback** - Share early and iterate
7. **Create drill-through pages** - Deep dive capabilities
8. **Use row-level security** - Hide sensitive data

---

## 📚 RESOURCES

- Power BI Training: https://learn.microsoft.com/power-bi/
- DAX Reference: https://dax.guide/
- Best Practices: https://www.sqlbi.com/
- Dashboard Design: https://www.interaction-design.org/literature/topics/data-visualization

---

**Your dashboard is ready! You've got this! 🎉**

After completing:
1. Save as .pbix file
2. Export to PDF
3. Take screenshots
4. Add to GitHub
5. Share in interviews!

---

**Good luck! This dashboard is portfolio-quality and interview-ready! 🚀**
