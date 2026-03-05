import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:\\Python\\train.csv')
order_mean = df.groupby('Order ID')['Sales'].mean()
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
subcategory_median = df.groupby('Sub-Category')['Sales'].median()
print(order_mean)
print(region_sales)
print(category_sales)
print(df['Row ID'].max())
print(df['Row ID'].min())
print(df.groupby('Category')['Row ID'].count())
print(subcategory_median)
top_region = region_sales.idxmax()
top_category = category_sales.idxmax()
print(top_region)
print(top_category)