import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense,Conv1D, Dropout, MaxPooling1D, Flatten
from keras.activations import relu, sigmoid,softmax
from keras.losses import categorical_crossentropy
from keras.optimizers import RMSprop
import top20largestFileReader as ReadData
from sklearn.model_selection import train_test_split
import pandas as pd
from keras.callbacks import EarlyStopping
import numpy as np


data,label = ReadData.read_data()
shape = label.shape 
one_hot_label = np.zeros((shape[0], 20))
for i in range(shape[0]):
    one_hot_label[i][label[i]] = 1
X_train, X_test, Y_train, Y_test = train_test_split(data, one_hot_label, test_size = 0.30, shuffle = True)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1],1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1],1)
# Y_train = Y_train.reshape(Y_train.shape[0], Y_train.shape[1],1)
# Y_test = Y_test.reshape(Y_test.shape[0], Y_test.shape[1],1)
input_shape1 = X_train.shape
print(input_shape1)
model = Sequential()

model.add(Conv1D(filters=64, kernel_size=2, activation='relu', input_shape= (X_train.shape[1], 1)))
model.add(Conv1D(filters=64, kernel_size=2, activation='relu'))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(20, activation='softmax'))

#compile model using accuracy to measure model performance
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print(model.summary())
early_stopping_monitor = EarlyStopping(patience=20)
model.fit(X_train, Y_train, epochs=100,batch_size= 500, validation_split=0.2, callbacks=[early_stopping_monitor], shuffle = True, verbose = 2)
model.save("model1.h5")
result = model.evaluate(X_test, Y_test)
print(result)