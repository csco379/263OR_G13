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


# Cheapest Insertion ( Assume symetric times to shorten time)
for k in range(len(sets)):
    # 1 possible combination
    cluster = sets[k]
    
    for j in cluster: # checks from distribution centre

        # Indexing ID to find distance of each node from distribution 

        node[i] = durations[56, cluster[i]-1] # accounts for data frame shift (CHECK)
    
        # Select the minimum and add to the route 
        route.append(np.indices(min(node)))
        time += min(node) +7.5 
        pallets += North[cluster[i], 5]

        # Remove added node from cluster ( last added node)
        cluster.pop(route[-1])
        while(cluster!=[]): # while nodes arent visited continue adding to route
            #2d array row = current node number in partial solution, cols = number of nodes left to visit in cluster 
            min_duration = np.zeros((len(route), len(cluster)))
            time_back = np.zeros((len(route), len(cluster)))
            # Check for next shortest route addition at insertion positions
            # Need to check point in route that every store in cluster could be added
            for i in route: # Checks distances from each next node in route to each node in the remaining cluster
                for j in cluster: 
                    # min_duration = every store in partial solution going to every store remaining
                    min_duration[i,j] = durations[route[i]-1, cluster[j]-1] # ( -1 accounts for dataframe feature : double check)
                    # Time from node in cluster back to next node or the origin

            # Find minimum combo in this array so can find associated store, add to route ( in correct spot depending on which node from then increment time and pallets (back time)
            min_index = divmod(min_duration.argmin(), min_duration.shape[1])        
            route.append(cluster[min_index[0]]) # Extracts row of min index which is the route that adds the least time 
            time += min_duration[min_duration[min_index[0]], min_duration[min_index[1]]] + 7.5     # Adding time of third added node   
            pallets += North[cluster[min_index[0]], 5]
            cluster.pop(route[min_index[0]]) # Remove the last appended node from cluster
            # Cluster still has 1 store in it (for sets of 3)

            # Check where the next store should be inserted into route list
        
            for j in route:
        
                temp_route = route.append(57) # Puts the distriution centre as the last store so last insertion spot can be checked
                # Find min duration to node still in cluster
                min_duration_best_out = durations[route[j]-1, cluster[0]-1]
                min_duration_best_back = durations[cluster[0]-1, route[j+1]-1] # accounted for by appending the distribution centre and non symetry
                for i in range(1,len(cluster)-1): # Start at 1 because the first element has been checked
                    #Checking each i
                    min_duration_temp_out = durations[route[j]-1, cluster[i]-1]
                    min_duration_temp_back = durations[cluster[i]-1, route[j+1]-1] # Accounting for directions
                    # Recording if best time
                    if(min_duration_temp_out + min_duration_temp_back < min_duration_best_out + min_duration_best_back):
                        min_duration_best_out = min_duration_temp_out
                        min_duration_best_back = min_duration_temp_back
                        # Could make 1 variable above to optimise
                        store = cluster[i]
            
                # Insert best new node into array  
                temp_route.insert(j+1,store)
                # Calculating total route time with this node
                temp_time = time + min_duration_best_out + min_duration_best_back + 7.5
            
                if(j==0):
                    routeMatrix[k] = temp_route
                    timeArray[k] = temp_time
                elif(temp_time<timeArray[k]):
                    routeMatrix[k] = temp_route
                    timeArray[k] = temp_time
            


       
                
        #Make dure that route is then stored as a row in an additional array
    # Increment set in region
 #store in sol 
 #
 ##
 #





    
    


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



