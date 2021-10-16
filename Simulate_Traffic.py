import numpy as np
import pandas as pd
import random
import statistics
import csv

##############################################################################################
# This function simulates the weekday and weekend traffic for route times, using files with
# all route durations, indices of the routes used and their demands
##############################################################################################

def trafficSimulation(weekdayFile, weekendFile, weekday_routes_used, saturday_routes_used, weekday_route_demands, saturday_route_demands):

    # Reading the csv files
    weekdayroute_file = np.loadtxt(open(weekdayFile), delimiter=',', skiprows=0)
    saturdayroute_file = np.loadtxt(open(weekendFile),  delimiter=',', skiprows=0)

    # List comprehension extracting times of routes used
    weekdayroute_file = [weekdayroute_file[int(i)] for i in weekday_routes_used]
    saturdayroute_file = [saturdayroute_file[int(i)] for i in saturday_routes_used]

    # Finding the number of durations for each file
    num_routes_weekday = len(weekdayroute_file)
    num_routes_saturday = len(saturdayroute_file)

    # Setting an array to store data
    durationsarray_weekday = np.zeros(num_routes_weekday)
    durationsarray_weekend = np.zeros(num_routes_saturday)

    # Simulating and storing durations while approximating the effect of traffic (-20% ~ +30% mins for weekdays, -10% ~ +20% mins for weekends)
    for i in range(num_routes_weekday):
        durationsarray_weekday[i] += (weekdayroute_file[i] - weekday_route_demands[i] * 450) * np.random.uniform(0.8, 1.3) + weekday_route_demands[i] * 450

    for j in range(num_routes_saturday):
        durationsarray_weekend[j] += (saturdayroute_file[j] - saturday_route_demands[j] * 450) * np.random.uniform(0.9, 1.2) + saturday_route_demands[j] * 450

    return durationsarray_weekday, durationsarray_weekend