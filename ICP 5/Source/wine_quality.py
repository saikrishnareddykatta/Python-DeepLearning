import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
# Reading the data set
dataset = pd.read_csv('winequality-red.csv')
# finding and printing the number of null values in the data set
print('The total null values in the data set are ', dataset.isnull().sum().sum())
# Grouping into features and target label
X = dataset.drop(['quality'], axis=1)
Y = dataset[['quality']]
# Build a Linear Model
from sklearn.model_selection import train_test_split
# split the data into train and test data sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=.33)
lr = linear_model.LinearRegression()
lr.fit(X_train, y_train)
y_prediction = lr.predict(X_test)
# Evaluate the performance of model using R^2 and RMSE score
print ("R^2 is: %.2f" % lr.score(X_test, y_test))
# print("R^2 Score: %.2f" % r2_score(Y, y_prediction))
print("Root Mean Squared Error: %.2f" % mean_squared_error(y_test, y_prediction))
# Finding the Correlation between target label and top 3 features
numeric_features = dataset.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print('Top 3 correlated variables to the target variable quality is: ')
print(corr['quality'].sort_values(ascending=False)[:4], '\n')