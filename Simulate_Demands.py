import numpy as np
import pandas as pd
import random

#######################################################################################
###             This script simulates the store demands via bootstrapping           ###
#######################################################################################

def BootstrapDemands():

    # Read in data files
    Demand_file = pd.read_csv("WoolworthsDemands.csv")
    Stores_data = pd.read_csv("Store_Data_Nonzero_GROUPED.csv")
    Stores_data_zero = pd.read_csv("Store_Data_Some_zero_GROUPED.csv")

    # Get number of stores and days
    n_stores, n_days = np.shape(Demand_file)

    # Loop through stores and bootstrap demand for each
    for i in range(n_stores):

        # Get store data
        storename = Demand_file['Store'].iloc[i]
        store_data = Demand_file.loc[Demand_file['Store'] == storename]
        store_demands = store_data.iloc[0, 1:].values.tolist()

        # Sort the list of demands and remove extreme values (min and max)
        store_demands.sort()
        store_demands = store_demands[1:-1]
        nonzero_demands = [value for value in store_demands if value != 0]

        # Sample store demand from empirical distribution
        sampled = random.choice(nonzero_demands)

        # Store in the data frame
        storeindex = Stores_data.index[Stores_data.Store == storename]
        Stores_data.at[storeindex, 'Demand Estimate'] = sampled

        if ("Countdown" in storename) and ("Metro" not in storename):
            Stores_data_zero.at[storeindex, 'Demand Estimate'] = sampled

    # Extract just the list of demands


    # Export to file
    #Stores_data.to_csv("Simulated_Demands_Nonzero.csv", index = False)
    # Stores_data_zero.to_csv("Simulated_Demands_Some_zero.csv", index = False)

    # Return the arrays
    return Stores_data, Stores_data_zero
