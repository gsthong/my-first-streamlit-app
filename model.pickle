from google.colab import drive
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

drive.mount('/content/drive')
df = pd.read_csv('/content/drive/MyDrive/IceCreamData.csv')

x = df['Temperature'].values
y = df['Revenue'].values
x.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=50, random_state=43)

model = LinearRegression()
model.fit(x_train, y_train)

f = open('model.pickle', 'wb')
pickle.dump(model, f)
