import pandas as pd
data = pd.read_csv('weatherHistory.csv')
print("Shape:", data.shape)
print("\nFeatures:", data.columns)

X=data[data.columns[2:5]]
Y=data[data.columns[-1]]

print("\nFeature matrix:", X.head())
print("\nResponse vector:",Y.head())