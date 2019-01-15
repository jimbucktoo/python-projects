import random
from sklearn import datasets
from sklearn.model_selection import train_test_split


class ScrappyKNN:

    def __init__(self):
        pass

    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test):
        predictions = []
        for row in x_test:
            label = random.choice(self.y_train)
            predictions.append(label)
        return predictions

iris = datasets.load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .5)

# from sklearn import tree
# my_classifier = tree.DecisionTreeClassifier()

# from sklearn.neighbors import KNeighborsClassifier
# my_classifier = KNeighborsClassifier()

my_classifier = ScrappyKNN()

my_classifier.fit(x_train, y_train)
predictions = my_classifier.predict(x_test)

print(predictions)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))