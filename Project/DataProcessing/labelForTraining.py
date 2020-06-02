import os
import pandas
import numpy as np
cwd = os.getcwd() #get current working directory
print(cwd)

splittedDataFolder = cwd + "/Data/labelledData/" #direct to containing folder
files = os.listdir(splittedDataFolder)
dic = {}
# header = ['SourceIP', 'SourcePort', 'DesIP','DesPort', 'FlowDuration', 'FlowBytes','FlowPackets','AvgPacketSize','ProtocolName']
for i in files:
    dataFrame = pandas.read_csv("./Data/labelledData/" + i)
    print(f"{dataFrame.shape} + {i}")
    lines = dataFrame.shape[0]
    dic[i] = lines
frequency = [i for i in dic.values()]
frequency.sort(reverse = True)
top20dic = ""
count = 0
for i in frequency:
    count += 1
    if count <= 20:
        frequency.remove(i)
        for j in dic.keys():
            if dic[j] == i:
                top20dic += "\n" +j   
with open("./Data/sorted20File.txt", "w") as file_X:
    file_X.write(top20dic)
    