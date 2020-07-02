from keras.models import Sequential
from keras.layers.core import Dense, Activation
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Question 2 - 2.	Change the data source to Breast Cancer data set
# available in the source folder and make required changes

# Load Data Set
dataset = pd.read_csv("breastcancer.csv").values
# to change categorical values to numerical values
labelencoder_Y = LabelEncoder()
y_label = labelencoder_Y.fit_transform(dataset[:, 1])
X_train, X_test, Y_train, Y_test = train_test_split(dataset[:, 2:32], y_label,
                                                    test_size=0.25, random_state=87)
print(X_train.shape)
print(Y_train.shape)
np.random.seed(155)
# create model
my_first_nn = Sequential()
# hidden layer
my_first_nn.add(Dense(60, input_dim=30, activation='relu'))
# output layer
my_first_nn.add(Dense(1, activation='sigmoid'))
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,initial_epoch=0)
my_first_nn.summary()
accuracy = my_first_nn.evaluate(X_test, Y_test)

# Question 3 -  Normalize the data before feeding the data to the model
# and check how the normalization change your accuracy
print("BEFORE NORMALIZATION")
print(dataset[:, 2:32])
from sklearn.preprocessing import StandardScaler
sc = StandardScaler().fit(dataset[:, 2:32])
dataset[:, 2:32] = sc.transform(dataset[:, 2:32])
print("AFTER NORMALIZATION")
print(dataset[:, 2:32])
X_train, X_test, Y_train, Y_test = train_test_split(dataset[:, 2:32], y_label,
                                                 test_size=0.25, random_state=87)
np.random.seed(155)
# create model
my_first_nn = Sequential()
# hidden layer
my_first_nn.add(Dense(60, input_dim=30, activation='relu'))
# output layer
my_first_nn.add(Dense(1, activation='sigmoid'))
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,initial_epoch=0)
my_first_nn.summary()
accuracy_normalization = my_first_nn.evaluate(X_test, Y_test)
print(my_first_nn.metrics_names)
print("Accuracy: " + str(accuracy))
print("Accuracy After Normalization: " + str(accuracy_normalization))
