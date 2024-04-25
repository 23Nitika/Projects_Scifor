from sklearn.datasets import load_iris
iris = load_iris()

X = iris.data
Y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names

print("Feature names: ", feature_names)
print("Target names: ", target_names)

print("\nType of X is:", type(X))
print("\nFirst 5 rows of X:\n", X[:5])