from analyze import load_data
from pathlib import Path

import argparse
import math

p = argparse.ArgumentParser(description="algorithm to detect anomalies")
p.add_argument("file", help="path to JSON data file")
P = p.parse_args()
file = Path(P.file).expanduser()
lab1_temp = (load_data(file)["temperature"])["lab1"]

var = lab1_temp.var()
mean = lab1_temp.mean()

low = mean - (2*math.sqrt(var))
high = mean + (2*math.sqrt(var))

lab1_bad_temp = lab1_temp[(low >= lab1_temp) | (lab1_temp >= high)]
bad_fraction = "{:.2f}".format((lab1_bad_temp.count()/lab1_temp.count())*100)
print(f'the percent of "bad" data points: {bad_fraction}%')

lab1_good_temp = lab1_temp[(low <= lab1_temp) & (lab1_temp <= high)]
var = "{:.2f}".format(lab1_good_temp.var())
median = "{:.2f}".format(lab1_good_temp.median())
print(f'median observed from the lab1 temperature data after discarding bad data points: {median}')
print(f'variance observed from the lab1 temperature data after discarding bad data points: {var}')