from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

iris = datasets.load_iris()
iris_data = iris.data
iris_target = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(iris_data,iris_target, test_size= 0.20)

classifier = KNeighborsClassifier()
classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)

print(accuracy_score(Y_pred, Y_test))
print(confusion_matrix(Y_pred, Y_test))