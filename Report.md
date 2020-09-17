# 2020-sensor-miniproject Report

### Contributors: Jyotsna Penumaka (BU ID: U13844479), Emanuel Perez (BU ID: U74196797)


## Task 0
#### 1) What is the greeting string issued by the server to the client upon first connecting?
The greeting string issued by the server to the client upon first connecting : ECE Senior Capstone IoT simulator                 

## Task 1
#### 1) Add Python code to Websockets client that saves the JSON data to a text file as it comes in (message by message)

```sh
python3  -m sp_iotsim.server
python3 -m sp_iotsim.client -l log.txt
```
We added code to src/sp_iotsim/client.py to collect data in a text file, in this case log.txt. 

## Task 2
```sh
python3 analyze.py log.txt
```
We added code to analyze.py to complete this task. Most of the tasks were done using pandas built-in functions.
#### 1) Report median and variance observed from temperature data

###### Temperature

Room | Median | Variance
-----|--------|----------
Lab1 | 21.01 | 7.41

#### 2) Report median and variance observed from the occupancy data

###### Occupancy 

Room | Median | Variance
-----|--------|----------
Lab1 | 5.00 | 5.05

#### 3) Plots of Probability Distribution Functions for each Sensor
<img width="639" alt="Screen Shot 2020-09-15 at 10 22 12 PM" src="https://user-images.githubusercontent.com/60219242/93285103-12c6c300-f7a2-11ea-932a-48a38cd12078.png">
<img width="637" alt="Screen Shot 2020-09-15 at 10 21 46 PM" src="https://user-images.githubusercontent.com/60219242/93285069-0478a700-f7a2-11ea-8d30-7729ace067f7.png">
<img width="638" alt="Screen Shot 2020-09-15 at 10 21 59 PM" src="https://user-images.githubusercontent.com/60219242/93285094-0c384b80-f7a2-11ea-8edb-5a88c5759aa6.png">

#### 4) Histogram Plots for each Sensor
<img width="638" alt="CO2 Histogram" src="https://user-images.githubusercontent.com/35668165/93511210-70692580-f8f0-11ea-91fb-04c5c239233e.png">
<img width="638" alt="Occupancy Histogram" src="https://user-images.githubusercontent.com/35668165/93511220-75c67000-f8f0-11ea-8afb-6945ae0e8d10.png">
<img width="638" alt="Temperature Histogram" src="https://user-images.githubusercontent.com/35668165/93511229-7a8b2400-f8f0-11ea-9b94-0b6fc10e79ef.png">


#### 5) What is the mean and variance of the time interval of the sensor readings? Please plot its probability distribution function. Does it mimic a well-known distribution for connection intervals in large systems? 

###### Time Interval of the Sensor Readings
Mean | Variance
-----|----------
0.968014 | 1.013983

###### Time Interval probability density function
<img width="632" alt="Screen Shot 2020-09-15 at 10 21 35 PM" src="https://user-images.githubusercontent.com/60219242/93285042-faef3f00-f7a1-11ea-8455-84a45c3f853c.png">

###### Time Interval Histogram
<img width="596" alt="Screen Shot 2020-09-17 at 3 49 42 PM" src="https://user-images.githubusercontent.com/60219242/93521239-c98b8600-f8fd-11ea-8496-64c93215e0f8.png">

Yes, it mimics the Erlang distribution which is used to predict waiting times in queuing systems. Erlang distrubution is also specific case of a Gamma distrubtion. Since the time intervals for all three rooms are the same, we are using one probability distribution function graph to represent them.


## Task 3
#### 1) Implement an algorithm that detects anomalies in temperature sensor data. Print the percent of "bad" data points and determine the temperature median and variance with these bad data points discarded--the same room you did in Task 2 Question 1.

```sh
python3 algorithm.py log.txt
```
Fraction of "Bad Readings" in temperature sensor data for Lab1: 
Room | Percentage | Fraction
-----|------------|----------
Lab1 | 1.11% | 6/540

The temperature median and variance with these bad data points discarded:

Room | Median | Variance
-----|--------|----------
Lab1 | 21.01 | 0.31

#### 2) Does a persistent change in temperature always indicate a failed sensor?
Not necessarily. A minute change caused by opening doors or changing the AC does not indicate a failed sensor. However, a drastic change would indicate a failed sensor (big change → sensor fails). The rate of change needs to be consistent with reality for example it cannot go from 27 celsius to 41 or from 27 celsius to -26. 


#### 3) What are possible bounds on temperature for each room type?
Upper and Lower bounds were calculated using 68–95–99.7 rule, which would result in 95.45% of the values to lie within two standard deviations of the mean. This was used to filter the data in task 3. This was completed in algorithm.py.

Upper bounds : mean + (2 * standard deviation)

Lower bounds : mean - (2 * standard deviation)

room | Upper Bound | Lower Bound
-----|-------------|-------------
lab1 | 15.51 | 26.40
class1 | 10.41 | 44.52
office | 15.24 | 30.73


## Task 4
#### 1) How is this simulation reflective of the real world?
As stated before, the simulation follows the Erlang distribution used in queueing systems and alike. The simulation also takes into account that sensors, at times, fail to correctly collect information from their surroundings.

#### 2) How is this simulation deficient? What factors does it fail to account for?
The simulation is deficient because it does not account for the time of the day and the change in temperature from opening or closing of the doors in the room. In other words, the simulation can have more realistic features to it.

#### 3) How is the difficulty of initially using this Python websockets library as compared to a compiled language e.g. C++ websockets
Python websockets library was convenient to use since the functions were well documented and easy to find compared to C++ websockets. 


#### 4) Would it be better to have the server poll the sensors, or the sensors reach out to the server when they have data?
It is better for the server to poll the sensor to keep complicated situations to occur especially as the number of sensors increase.
