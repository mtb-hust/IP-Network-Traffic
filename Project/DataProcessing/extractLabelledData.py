import pandas as pd
import csv
import numpy as np #import cac thu vien de doc data

#Because the whole file is so large - > split it in to small piece so that our machine can work better
#We read 10000k for each iteration

#our dataset have 
for i in range(380):
    skipRow = 10000*i
    dataFrame = pd.read_csv("./Data/RawData.csv", nrows= 10000, skiprows= [k for k in range(1,skipRow)])
    dataFrame = dataFrame.iloc[:, [1,2,3,4, 7, 20,21,58, 86]]
    for k in range(0,10000):
        try:
            temp = dataFrame.iloc[k]
            with open("./Data/splittedDataWithLabels/" + temp["ProtocolName"] +".csv", "+a") as file_X:
                writer = csv.writer(file_X, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(temp)
                file_X.close()
        except:
            continue
    print(i/380*100)