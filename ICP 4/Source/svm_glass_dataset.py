import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
# reading data from glass.csv
data = pd.read_csv('glass.csv')
# dropping the target column from the data set
X_train = data.drop("Type", axis=1)
# appending target column to training data set
Y_train = data["Type"]
# splitting the data set into train data set and test data set
X_train, X_test, Y_train, Y_test = train_test_split(X_train, Y_train, test_size=0.4, random_state=0)
# SVM Classifier
svc = SVC()
# fitting the train data set
svc.fit(X_train, Y_train)
# predicting the test data set
Y_pred = svc.predict(X_test)
# finding the accuracy
acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
acc_svc = round(svc.score(X_test, Y_test) * 100, 2)
print("Naive Bayes Accuracy for train data is: ", acc_svc)
print("Naive Bayes Accuracy for test data is: ", acc_svc)
# classification report
print("Classification Report:\n", classification_report(Y_test, Y_pred))

