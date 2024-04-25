import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data into a pandas DataFrame
world_population = pd.read_csv('world_population.csv')

# Display the first few rows of the DataFrame
print(world_population.head())

# Check for missing values
print(world_population.isnull().sum())

# Drop rows with missing values
world_population.dropna(inplace=True)

# Basic statistics
print(world_population.describe())

# Data Visualization
world_population['Average Population'] = world_population[['2022 Population', '2020 Population', '2015 Population',
                                                           '2010 Population', '2000 Population', '1990 Population',
                                                           '1980 Population', '1970 Population']].mean(axis=1)

# Plotting the graph of years against the average world population
plt.figure(figsize=(10, 6))
sns.lineplot(data=world_population, x='Average Population', y='World Population Percentage')
plt.title('Average World Population Over Percentage')
plt.xlabel('Average Population')
plt.ylabel('World Population Over Percentage')
plt.grid(True)
plt.show()