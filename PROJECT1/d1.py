import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:\\Python\\train.csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.describe())
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)