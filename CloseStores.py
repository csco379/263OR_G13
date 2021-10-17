import pandas as pd
import numpy as np
from SolveLP_Closing import solveLP
from Simulate_Routing import SimulateCosts
from GenerateRoutes import generate_route_sets
import math

def Closing():
        
    # List of store pairs we consider closing
    ClosingStores = [['Countdown Manukau', 'Countdown Manukau Mall'],
                    ['Countdown Roselands', 'Countdown Papakura'],
                    ['Countdown Roselands', 'SuperValue Papakura'],
                    ['Countdown Papakura', 'SuperValue Papakura'],
                    ['Countdown Aviemore Drive', 'Countdown Highland Park'],
                    ['Countdown Westgate', 'Countdown Northwest']]
    
    # generates routes and solves LP for weekdays without  the store with lower demand
    # reallocates demand - 50% of demand from store with lower demand added to store with higher demand

    for i in ClosingStores:
        data_df = pd.read_csv("Store_Data_Nonzero_GROUPED.csv")
        Store_1_ID = int(data_df[data_df['Store'] == i[0]].index.values)    #gets index of 1st store in pair 
        Store_2_ID = int(data_df[data_df['Store'] == i[1]].index.values)    #gets index of 2nd store in pair

        Store_1_Demand = data_df.iloc[Store_1_ID]['Demand Estimate']        #gets demand of 1st store in pair
        Store_2_Demand = data_df.iloc[Store_2_ID]['Demand Estimate']        #gets demand of 2nd store in pair

        #finds the store with lower demand and reallocates demand to other store
        #lower demand store assigned to closing_store variable for input into SolveLP_Closing function
        if Store_1_Demand >= Store_2_Demand:
            data_df.at[Store_1_ID, 'Demand Estimate'] = math.ceil(Store_1_Demand + 0.5*Store_2_Demand)
            data_df.at[Store_2_ID, 'Demand Estimate'] = 0
            closing_store = data_df.iloc[Store_2_ID]['Store']
        else:
            data_df.at[Store_2_ID,'Demand Estimate'] = math.ceil(Store_2_Demand + 0.5*Store_1_Demand)
            data_df.at[Store_1_ID,'Demand Estimate'] = 0
            closing_store = data_df.iloc[Store_1_ID]['Store']
        
        data_df.to_csv('Store_Data_Nonzero_Closing.csv', index = False)
        data_df.to_csv('Store_Data_Some_zero_Closing.csv', index = False)
        generate_route_sets(True, "Weekday", closing = True)                            #generates routes with the new csv file
        generate_route_sets(False, "Weekend", closing = True)

        solveLP(Weekday = True, closing = True, closing_store = closing_store)          #solves LP with the new routes generated
        solveLP(Weekday = False, closing = True, closing_store = closing_store)

if __name__ == "__main__":

    ### UNCOMMENT TO RUN ###
    # Closing()

    if True:
        # Hard coded simulation of routing costs with the 'best' store removed
        # Countdown Papakura removed - it's demand has been accounted for in that of Countdown Roselands

        # Process data
        data_df = pd.read_csv("Store_Data_Nonzero_GROUPED.csv")
        Store_1_ID = int(data_df[data_df['Store'] == 'Countdown Roselands'].index.values)    #gets index of 1st store in pair 
        Store_2_ID = int(data_df[data_df['Store'] == 'Countdown Papakura'].index.values)     #gets index of 2nd store in pair
        Store_1_Demand = data_df.iloc[Store_1_ID]['Demand Estimate']
        Store_2_Demand = data_df.iloc[Store_2_ID]['Demand Estimate']
        if Store_1_Demand >= Store_2_Demand:
            data_df.at[Store_1_ID, 'Demand Estimate'] = math.ceil(Store_1_Demand + 0.5*Store_2_Demand)
            closing_store = data_df.iloc[Store_2_ID]['Store']
        else:
            data_df.at[Store_2_ID,'Demand Estimate'] = math.ceil(Store_2_Demand + 0.5*Store_1_Demand)
            closing_store = data_df.iloc[Store_1_ID]['Store']                    

        # Store new data in files
        data_df.to_csv('Store_Data_Nonzero_Closing.csv', index = False)
        data_df.to_csv('Store_Data_Some_zero_Closing.csv', index = False)

        # Regenerate routes
        generate_route_sets(True, "Weekday", closing = True)                
        generate_route_sets(True, "Weekend", closing = True)

        # Solve for the routes used
        solveLP(Weekday = True, closing = True, closing_store = 'Countdown Papakura')           #solves LP with the new routes generated
        solveLP(Weekday = False, closing = True, closing_store = 'Countdown Papakura')

        # Simulate the routing costs
        SimulateCosts(closing = True, plot = True)
