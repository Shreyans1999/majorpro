# Importing library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from sklearn import metrics 
import warnings
warnings.filterwarnings('ignore')
# To read the dataset
data = pd.read_csv("phishing.csv")
data.head()
# Drop unecesssary columns
data = data.drop(['Index'],axis = 1)
data.describe().T
# Give all the columns name
data.columns
# To know about the datatypes of the columns
data.dtypes
# To know the size of the dataset along with the columns
data.shape
# To display the whole dataset
data
