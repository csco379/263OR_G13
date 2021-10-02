# Generating a subset of feasible routes

# Libraries
import numpy as np
import pandas as pd
from Regions import set_boundary
# Loading in store data

distributionCentre = pd.read_csv("Distribution_Centre_Data.csv")
weekdayData = pd.read_csv("Store_Data_Nonzero.csv")
#print(weekdayData)

# Applying regions
# Which pdf 
weekdayRegions = set_boundary("Store_Data_Nonzero.csv") # ????IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices


# Ideas 
