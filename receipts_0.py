import pandas as pd

data=pd.DataFrame({
    "name":[],
    "weight":[],
    "price":[]})

data.to_excel("Data.xlsx", sheet_name="data", startcol=0, startrow=0, index=False)