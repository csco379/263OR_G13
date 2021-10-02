# Generating a subset of feasible routes

# Libraries
import numpy as np
import pandas as pd
from Regions import set_boundaries
# Loading in store data

distributionCentre = pd.read_csv("Distribution_Centre_Data.csv")
weekdayData = pd.read_csv("Store_Data_Nonzero.csv")
durations = pd.read_csv("WoolworthsTravelDurations.csv")

#print(weekdayData)

# Applying regions
# Which pdf 
weekdayRegions = set_boundaries("Store_Data_Nonzero.csv") # ????IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
weekdayRegions


# Approach
# Step 1 : Seperating data into regions based on the attribute
# Loop through different regions 
# In each region every combination of 3 stores will be formed ( order doesn't matter) and recorded in lists corresponding to route and the ID's of stores in each route (pallets <30)

# For loop that does Cheapest insertion on each combination. ( to figure out best order for the nodes in the combination)
# Best order will be turned into a 1D array of which stores and in which order () 
# Output of Cheapest insertion for loop
#   route
#   1 [3, 0, 2, 1...(number of stores)]
#   2 rest of the routes (appended to row above)
#   3
#   Corresponding time and cost of each route are also input into a 1D array


# Make a copy of this 2D array and turn all values >= 1 into 1

# These 3 arrays (2D binary route matrix, time and cost, 1D arrays) convert to csv to feed straight into solver. 



