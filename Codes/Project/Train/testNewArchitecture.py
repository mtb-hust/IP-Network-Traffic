import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense,Conv1D, Dropout, GlobalAveragePooling1D
from keras import Input
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
input_shape = X_train.shape
print(input_shape)
model=Sequential()
model.add(Input(shape))
model.add(Conv1D(filters=128, kernel_size = 7, strides=3, activation='relu'))
model.add(Dropout(0.2))
model.add(Conv1D(filters=512, kernel_size = 7, strides=3, activation='relu'))
model.add(Dropout(0.2))
model.add(GlobalAveragePooling1D())
model.add(Dense(20, activation=softmax))
model.compile(loss="categorical_crossentropy",optimizer=RMSprop(),metrics=["accuracy"])
model.fit(X_train,Y_train, epochs = 500, batch_size= 512)
model.save("model1.h5")
model = keras.models.load_model("model.h5")
result = model.evaluate(X_test, Y_test)
print(result)