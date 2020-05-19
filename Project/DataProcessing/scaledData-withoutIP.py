import pandas as pd
import csv 
import numpy as np
import os

cwd = os.getcwd() #get current working directory
print(cwd)

splittedDataFolder = cwd + "/Data/splittedDataWithLabels/" #direct to containing folder
files = os.listdir(splittedDataFolder)
for file in files:
    df = pd.read_csv("./Data/splittedDataWithLabels/" + file)
    data = df.iloc[:,[1,3,4,5,6,7]].to_numpy
    print(data)
    