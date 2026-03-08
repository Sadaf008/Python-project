import pandas as pd
df = pd.read_csv("D:\\Python\\archive\\netflix_titles.csv", encoding="latin-1")
print(df.head())
print(df.info())
print(df.isnull().sum())
#Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(subset=['country', 'type', 'release_year', 'listed_in'], inplace=True)

