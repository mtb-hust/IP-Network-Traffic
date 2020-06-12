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
temp = ""
for i in dic.keys():
    temp = temp +"\n" +i
with open("./Data/allFiles.txt", "w") as file_X:
    file_X.write(temp)