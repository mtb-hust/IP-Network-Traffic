import os
import pandas
import numpy as np
cwd = os.getcwd() #get current working directory
print(cwd)

splittedDataFolder = cwd + "/Data/labelledData/" #direct to containing folder
files = os.listdir(splittedDataFolder)
sum = 0
# header = ['SourceIP', 'SourcePort', 'DesIP','DesPort', 'FlowDuration', 'FlowBytes','FlowPackets','AvgPacketSize','ProtocolName']
for i in files:
    dataFrame = pandas.read_csv("./Data/labelledData/" + i)
    print(f"{dataFrame.shape} + {i}")
    sum += dataFrame.shape[0]
print(sum)