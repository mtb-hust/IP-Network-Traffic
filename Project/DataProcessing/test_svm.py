import top20largestFileReader as ReadData
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
clf = LinearSVC( C = 20)
data,label = ReadData.read_data()
shape = label.shape 
one_hot_label = np.zeros((shape[0], 20))
testData = []
testLabel = []
for i in range(shape[0]):
    one_hot_label[i][label[i]] = 1
for i in range(shape[0]):
    if i%5 == 0:
        testData.append(data[i])
        testLabel.append(label[i])
X_test, X_train, Y_test, Y_train = train_test_split(testData, testLabel, test_size = 0.30, shuffle = True)
clf.fit(X_train, Y_train)
print(clf.score(X_test,Y_test))
