import os
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 

# Import the dataset
path = 'C:\\Users\\ctufaro_admin\\My Projects\\Pyfun\Machine-Learning-A-Z-Template-Folder\\Machine Learning A-Z\\Part 1 - Data Preprocessing'
pathData = path + '\\Data.csv'

dataset = pd.read_csv(pathData)
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

#splitting the test set and training set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

#feature scaling
'''from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_test = sc_X.transform(x_test)'''