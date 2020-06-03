import keras
import tensorflow as tf
from keras.models import Sequential
from keras .layers import Dense
from keras.activations import relu, sigmoid,softmax
from keras.losses import categorical_crossentropy
from keras.optimizers import RMSprop
import top20largestFileReader as ReadData
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


data,label = ReadData.read_data()
shape = label.shape 
one_hot_label = np.zeros((shape[0], 20))
for i in range(shape[0]):
    one_hot_label[i][label[i]] = 1
print(type(one_hot_label))
print(type(data))
X_train, X_test, Y_train, Y_test = train_test_split(data, one_hot_label, test_size = 0.30, shuffle = True)
print(type(X_test))
print(type(X_train))
model=Sequential()
model.add(Dense(256,input_dim=6,activation=relu))
model.add(Dense(512,activation=relu))
model.add(Dense(16,activation=softmax))
model.compile(loss="categorical_crossentropy",optimizer=RMSprop(),metrics=["accuracy"])
model.fit(X_train.transpose,Y_train.transpose, epochs = 500, steps_per_epoch = 500, batch_size = 1024)
model.save("model.h5")