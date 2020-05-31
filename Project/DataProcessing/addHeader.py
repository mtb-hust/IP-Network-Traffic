# File này được dùng để thêm tiêu đề cho file csv được tách ra từ labelledData,
#  vì sau khi xuất file từ labbelledData, header bị mất, làm missing một hàng data
import pandas as pd
import csv 
import numpy as np
import os

cwd = os.getcwd() #get current working directory
print(cwd)

splittedDataFolder = cwd + "/Data/splittedDataWithLabels/" #direct to containing folder
files = os.listdir(splittedDataFolder)
header = ['SourceIP', 'SourcePort', 'DesIP','DesPort', 'FlowDuration', 'FlowBytes','FlowPackets','AvgPacketSize','ProtocolName']
for file in files:
    with open("./Data/splittedDataWithLabels/" + file, newline='') as f:
        r = csv.reader(f)
        with open("./Data/labelledData/" + file, "+a") as file_X:
            writer = csv.writer(file_X)   
            writer.writerow(header)
            for line in r:
                writer.writerow(line)
    print(file)