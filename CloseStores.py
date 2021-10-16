import pandas as pd
import numpy as np
from SolveLP_Copy import solveLP
from GenerateRoutes import generate_route_sets
import math

def Closing (Weekday):
        
    # List of store pairs we consider closing
    ClosingStores = [['Countdown Manukau', 'Countdown Manukau Mall'],
                    ['Countdown Roselands', 'Countdown Papakura'],
                    ['Countdown Roselands', 'SuperValue Papakura'],
                    ['Countdown Papakura', 'SuperValue Papakura'],
                    ['Countdown Aviemore Drive', 'Countdown Highland Park'],
                    ['Countdown Westgate', 'Countdown Northwest']]

    # generates routes and solves LP for weekdays without 2 stores
    # reallocate demand - 0.75 of demand sum for both stores
    # less demand reallocate to the other one
    if Weekday == True:

        for i in ClosingStores:
            data_df = pd.read_csv("Store_Data_Nonzero_GROUPED.csv")
            Store_1_ID = int(data_df[data_df['Store'] == i[0]].index.values)    #gets index of 1st store in pair 
            Store_2_ID = int(data_df[data_df['Store'] == i[1]].index.values)    #gets index of 2nd store in pair

            Store_1_Demand = data_df.iloc[Store_1_ID]['Demand Estimate']
            Store_2_Demand = data_df.iloc[Store_2_ID]['Demand Estimate']
            print(type(Store_1_Demand))
            if Store_1_Demand >= Store_2_Demand:
                #data_df.iloc[Store_1_ID]['Demand Estimate'] = 0.75*(Store_1_Demand + Store_2_Demand)
                data_df.at[Store_1_ID, 'Demand Estimate'] = math.ceil(Store_1_Demand + 0.5*Store_2_Demand)
                data_df = data_df.drop(Store_2_ID)
            else:
                #data_df.iloc[Store_2_ID]['Demand Estimate'] = 0.75*(Store_1_Demand + Store_2_Demand)
                data_df.at[Store_2_ID,'Demand Estimate'] = math.ceil(Store_2_Demand + 0.5*Store_1_Demand)
                data_df = data_df.drop(Store_1_ID)                    #deletes the store row with lowest demand from data
                
            data_df.to_csv('Store_Data_Nonzero_Closing.csv', index = False)

            generate_route_sets(True, "Weekday", closing = True)                #generates routes without the pair of stores

            solveLP(Weekday = True, closing = True)                             #solves LP with the new routes generated

    # generates routes and solves LP for weekends without 2 stores
    elif Weekday == False:

        for i in ClosingStores:
            data_df = pd.read_csv("Store_Data_Some_zero_GROUPED.csv")
            Store_1_ID = int(data_df[data_df['Store'] == i[0]].index.values)    #gets index of 1st store in pair 
            Store_2_ID = int(data_df[data_df['Store'] == i[1]].index.values)    #gets index of 2nd store in pair 

            data_df = data_df.drop([Store_1_ID, Store_2_ID])                    #deletes those 2 store's corresponding rows from data

            data_df.to_csv('Store_Data_Some_zero_Closing.csv')

            generate_route_sets(False, "Weekend", closing = True)               #generates routes without the pair of stores

            solveLP(Weekday = False, closing = True)                            #solves LP with the new routes generated
        


if __name__ == "__main__":

    Closing(Weekday = True)
    #Closing(Weekday = False)
