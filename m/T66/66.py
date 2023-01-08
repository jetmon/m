from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score, recall_score, precision_score, confusion_matrix
import pandas as pd

X = pd.read_csv("NBC.csv", names=['message', 'label'])
X['labelnum'] = X.label.map({'pos':0,'neg':1})
print(X)

X_message = X.message
Y_label_num = X.labelnum

X_train,X_test, Y_train, Y_test = train_test_split(X_message, Y_label_num)

cv = CountVectorizer()
X_train_f_tf = cv.fit_transform(X_train)
X_test_tf = cv.transform(X_test)

MNB = MultinomialNB()
MNB.fit(X_train_f_tf, Y_train)
Y_pred = MNB.predict(X_test_tf)

print(accuracy_score(Y_test, Y_pred))
print(confusion_matrix(Y_test, Y_pred))