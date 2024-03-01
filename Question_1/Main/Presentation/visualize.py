from monthly_expenses_generator import generate_monthly_expenses
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime



df = generate_monthly_expenses()
print(df)


# Convert birth_date and transaction_date to datetime
df['birth_date'] = pd.to_datetime(df['birth_date'])
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# 1. Total Expenses by Category
total_expenses_category = df.groupby('category')['amount'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='category', y='amount', data=total_expenses_category)
plt.title('Total Expenses by Category')
plt.xlabel('Category')
plt.ylabel('Total Expenses')
plt.show()

# 2. Most Expensive Subcategories
most_expensive_subcategories = df.groupby('subcategory')['amount'].sum().nlargest(5).reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='amount', y='subcategory', data=most_expensive_subcategories)
plt.title('Top 5 Most Expensive Subcategories')
plt.xlabel('Total Expenses')
plt.ylabel('Subcategory')
plt.show()

# 3. Calculate transaction frequency for each part of the month

plt.figure(figsize=(10, 6))
early_month = df[df['transaction_date'].dt.day <= 10]['transaction_date'].dt.month.value_counts().sort_index()
mid_month = df[(df['transaction_date'].dt.day > 10) & (df['transaction_date'].dt.day <= 20)]['transaction_date'].dt.month.value_counts().sort_index()
late_month = df[df['transaction_date'].dt.day > 20]['transaction_date'].dt.month.value_counts().sort_index()
width = 0.25
plt.bar(early_month.index - width, early_month, width, label='Early Month')
plt.bar(mid_month.index, mid_month, width, label='Mid Month')
plt.bar(late_month.index + width, late_month, width, label='Late Month')
plt.title('Transaction Frequency Over Time (Divided by Month Parts)')
plt.xlabel('Month')
plt.ylabel('Frequency')
plt.xticks(early_month.index)
plt.legend()
plt.show()

# 4. Average Transaction Amount by Category
average_transaction_category = df.groupby('category')['amount'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='category', y='amount', data=average_transaction_category)
plt.title('Average Transaction Amount by Category')
plt.xlabel('Category')
plt.ylabel('Average Amount')
plt.show()

# 5. Distribution of Transaction Amounts
plt.figure(figsize=(10, 6))
sns.histplot(df['amount'], bins=20, kde=True)
plt.title('Distribution of Transaction Amounts')
plt.xlabel('Amount')
plt.ylabel('Frequency')
plt.show()

# 6. Customer Age Distribution
df['age'] = (datetime.now() - df['birth_date']).astype('<m8[Y]')
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], bins=20, kde=True)
plt.title('Customer Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 7. Most Visited Locations
most_visited_locations = df['location'].value_counts().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='index', y='location', data=most_visited_locations)
plt.title('Most Visited Locations')
plt.xlabel('Location')
plt.ylabel('Frequency')
plt.show()

# 8. Transaction Amounts vs. Birth Year
plt.figure(figsize=(10, 6))
sns.scatterplot(x='birth_date', y='amount', data=df)
plt.title('Transaction Amounts vs. Birth Year')
plt.xlabel('Birth Year')
plt.ylabel('Amount')
plt.show()

# 9. Transaction Amounts by Location
plt.figure(figsize=(10, 6))
sns.boxplot(x='location', y='amount', data=df)
plt.title('Transaction Amounts by Location')
plt.xlabel('Location')
plt.ylabel('Amount')
plt.show()

# 10. Transaction Patterns
plt.figure(figsize=(10, 6))
sns.countplot(x='transaction_date', hue='category', data=df)
plt.title('Transaction Patterns')
plt.xlabel('Transaction Date')
plt.ylabel('Frequency')
plt.show()
