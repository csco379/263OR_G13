import numpy as np
import pandas as pd
import random
import statistics
import csv

# This function simulates the weekday and weekend traffic for route times
def trafficSimulation(weekdayFile, weekendFile):

    # Reading the csv files
    weekdayroute_file = pd.read_csv(weekdayFile)
    weekendroute_file = pd.read_csv(weekendFile)

    # Finding the number of durations for each file
    num_routes_weekday = len(weekdayroute_file)
    num_routes_weekend = len(weekendroute_file)

    # Setting an array to store data
    durationsarray_weekday = np.zeros(num_routes_weekday)
    durationsarray_weekend = np.zeros(num_routes_weekend)

    # Simulating and storing durations while approximating the effect of traffic (-20% ~ +50% mins for weekdays, -10% ~ +20% mins for weekends)
    for i in range(num_routes_weekday):
        durationsarray_weekday[i] += weekdayroute_file.iloc[i] * np.random.uniform(0.8, 1.5)

    for j in range(num_routes_weekend):
        durationsarray_weekend[j] += weekendroute_file.iloc[j] * np.random.uniform(0.9, 1.2)

    return durationsarray_weekday, durationsarray_weekend