# Libraries
import numpy as np
from numpy.core.einsumfunc import _einsum_path_dispatcher  #?????
from numpy.lib.nanfunctions import _nanprod_dispatcher
import pandas as pd
import folium

#################################### Region and Store Type Visualisation ####################################
ORSkey = "5b3ce3597851110001cf6248354cfef3acb24131a10df048bf5cddaf"

data = pd.read_csv("Store_Data_Some_zero_GROUPED.csv")

coords = data[['Long', 'Lat']]
coords = coords.to_numpy().tolist()

m = folium.Map(location = list(reversed(coords[2])), zoom_start=10)

for i in range(0, len(coords)):
    if data.Region[i]== "North":
        iconCol = "green"
    elif data.Region[i]== "South":
        iconCol = "cadetblue"
    elif data.Region[i]== "East":
        iconCol = "lightred"
    elif data.Region[i]== "West":
        iconCol = "darkblue"
    elif data.Region[i]== "Central":
        iconCol = "purple"

    if  "Countdown" in data.Store[i]:
        icon = "cloud"
    elif "FreshChoice" in data.Store[i]:
        icon = "tag"
    elif "SuperValue" in data.Store[i]:
        icon = "map-piin"
    elif "Distribution" in data.Store[i]:
        icon = "certificate"


    folium.Marker(list(reversed(coords[i])), popup =data.Store[i], icon = folium.Icon(color = iconCol, icon=icon)).add_to(m)
m

############################################################################################################


# Demand Visualisation

import seaborn as sns
import matplotlib.pyplot as plt
# Import data for different day types
data_someZero = data
data_nonZero = pd.read_csv("Store_Data_Nonzero_GROUPED.csv")

ax = plt.subplots(1, 2, sharey=True)

sns.displot(data_someZero, x= "Store", y= "Demand", col= "Region", ax= ax[0])

sns.displot(data_nonZero, x= "Store", y= "Demand", col= "Region", ax=ax[1] )
