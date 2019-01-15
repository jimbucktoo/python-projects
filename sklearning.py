import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris

# features = [[140,0], [130,1], [169,0], [170,1]]
# labels = ["apples","oranges","bananas","cherries"]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(features, labels)
# print clf.predict([[170, 0.9]])

iris = load_iris()
print(iris.feature_names)
print(iris.target_names)

test_idx = [0,50,100]

# training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# print("train target:",train_target)
# print("test target:",test_target)
# print("train data:",train_data)
# print("test data:",test_data)

print(iris.target)
print(iris.data)

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print(test_target)
print(clf.predict(test_data))

