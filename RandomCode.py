import numpy as np
import pandas as pd
import itertools
from pulp import *

route_matrix = np.loadtxt(open("Binary_Route_Matrix.csv"), delimiter=",", skiprows=0)
route_time_vector = np.loadtxt(open("Route_Times.csv"), delimiter=",", skiprows=0)
route_pallets_vector = np.loadtxt(open("Route_Pallets.csv"), delimiter=",", skiprows=0)

# Obtain the number of stores and potential routes to use
n_stores, n_routes = np.shape(route_matrix)

#print(n_stores, n_routes)

durations = pd.read_csv("WoolworthsTravelDurations.csv").to_numpy()

store1index = 2
store2index = 4
print(durations[2,4+1])




