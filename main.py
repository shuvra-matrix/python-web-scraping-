import pandas as pd
import requests
import csv
rows = []

data = pd.read_csv("web.csv")
web_data = {(data_row["url"]): data_row for (index, data_row) in data.iterrows()}
fields = ['url', 'result'] 
filename = "web_result.csv"
           
for i in web_data:
    x = requests.get(f'{i}')
    if "acko" in x.text:
        list = [i,'yes']
        rows.append(list)
    elif "Acko" in x.text:
        list = [i,'yes']
        rows.append(list)
    else:
        list = [i,'no']
        rows.append(list)

with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(rows)
            
