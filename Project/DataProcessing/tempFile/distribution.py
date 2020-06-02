import pandas as pd
import os
import csv
cwd = os.getcwd() #get current working directory
print(cwd)

splittedDataFolder = cwd + "/Data/splittedDataWithLabels/" #direct to containing folder

dictionary = {}

files = os.listdir(splittedDataFolder)
for file in files:
    df = pd.read_csv("./Data/splittedDataWithLabels/" + file)
    shape = df.shape
    dictionary[file] = shape[0] + 1 #compute file shape

sortedDictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])} #sort sortedDictionary by value

print(sortedDictionary)


