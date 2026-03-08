# part3_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\\Python\\archive\\netflix_titles.csv", encoding="latin-1")
df.drop_duplicates(inplace=True)
df.dropna(subset=['country', 'type', 'release_year', 'listed_in'], inplace=True)

# Top 10 Directors
top_directors = df['director'].value_counts().head(10)
print(top_directors)
plt.figure(figsize=(10,5))
sns.barplot(x=top_directors.values, y=top_directors.index, palette='cool')
plt.show()

# Genre Analysis (Top 10 genres)
all_genres = df['listed_in'].str.split(',').explode().str.strip()
top_genres = all_genres.value_counts().head(10)
print(top_genres)
plt.figure(figsize=(10,5))
sns.barplot(x=top_genres.values, y=top_genres.index, palette='Set2')
plt.show()

# Content Added by Release Year (Trend)
year_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(12,5))
sns.lineplot(x=year_counts.index, y=year_counts.values, marker='o')
plt.show()