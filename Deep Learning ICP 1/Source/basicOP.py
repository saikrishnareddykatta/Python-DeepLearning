import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# load data set
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

dataset = pd.read_csv("diabetes.csv", header=None).values

X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,0:8], dataset[:,8],
                                                    test_size=0.25, random_state=87)
np.random.seed(155)
# create model
my_first_nn = Sequential()

# One Hidden layer
my_first_nn.add(Dense(20, input_dim=8, activation='relu'))
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,
                                     initial_epoch=0)
one_hidden_summary = my_first_nn.summary()
one_hidden_accuracy = my_first_nn.evaluate(X_test, Y_test)

# Two Hidden Layers
my_first_nn.add(Dense(10, input_dim=8, activation='relu'))
my_first_nn.add(Dense(30, input_dim=8, activation='relu'))
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,
                                     initial_epoch=0)
two_hidden_summary = my_first_nn.summary()
two_hidden_accuracy = my_first_nn.evaluate(X_test, Y_test)

# Three Hidden Layers
my_first_nn.add(Dense(5, input_dim=8, activation='relu'))
my_first_nn.add(Dense(30, input_dim=8, activation='relu'))
my_first_nn.add(Dense(20, input_dim=8, activation='relu'))
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,
                                     initial_epoch=0)
three_hidden_summary = my_first_nn.summary()
three_hidden_accuracy = my_first_nn.evaluate(X_test, Y_test)
print(my_first_nn.metrics_names)
# print("Summary for One Hidden Layer" + str(one_hidden_summary))
print("Accuracy for One Hidden Layer: " + str(one_hidden_accuracy))
# print("Summary for Two Hidden Layer" + str(two_hidden_summary))
print("Accuracy for Two Hidden Layer: " + str(two_hidden_accuracy))
# print("Summary for Three Hidden Layer" + str(three_hidden_summary))
print("Accuracy for Three Hidden Layer: " + str(three_hidden_accuracy))