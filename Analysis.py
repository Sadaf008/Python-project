import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("D:\\Python\\archive\\netflix_titles.csv", encoding="latin-1")
df.drop_duplicates(inplace=True)
df.dropna(subset=['country', 'type', 'release_year', 'listed_in'], inplace=True)

# Movies vs TV Shows
type_count = df['type'].value_counts()
print(type_count)

# Plot
plt.figure(figsize=(6,4))
sns.barplot(x=type_count.index, y=type_count.values, palette='viridis')
plt.show()

# Top 10 Countries producing content
top_countries = df['country'].value_counts().head(10)
print(top_countries)
plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.index, y=top_countries.values, palette='magma')
plt.xticks(rotation=45)
plt.show()
