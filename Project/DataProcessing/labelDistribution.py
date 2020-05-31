import os
import pandas
import numpy as np
cwd = os.getcwd() #get current working directory
print(cwd)

splittedDataFolder = cwd + "/Data/splittedDataWithLabels/" #direct to containing folder
files = os.listdir(splittedDataFolder)
# header = ['SourceIP', 'SourcePort', 'DesIP','DesPort', 'FlowDuration', 'FlowBytes','FlowPackets','AvgPacketSize','ProtocolName']
for i in files:
    dataFrame = pandas.read_csv("./Data/splittedDataWithLabels/" + i)
    print(dataFrame.shape)