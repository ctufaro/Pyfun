#multiple linear regression
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
# Import the dataset
path = 'C:\\Users\\ctufaro_admin\\My Projects\\Pyfun\Machine-Learning-A-Z-Template-Folder\\Machine Learning A-Z\\Part 2 - Regression\\Section 5 - Multiple Linear Regression\\Multiple_Linear_Regression'
pathData = path + '\\50_Startups.csv'

dataset = pd.read_csv(pathData)
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

#avoiding the dummy variable trap
X = X[:, 1:]

#splitting the test set and training set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

#feature scaling
'''from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_test = sc_X.transform(x_test)'''

#Fitting Multiple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

#Predicting the test set results
y_pred = regressor.predict(x_test)

#Building backward elimination
import statsmodels.formula api as sm