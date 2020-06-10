# kiểm trả tập data có bao nhiêu cột, mỗi cột có thông số ra sao

import pandas as pd

dataFrame = pd.read_csv("./Data/RawData.csv", nrows = 10)
i = 0
print(dataFrame.iloc[1])
for col in dataFrame.columns:
    print(f"{col} : {i}")
    i = i +1
#check what columns to keep

