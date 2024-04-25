import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
df = pd.read_csv('dataset.csv')

#print(df.head())
print(df.describe())
print(df.columns)
df.columns = df.columns.str.strip()

print(df.isnull().sum())

df.dropna(subset=['Planet Density (g/cm**3)'], inplace=True)

plt.figure(figsize=(10, 6))



numeric_df = df.select_dtypes(include=np.number)
#heatmap
plt.figure(figsize=(10,6))
sns.heatmap(numeric_df.corr(), cmap='coolwarm')
plt.title('Correlation HeatMap')
plt.show()
