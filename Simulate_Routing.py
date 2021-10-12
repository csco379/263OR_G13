import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Simulate_Demands_Functions import *
from Simulate_Traffic import *

##############################################################################################
# This script simulates the supermarket routing problem, using the optimal set of routes
# generated in the linear program (for uncertain demands and traffic/duration times)
##############################################################################################

if __name__ == "__main__":

    # Set the random seed
    np.random.seed(44)

    # Set number of trials
    n = 10

    # Store cost parameter data
    Cost_Parameters = {'NumTrucks' : 30, 
                   'TruckPallets' : 26,
                   'AverageRouteTime' : 14400,
                   'TruckHourlyCost' : 225,
                   'ExtraTruckTime' : 275,
                   'TruckShift' : 14400,
                   'ExtraTimeCost' : 11/144,
                   'WetLeasedCost' : 2000,
                   'MaxRouteTime' : 18000}

    # Read in the routes used in the optimal solution (output from SolveLP.py)
    weekday_route_data = np.loadtxt(open("RouteStores_Weekday.csv"), delimiter=",", skiprows=0)
    saturday_route_data = np.loadtxt(open("RouteStores_Weekend.csv"), delimiter=",", skiprows=0)
    weekday_routes_used = list(np.loadtxt(open('RouteVector_Weekday.csv'), delimiter = ',', skiprows=0))
    saturday_routes_used = list(np.loadtxt(open('RouteVector_Weekend.csv'), delimiter = ',', skiprows=0))

    # Get number of routes used in each case
    n_routes_weekday = np.shape(weekday_route_data)[0]
    n_routes_saturday = np.shape(saturday_route_data)[0]

    # Initialise lists of results
    weekday_costs = np.zeros(n)         # Total operting cost for 1 day
    saturday_costs = np.zeros(n)
    weekday_trucks =np.zeros(n)         # Number of normal trucks utilised in 1 day
    saturday_trucks = np.zeros(n)
    weekday_rental = np.zeros(n)        # Number of 4-hour rental periods purchased
    saturday_rental = np.zeros(n)


    # Loop through trials
    for i in range(n):

        # Simulate demands and route times
        weekday_stores_demands, saturday_stores_demands = BootstrapDemands()
        weekday_route_demands, saturday_route_demands = Obtain_Simulated_Route_Demands(weekday_routes_used, saturday_routes_used, weekday_stores_demands, saturday_stores_demands)
        weekday_route_durations, saturday_route_durations = trafficSimulation("Route_Times_Weekday.csv", "Route_Times_Weekend.csv")

        # Get the times of the actual routes used
        weekday_route_times = [weekday_route_durations[int(i)] for i in weekday_routes_used]
        saturday_route_times = [saturday_route_durations[int(i)] for i in saturday_routes_used]


        ### WEEKDAY ###
        # Initialise costs for this simulate day
        weekday_routing_cost = 0
        weekday_routing_trucks = 0
        weekday_routing_rental_time = 0
        # Loop through each route in the routing plan and add its costs, operations, etc
        for j in range(n_routes_weekday):

            if weekday_route_demands[j] <= 26:
                if weekday_route_times[j] < Cost_Parameters['TruckShift']:
                    weekday_routing_cost += weekday_route_times[j] * Cost_Parameters['TruckHourlyCost']/(60**2)
                else:
                    weekday_routing_cost += (Cost_Parameters['TruckShift'])*(Cost_Parameters['TruckHourlyCost']/(60**2)) + (weekday_route_times[j] - Cost_Parameters['TruckShift']) * (Cost_Parameters['ExtraTruckTime']/(60**2))

                weekday_routing_trucks += 1

            else:
                weekday_routing_rental_time += weekday_route_times[j]

        N_4h_leased = np.ceil(weekday_routing_rental_time/(4*60**2))
        weekday_routing_cost += N_4h_leased * Cost_Parameters['WetLeasedCost']

        # Store weekday cost
        weekday_costs[i] = weekday_routing_cost

        # Store number of trucks used
        weekday_trucks[i] = weekday_routing_trucks

        # Store number of wet-leased 4h periods bought
        weekday_rental[i] = N_4h_leased


        ### WEEKEND ###
        # Initialise costs for this simulate day
        saturday_routing_cost = 0
        saturday_routing_trucks = 0
        saturday_routing_rental_time = 0
        # Loop through each route in the routing plan and add its costs, operations, etc
        for j in range(n_routes_saturday):

            if saturday_route_demands[j] <= 26:
                if saturday_route_times[j] < Cost_Parameters['TruckShift']:
                    saturday_routing_cost += saturday_route_times[j] * Cost_Parameters['TruckHourlyCost']/(60**2)
                else:
                    saturday_routing_cost += (Cost_Parameters['TruckShift'])*(Cost_Parameters['TruckHourlyCost']/(60**2)) + (saturday_route_times[j] - Cost_Parameters['TruckShift']) * (Cost_Parameters['ExtraTruckTime']/(60**2))

                saturday_routing_trucks += 1

            else:
                saturday_routing_rental_time += saturday_route_times[j]

        N_4h_leased = np.ceil(saturday_routing_rental_time/(4*60**2))
        saturday_routing_cost += N_4h_leased * Cost_Parameters['WetLeasedCost']

        # Store weekday cost
        saturday_costs[i] = saturday_routing_cost

        # Store number of trucks used
        saturday_trucks[i] = saturday_routing_trucks

        # Store number of wet-leased 4h periods bought
        saturday_rental[i] = N_4h_leased



    ###   Print/display the results   ###

    plt.figure(1)
    plt.hist(weekday_costs, density=True, histtype='stepfilled', alpha=0.2)

    plt.figure(2)
    plt.hist(saturday_costs, density=True, histtype='stepfilled', alpha=0.2)

    plt.figure(3)
    plt.hist(weekday_trucks, density=True, histtype='stepfilled', alpha=0.2, bins=10)
    plt.hist(saturday_trucks, density=True, histtype='stepfilled', alpha=0.2, bins=10)

    plt.figure(4)
    plt.hist(weekday_rental, density=True, histtype='stepfilled', alpha=0.2, bins=10)
    plt.hist(saturday_rental, density=True, histtype='stepfilled', alpha=0.2, bins=10)


    plt.show()
