# Generating a subset of feasible routes

# Libraries
import numpy as np
from numpy.core.einsumfunc import _einsum_path_dispatcher  #?????
from numpy.lib.nanfunctions import _nanprod_dispatcher
import pandas as pd
import itertools
from Regions import set_boundaries


# Read in grouped data
distributionCentre = pd.read_csv("Distribution_Centre_Data.csv")
data = pd.read_csv("Store_Data_Some_zero_GROUPED.csv")
durations = pd.read_csv("WoolworthsTravelDurations.csv").to_numpy()
# Distribution centre distances 
DC = durations[56]

# Seperate the data into regions and convert to numpy arrays
North = data.loc[data["Region"]=='North'].to_numpy()
South = data.loc[data["Region"]=='South'].to_numpy()
East = data.loc[data["Region"]=='East'].to_numpy()
West = data.loc[data["Region"]=='West'].to_numpy()
Central= data.loc[data["Region"]=='Central'].to_numpy()


# Loop to apply to each region to get each combination of 3 stores
# check time not >30 Duration 
# object = (sets[0])[0]  tuple indexing
# ID
ID_set = North[:,4]
#list every unordered combo of 3 stores
sets = list(itertools.combinations(ID_set, 3))


# Creating ordered route array to store outcome
route = [O]
currentRoute = []

# 1d array 
node = []


# Cheapest Insertion
for i in range(len(sets)):
    # 1 possible combination
    cluster = sets[i]
    
    for j in cluster: # checks from origin

        # Indexing ID to find distance of each node from distribution 

        node[i] = durations[56, cluster[i]-1] # accounts for data frame shift (CHECK)
    
    # Select the minimum and add to the route 
    route.append(np.indices(min(node)))
    time += min(node)
    pallets += North[cluster[i], 5]

    # Remove added node from cluster ( last added node)
    cluster.pop(route[-1])
    while(cluster!=[]): # while nodes arent visited continue adding to route
        #2d array row = current node number in partial solution, cols = number of nodes left to visit in cluster 
        min_duration = np.zeros((len(route), len(cluster)))
        # Check for next shortest route addition at insertion positions
        for j in cluster: # Checks distances from each next node in route to each node in the remaining cluster
            for i in route:
                min_duration[i,j] = durations[route[i]-1, cluster[j]-1] # can index according to this ( -1 accounts for dataframe feature)
                # Find minimum of this array the find associated store, add to route ( in correct spot depending on which node from then increment time and pallets (back time)
                route.append(np.indices(min(min_duration)))
                nodes[i]= 
                # Remove the last appended node from cluster
        #Make dure that route is then stored as a row in an additional array
    # Increment set in region
 





    
    


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



