import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv("sales_data.csv")
    print("Dataset loaded successfully.\n")
except FileNotFoundError:
    print("Error: sales_data.csv not found.")
    exit()

print("FIRST 5 ROWS OF DATASET")
print(df.head())
print()
print("MISSING VALUES")
print(df.isnull().sum())
print()
df = df.dropna()
df = df.drop_duplicates()
print("Dataset cleaned successfully.\n")

if "Revenue" not in df.columns:
    df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]
print("SUMMARY STATISTICS")
print(df.describe())
print()
print("SALES RECORDS WITH REVENUE GREATER THAN 10000")
high_sales = df[df["Revenue"] > 10000]
print(high_sales)
print()
print("TOTAL REVENUE BY REGION")
revenue_by_region = df.groupby("Region")["Revenue"].sum()
print(revenue_by_region)
print()

print("TOTAL REVENUE BY PRODUCT")
revenue_by_product = df.groupby("Product")["Revenue"].sum()
print(revenue_by_product)
print()

best_region = revenue_by_region.idxmax()
best_region_revenue = revenue_by_region.max()
best_product = revenue_by_product.idxmax()
best_product_revenue = revenue_by_product.max()

print("MEANINGFUL INSIGHTS")
print(f"1. Region with highest revenue: {best_region} (₹{best_region_revenue:,.2f})")
print(f"2. Product with highest revenue: {best_product} (₹{best_product_revenue:,.2f})")
print(f"3. Total revenue generated: ₹{df['Revenue'].sum():,.2f}")
print(f"4. Average revenue per sale: ₹{df['Revenue'].mean():,.2f}")
print()
print("Generating revenue by region chart...")

revenue_by_region.plot(kind="bar", figsize=(8, 5))
plt.title("Total Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_by_region_chart.png")
plt.show()
df.to_csv("cleaned_sales_data.csv", index=False)

print("Cleaned dataset saved as cleaned_sales_data.csv")
print("Chart saved as revenue_by_region_chart.png")
print("Analysis completed successfully.")