from analyze import load_data
import argparse
from pathlib import Path

p = argparse.ArgumentParser(description="algorithm to detect anomalies")
p.add_argument("file", help="path to JSON data file")
P = p.parse_args()
file = Path(P.file).expanduser()
data = load_data(file)
print(data["temperature"].mean()["lab1"])
anomaly = {}
for i in data:
    print(i)
    num_cols = len(data[i].columns)
    print(f'num_cols: {num_cols}')
    mean = data[i].mean()
    print(type(mean))
    var = data[i].var()
    for j in mean:
        print(data[i]['lab1'])
