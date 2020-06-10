#bảng phân tích dữ liệu, phân phối của các cột dữ liệu được trích xuất. 
#từ đó có thể xem xét tính chất dữ liệu
import pandas as pd
import csv 
import numpy as np
import os

cwd = os.getcwd() #get current working directory
print(cwd)

splittedDataFolder = cwd + "/Data/splittedDataWithLabels/" #direct to containing folder
files = os.listdir(splittedDataFolder)

with open("./Data/analyze.csv", "+a") as file_x:
    writer = csv.writer(file_x, delimiter =  ",")
    writer.writerow(["ProtocolName","MinSourcePort", "MaxSourcePort", "MinDesport", "MaxDesport","MinFlowDur","MaxFlowDur","MinFlowBytes"
        , "MaxFlowBytes", "MinFlowPackets", "MawFlowPackets", "MinAvgPacketSize", "MaxAvgPacketSize"
        ])
    for file in files:
        df = pd.read_csv("./Data/labelledData/" + file)
        data = [file]
        for col in df.columns:
            if(col == "SourceIP" or col == "DesIP" or  col ==  "ProtocolName"):
                continue
            temp = df[col].to_numpy()
            min1 = temp.min()
            max2 = temp.max()
            print(f"{col} + {min1} +{max2}")
            data.append(min1)
            data.append(max2)
        writer.writerow(data)
        print(data)
    

            
        