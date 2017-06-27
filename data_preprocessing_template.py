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



