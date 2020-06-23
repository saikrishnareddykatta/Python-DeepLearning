import numpy as np
import pandas as pd
# Reading the data set
train = pd.read_csv('train.csv')
print("Train data shape:", train.shape)
import matplotlib.pyplot as plt
# plotting Sale Price vs Above ground living area
var = 'GarageArea'
data = pd.concat([train['SalePrice'], train[var]], axis=1)
plt.scatter(x=train['GarageArea'], y=train['SalePrice'])
plt.ylabel('Sale Price')
plt.xlabel('Above ground living area')
plt.show()
from scipy import stats
# calculating absolute value of each element in the data set "data"
# The z-scores, standardized by mean and standard deviation of input array.
z = np.abs(stats.zscore(data))
print(z)
threshold = 3
print(np.where(z > 3))
# Finding the Inter Quartile Range
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
# Deleting the Outlier data using Normal Distribution Curve or Bell Curve
data = data[(z < 3).all(axis=1)]
# Deleting the Outlier data using Inter Quartile Range
data_df_out = data[~((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1)]
print(data.shape)
print(data_df_out.shape)
# plotting Sale Price vs Above ground Using Normal Distribution Curve or Bell Curve
var = 'GarageArea'
plt.scatter(x=data['GarageArea'], y=data['SalePrice'])
plt.ylabel('Sale Price')
plt.xlabel('Above ground ')
plt.show()
#  plotting Sale Price vs Above ground Using Inter Quartile Range
plt.scatter(x=data_df_out['GarageArea'], y=data_df_out['SalePrice'])
plt.ylabel('Sale Price')
plt.xlabel('Above ground ')
plt.show()
