from analyze import load_data
import argparse
from pathlib import Path

p = argparse.ArgumentParser(description="algorithm to detect anomalies")
p.add_argument("file", help="path to JSON data file")
P = p.parse_args()
file = Path(P.file).expanduser()
temp = load_data(file)["temperature"]
#print(temp)
var = temp.var()
mean = temp.mean()
low = mean - (2*(var**2))
high = mean + (2*(var**2))
lab1_temp = temp["lab1"]
office_temp = temp["office"]
class1_temp = temp["class1"]
lab1_bool = lab1_temp.between(low[0],high[0])
l = lab1_bool.where(lab1_bool == 'False').index
print(lab1_bool)
#print(data["temperature"].mean()["lab1"])
# anomaly = {}
# for i in data:
#     num_cols = len(data[i].columns)
#     mean = data[i].mean()
#     var = data[i].var()
    #for j in mean:
        #print(data[i]['lab1'])
