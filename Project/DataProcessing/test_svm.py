import top20largestFileReader as ReadData
from sklearn.svm import SVC
clf = SVC()
data,label = ReadData.read_data()
clf.fit(data,label)
print(clf.score(exidata,label))
