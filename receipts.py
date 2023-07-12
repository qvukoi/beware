import pandas as pd
import openpyxl

while True:
    ask=input("start? y/n: ")
    if ask=="n":
        break
    
    else:
        x=input("name: ")
        if True:
            print("ok")
    
    try:
        z=float(input("weight or amount: "))
        if True:
            print("ok")
    except ValueError:
        print("error. try again")
        continue
    
    try:    
        y=int(input("price: "))
        if True:
            print("ok")
    except ValueError:
        print("error. try again")
        continue

    row=pd.DataFrame({
    "name":[x],
    "weight":[z],
    "price":[y]})

    with pd.ExcelWriter("Data.xlsx",
                    mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:  
        row.to_excel(writer, sheet_name="data", startrow=writer.sheets["data"].max_row, header=None, index=False)

read=pd.read_excel("Data.xlsx")
total=list(read.sum())[2]
print("success! total: "+str(total))