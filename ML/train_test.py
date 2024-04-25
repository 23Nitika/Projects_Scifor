from sklearn.datasets import load_iris
iris = load_iris()

X=iris.data
Y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.4, random_state=1)
#print the shapes of X objects and Y objects
print(X_train.shape)
print(X_test.shape)

print(Y_test.shape)
print(Y_test.shape)