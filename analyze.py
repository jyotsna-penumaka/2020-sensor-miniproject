#!/usr/bin/env python3
"""
This example assumes the JSON data is saved one line per timestamp (message from server).
It shows how to read and process a text file line-by-line in Python, converting JSON fragments
to per-sensor dictionaries indexed by time.
These dictionaries are immediately put into Pandas DataFrames for easier processing.
Feel free to save your data in a better format--I was just showing what one might do quickly.
"""
import pandas
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import matplotlib.pyplot as plt
import numpy as np


def load_data(file: Path) -> T.Dict[str, pandas.DataFrame]:

    temperature = {}
    occupancy = {}
    co2 = {}

    with open(file, "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])

            temperature[time] = {room: r[room]["temperature"][0]}
            occupancy[time] = {room: r[room]["occupancy"][0]}
            co2[time] = {room: r[room]["co2"][0]}

    data = {
            "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
            "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
            "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
            }

    return data

def analyse_data(data: T.Dict[str, pandas.DataFrame]):
    for k in data:
        if k != "co2":
            median = data[k]["lab1"].median()
            var = data[k]["lab1"].var()
            print(f'median observed from the lab1 {k} data: {"{:.2f}".format(median)}')
            print(f'variance observed from the lab1 {k} data: {"{:.2f}".format(var)}')
        plt.figure()
        (data[k]["lab1"]).plot.density(label=k,title=f'probability distribution function for lab1')
        plt.xlabel(k)
        plt.ylabel('Probability')
        plt.legend(loc="upper left")
    time = data["temperature"].index
    time_delta = (time[1:]-time[:-1]).total_seconds().to_series().to_frame()
    time_var = time_delta.var()
    time_mean = time_delta.mean()
    print(f'variance of the time interval of the sensor readings {time_var}')
    print(f'mean of the time interval of the sensor readings {time_mean}')
    time_delta.plot.density(title=f'probability distribution function for time')
    plt.xlabel('Time Interval (seconds)')
    plt.ylabel('Probability')
    time_delta.plot.hist(title=f'probability distribution function for time')
    plt.xlabel('Time Interval (seconds)')
    plt.ylabel('Probability')
    plt.figure()
    # To make the histograms              
    plt.suptitle("Lab1 Occupancy Histogram")
    data["occupancy"].lab1.hist()
    plt.ylabel("Number of entries")
    plt.xlabel("Occupancy")
    plt.figure()
    plt.suptitle("Lab1 Temperature Histogram")
    data["temperature"].lab1.hist()
    plt.ylabel("Number of entries")
    plt.xlabel("Temperature")
    plt.figure()
    plt.suptitle("Lab1 CO2 Histogram")
    data["co2"].lab1.hist()
    plt.ylabel("Number of entries")
    plt.xlabel("CO2")
                  
    plt.show()

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()
    file = Path(P.file).expanduser()

    data = load_data(file)
    analyse_data(data)