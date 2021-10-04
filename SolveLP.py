import numpy as np
from numpy.core.einsumfunc import _einsum_path_dispatcher
from numpy.lib.nanfunctions import _nanprod_dispatcher
import pandas as pd
import itertools
from Regions import set_boundaries
from pulp import *


# Read in the route matrix, route times and route pallet demands
route_matrix = np.loadtxt(open("Binary_Route_Matrix.csv"), delimiter=",", skiprows=0)
route_time_vector = np.loadtxt(open("Route_Times.csv"), delimiter=",", skiprows=0)
route_pallets_vector = np.loadtxt(open("Route_Pallets.csv"), delimiter=",", skiprows=0)

# Obtain the number of stores and potential routes to use
n_stores, n_routes = np.shape(route_matrix)

# Create a dictionary for the problem costs
Cost_Parameters = {'NumTrucks' : 30, 
                   'TruckPallets' : 26,
                   'AverageRouteTime' : 14400,
                   'TruckHourlyCost' : 225,
                   'TruckShift' : 14400,
                   'ExtraTimeCost' : 11/144,
                   'WetLeasedCost' : 5/9}


#########################################################################################

#Converting the csv file to a list
def csv_to_list(filename , headers = True):
    row = 1
    if headers = False:
        row = 0
    with open(filename, "r") as f:
        data = [row for row in csv.reader(f.read().splitlines())]
        return data[row]

#Loading the data as a list
data = csv_to_list(____, headers = True)

nodes = [str(i) for i in range(1, 67)]

def solve(routeNames, timeArray, routes)

    nodes = [str(i) for i in range(1, __)]    
    demand = np.ones(66)
    demand[DCI] = 0
    cost = np.zeros(len(timeArray))
    print('Finding stores with no demand:', np.where(demand == 0))

    demand = dict(zip(nodes, list(demand)))
    cost = dict(zip(routeNames, cost))

    trucks = 30

    #Cost of sending a truck on a route
    for i in len(timeArray):
        if time[i] <= 14400
            cost[i] = 225 * time[i]/3600
        else:
            cost[i] = 225 * 4 + 275 * ((time[i] - 14400) / 3600)

    #Making the route data to a dictionary
    routes = makeDict([nodes, routeNames], routes, 0)

    #The problem variables for the number of each route
    vars = LpVariable.dicts("Route", routeNames, 0, None, LpInteger)

    #Creating the problem
    prob = LpProblem("Pallet Problem", LpMinimize)

    #Objective function (total no. of routes used * cost of each route)
    prob += lpSum([vars[i] * cost[i] for i in routeNames]), "Cost of Transporting Pallets"

    #Constraint for one route per node
    for i in nodes:
        prob += lpSum([vars[j] * routes[i][j] for j in routeNames]) >= demand[i]

    #Constraint for the number of available trucks
    prob += lpSum([vars[i] for i in routeNames]) <= trucks * 2

    #Writing the problem data to an lp file
    prob.writeLP("PalletProblem.lp")

    #Solving the problem
    prob.solve()

    #Finding the number of trucks
    num_truck = 0
    for v in prob.variables():
        if (v.varValue != 0) and (v.varValue != None):
                num_truck += v.varValue
        
    #Number of trucks used pinted to the screen
    print("Number of Trucks used: ", num_truck)

    #Each of the variables are printed with its resolved optimum value
    for v in prob.variables():
        print(v.name, "=", v.varValue)

    #Optimised objective function value printed to the screen
    print("Cost of Transporting Pallets = $ %.2f" % value(prob.objective))

    #Status of the problem is printed to the screen
    print("Status:", LpStatus[prob.status])