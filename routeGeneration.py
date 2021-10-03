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
# Distribution centre index
DC = 55

# Seperate the data into regions and convert to numpy arrays
North = data.loc[data["Region"]=='North'].to_numpy()
South = data.loc[data["Region"]=='South'].to_numpy()
East = data.loc[data["Region"]=='East'].to_numpy()
West = data.loc[data["Region"]=='West'].to_numpy()
Central= data.loc[data["Region"]=='Central'].to_numpy()


# Generalise for loop for each region
region = North

# Loop to apply to each region to get each combination of 3 stores
# ID
ID_set = region[:,4]
#list every unordered combo of 3 stores
sets = list(itertools.combinations(ID_set, 3))

# Initialising lists
############################################################
# Creating ordered route array to store outcome
route = [DC] # Distribution centre ID is the first element of all routes
currentRoute = []
node = []
time= 0.0
pallets = 0
temp_route = []
# Initialising final time and route storage lists
routeMatrix = [[]]
timeArray = []
palletsArray = []
############################################################

# Cheapest Insertion ( Assume symetric durations)
for k in range(len(sets)):
    print(k) # To check progress whilst running 
    # 1 possible combination of stores
    cluster = list(sets[k])
    
    for n in cluster: # checks from distribution centre

        # Indexing ID to find distance of each store in cluster from distribution 
        node.append(durations[DC, n+1]) # accounts for data frame shift (CHECK)
    
        # Select the minimum time and add to the route ( Symetric assumption here) 
        route.append(node.index(min(node)))
        time += min(node) + 7.5 # Here only accounting for one way
        pallets += region[n, 5]
        # Remove added node from cluster ( last added node)
        cluster.pop(route[-1])

        while(cluster!=[]): # while nodes arent in the partial solution continue adding to route
            #2d array row = current node number in partial solution, cols = number of nodes left to visit in cluster 
            min_duration = np.zeros((len(route), len(cluster)))
            time_back = np.zeros((len(route), len(cluster)))
            # Check for next shortest route addition at insertion positions
            # Need to check point in route that every store in cluster could be added
            route.append(DC) # Distribution centre store
            for i in range(len(route)-1): # Checks distances from each next node in route to each node in the remaining cluster
                for j in range(len(cluster)): 
                    min_time_temp = durations[route[i]-2, cluster[j]+1] + durations[route[i+1]-2, cluster[j]+1]
                    if(j==0):
                        min_time = time + min_time_temp + 7.5
                        min_store = cluster[j]
                        pallets_temp = pallets + region[min_store,5]
                    elif(min_time_temp<min_time):
                        min_time = time + min_time_temp + 7.5
                        min_store = cluster[j]
                        pallets_temp = pallets + region[min_store,5]
                    # min_duration = every store in partial solution going to every store remaining and back to next store in solution
                    # ( -1 accounts for dataframe feature : double check)
                    #min_duration[i,j] = durations[route[i]-1, cluster[j]-1] + durations[route[i+1]-1, cluster[j]-1]
                    # Time from node in cluster back to next node or the origin

            # Find minimum combo in this array so can find associated store, add to route ( in correct spot depending on which node from then increment time and pallets (back time)
            #min_index = divmod(min_duration.argmin(), min_duration.shape[1])        
            #route.append(cluster[min_index[0]]) # Extracts row of min index which is the route that adds the least time 
            #time += min_duration[min_duration[min_index[0]], min_duration[min_index[1]]] + 7.5     # Adding time of third added node   
            #pallets += North[cluster[min_index[0]], 5]
            #cluster.pop(route[min_index[0]]) # Remove the last appended node from cluster
            # Cluster still has 1 store in it (for sets of 3)

            # Check where the next store should be inserted into route list
        
            for v in range(len(route)):
                temp_route = route # takes a copy 
                # Find min duration to node still in cluster
                for u in range(len(cluster)): # Start at 1 because the first element has been checked
                    #Checking each i
                    min_duration_temp = durations[route[v]-2, cluster[u]+1] + durations[cluster[u]-2, route[v+1]+1] # Both directions
                    # Recording if best time
                    if(v==0):
                        min_duration_best = min_duration_temp
                        store_ID = cluster[u]
                    elif(min_duration_temp < min_duration_best):
                        min_duration_best = min_duration_temp
                        store_ID = cluster[u]
                        
            
                # Insert best new node into array  
                temp_route.insert(v+1,store_ID)
                # Calculating total route time with this insertion point
                temp_time = time + min_duration_best + 7.5
                temp_pallets = pallets
                
                # Output arrays
                if(v==0):
                    routeMatrix[k] = temp_route
                    timeArray.append(temp_time)
                    pallets = pallets_temp + region[store_ID,5]
                elif(temp_time<timeArray[k]):
                    routeMatrix[k] = temp_route
                    timeArray[k] = temp_time
                    pallets = pallets_temp + region[store_ID,5]
            


       
                
print(routeMatrix)




    
    


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



