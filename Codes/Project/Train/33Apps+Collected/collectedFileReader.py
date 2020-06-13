import pandas as pd
import numpy  as np
from sklearn.preprocessing import MinMaxScaler
def read_data():
    with open("./Data/collectedFiles.txt") as file_x:
        list_name=file_x.read().split("\n")
    data = []
    label = []
    name2index = {}
    count = 0
    for name_file in list_name:
        name2index[name_file.split('.')[0]] = count
        count += 1
    column_label = 'Label'
    list_column_name = [ 'Src Port', 'Dst Port', 'Flow Duration', 'Flow Byts/s', 'Flow Pkts/s', 'Pkt Size Avg']
    for name_file in list_name:
        dataFrame_ = pd.read_csv('./Data/collectedData/' + name_file)
        dataFrame = dataFrame_[list_column_name].values.tolist()
        numLabels = len(dataFrame)
        label = name_file[:-4]
        labelFrame = dataFrame_[column_label].values.tolist()
        print(f"{len(dataFrame)} + {name_file}")
        for index in range(len(dataFrame)):
            data.append(dataFrame[index])
            # label_ = [0.0 for _ in range(len(list_name))]
            label_=name2index[labelFrame[index]]
            label.append(label_)
    data = np.array(data)
    label = np.array(label)
    return (dataScaler(data),label)
def dataScaler(data):
    scaler = MinMaxScaler(feature_range=(0,1))
    scaler.fit(data)
    return scaler.transform(data)
if __name__ == "__main__":
    data,label = read_data()
    data = dataScaler(data)
    print(data)
    np.savetxt("./temp.csv", data, delimiter=",")