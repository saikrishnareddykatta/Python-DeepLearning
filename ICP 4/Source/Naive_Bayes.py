import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
# reading data from glass.csv
data = pd.read_csv('glass.csv')
# removing target column from the data set
X_train = data.drop("Type", axis=1)
# appending target column to the training data set
Y_train = data["Type"]
# splitting the data set into train data set and test data set
X_train, X_test, Y_train, Y_test = train_test_split(X_train, Y_train, test_size=0.2, random_state=0)
# Naive Bayes Classifier
nav = GaussianNB()
# fitting the train data set
nav.fit(X_train, Y_train)
# predicting the test data set
Y_pred = nav.predict(X_test)
# finding the accuracy
acc_nav = round(nav.score(X_train, Y_train) * 100, 2)
acc_nav2 = round(nav.score(X_test, Y_test) * 100, 2)
print("Naive Bayes Accuracy for train data is: ", acc_nav)
print("Naive Bayes Accuracy for test data is: ", acc_nav2)
# classification report
print("Classification Report:\n", classification_report(Y_test, Y_pred))

