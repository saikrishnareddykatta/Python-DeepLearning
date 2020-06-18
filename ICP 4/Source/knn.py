import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier

train_df = pd.read_csv('./train_preprocessed.csv')
test_df = pd.read_csv('./test_preprocessed.csv')
X_train = train_df.drop("Survived",axis=1)
Y_train = train_df["Survived"]
X_test = test_df.drop("PassengerId",axis=1).copy()
print(train_df[train_df.isnull().any(axis=1)])
# KNN Classifier
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
acc_knn = round(knn.score(X_train, Y_train) * 100, 2)

# finding the KNN Accuracy
print("KNN accuracy is:",acc_knn)
print(train_df[['Sex', 'Survived']]. \
      groupby(['Sex']). \
      mean().sort_values(by='Survived', ascending=False))

# Using the Correlation method
data = train_df[['Sex', 'Survived']]
correlation = data.corr(method='pearson')
print(correlation)