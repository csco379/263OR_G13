# Generating a subset of feasible routes

# Libraries
import numpy as np
import pandas as pd
from Regions import set_boundaries
# Loading in store data

distributionCentre = pd.read_csv("Distribution_Centre_Data.csv")
weekdayData = pd.read_csv("Store_Data_Nonzero.csv")
#print(weekdayData)

# Applying regions
# Which pdf 
weekdayRegions = set_boundaries("Store_Data_Nonzero.csv") # ????IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices

# Route construction ideas 
# Stores for each region will be put into an ordered list so it can be popped off the list once included in a route, this will ensure each route is included at least once
# but can be included multiple times

# Second unordered list to ensure same route does not have 1 node twice

# greedy approach
# first go to min distance store, reserve second min distance store for way back.
# iteratively seek the next closest unvisited store on the list. until reach max number of pallets. 
# Could then seek any stores with demand less than that fulfilled, and if the duration is within some metric of distance it will go there rather than the next closest.

# Route improvement ideas
