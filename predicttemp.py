from google.colab import drive
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

drive.mount('/content/drive')
df = pd.read_csv('/content/drive/MyDrive/IceCreamData.csv')
df.head()

x = df['Temperature'].values
y = df['Revenue'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 50 , random_state = 43)
x_train = np.array((x_train))
x_test = np.array((x_test))
y_train = np.array((y_train))
y_test = np.array((y_test))

y_line = model.predict(x)

f = open('model.pickle', 'wb')
pickle.dump(model, f)
