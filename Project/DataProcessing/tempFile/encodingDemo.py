import pandas as pd
import numpy as np
import os
cwd = os.getcwd() #get current working directory
print(cwd)

splittedDataFolder = cwd + "/Data/splittedDataWithLabels/" #direct to containing folder
files = os.listdir(splittedDataFolder)
for i in files:
    dataFrame = pd.read_csv("./Data/splittedDataWithLabels/" + i)
    dataFrame = dataFrame.to_numpy()
    print(dataFrame.shape)