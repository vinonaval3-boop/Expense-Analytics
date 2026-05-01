import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv('data/expenses.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Analysis
total = df['Amount'].sum()
print("Total Expense:", total)

df['Month'] = df['Date'].dt.month
monthly = df.groupby('Month')['Amount'].sum()
print("\nMonthly Expense:\n", monthly)

category = df.groupby('Category')['Amount'].sum()
print("\nCategory Expense:\n", category)

# Charts
os.makedirs('output', exist_ok=True)

monthly.plot(kind='line', title='Monthly Expense Trend', marker='o', color='blue')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.tight_layout()
plt.savefig('output/monthly.png')
plt.close()

category.plot(kind='bar', title='Category-wise Expense', color='orange')
plt.xlabel('Category')
plt.ylabel('Amount')
plt.tight_layout()
plt.savefig('output/category.png')
plt.close()

# Insights
print("\nTop Spending Category:", category.idxmax())
print("Lowest Spending Category:", category.idxmin())
print("\nCharts saved to output/ folder!")