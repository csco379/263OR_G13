# Libraries
import numpy as np
from numpy.core.einsumfunc import _einsum_path_dispatcher  #?????
from numpy.lib.nanfunctions import _nanprod_dispatcher
import pandas as pd
import folium
import openrouteservice as ors
#################################### Region and Store Type Visualisation ####################################
ORSkey = "5b3ce3597851110001cf6248354cfef3acb24131a10df048bf5cddaf"

data = pd.read_csv("Store_Data_Some_zero_GROUPED.csv")

coords = data[['Long', 'Lat']]
coords = coords.to_numpy().tolist()
'''
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
# Add a key for the different icons

    folium.Marker(list(reversed(coords[i])), popup =data.Store[i], icon = folium.Icon(color = iconCol, icon=icon)).add_to(m)
m.save("RegionMap.html")
'''
########################################### Route Visualisation #################################################################

# Import list of routes with which stores are in it as a numpy array
data_nonZero = pd.read_csv("Store_Data_Nonzero_GROUPED.csv")

coords = data_nonZero[['Store', 'Long', 'Lat']]
#coords = coords.to_numpy().tolist()


route = [None]*21
# List of routes used in optimal solution:
route[0] = ["Countdown Mangere Mall"]
route[1]= ["Countdown Botany Downs",  "Countdown Howick",  "Countdown Meadowlands",  "FreshChoice Half Moon Bay"]
route[2] = ["Countdown Birkenhead",  "Countdown Glenfield",  "Countdown Northcote"]
route[3] = ["Countdown Aviemore Drive",  "Countdown Highland Park",  "Countdown Pakuranga"]
route[4] = ["Countdown Meadowbank",  "Countdown St Johns",  "FreshChoice Otahuhu"]
route[5] = ["Countdown Mt Wellington",  "Countdown Sylvia Park"]
route[6] = ["Countdown Blockhouse Bay",  "Countdown Kelston",  "SuperValue Avondale",  "SuperValue Titirangi"]
route[7] = ["Countdown Browns Bay",  "Countdown Mairangi Bay"]
route[8] = ["Countdown Hauraki Corner",  "Countdown Takapuna"]
route[9] = ["Countdown Milford",  "Countdown Sunnynook"]
route[10] = ["Countdown Henderson",  "Countdown Lincoln Road",  "Countdown Lynmall",  "SuperValue Palomino"]
route[11] = ["Countdown Hobsonville",  "Countdown Lynfield",  "Countdown Northwest",  "FreshChoice Ranui"]
route[12] = ["Countdown Te Atatu",  "Countdown Te Atatu South",  "Countdown Westgate",  "FreshChoice Glen Eden"]
route[13] = ["Countdown Airport",  "Countdown Roselands",  "Countdown Takanini",  "SuperValue Papakura"]
route[14] = ["Countdown Mangere East",  "Countdown Manukau Mall",  "Countdown Papatoetoe", " SuperValue Flatbush"]
route[15] = ["Countdown Greenlane ", "Countdown Newmarket",  "Countdown Onehunga",  "Countdown Metro Albert Street"]
route[16] = ["Countdown Grey Lynn",  "Countdown Mt Eden",  "Countdown Ponsonby",  "Countdown Metro Halsey Street"]
route[17] = ["Countdown Grey Lynn Central",  "Countdown Pt Chevalier",  "FreshChoice Mangere Bridge"]
route[18] = ["Countdown Mt Roskill",  "Countdown St Lukes",  "Countdown Three Kings"]
route[19] = ["Countdown Auckland City",  "Countdown Victoria", "Street West"]
route[20] = ["Countdown Manukau",  "Countdown Manurewa",  "Countdown Papakura"]





# Plot each route on a map of Auckland
#Weekday

# Each row is a route 
# If row is not empty (sum != 0) then nodes ordered 0 12 3 
client = ors.Client(key=ORSkey)
routeMapped = []
# 
for i in range (0,len(route)):
    for j in range (1,len(route[i])):
        routeMapped.append( client.directions(coordinates = [coords[route[i][j-1]],coords[route[i][j]]], profile='driving-hgv', formate = 'geojson', validate = False))


routeMap = folium.Map(location=list(reversed(coords[2])), zoom_start=10)
folium.PolyLine(locations = [list(reversed(coords)) for coords in route['features'][0]['geometry']['coordinates']]).add_to(routeMap)


#Weekend



########################################### Demand Visualisation ############################################

'''

import seaborn as sns
import matplotlib.pyplot as plt ###???

# Seperate the data into regions 
North = data.loc[data["Region"]=='North']
South = data.loc[data["Region"]=='South']
East = data.loc[data["Region"]=='East']
West = data.loc[data["Region"]=='West']
Central= data.loc[data["Region"]=='Central']

# Import data for different day types
data_someZero = data
data_nonZero = pd.read_csv("Store_Data_Nonzero_GROUPED.csv")


# Some 0 data
fig = plt.figure()
plt.title("Saturday Demand Estimation")
# North 
ax1 = fig.add_subplot(2,3,1, xlabel="North Region")
#ax1 = plt.subplot(111)
sns.barplot(x="Store", y="Demand Estimate", hue="Store", data= North, ax=ax1, palette= "viridis")
ax1.axes.xaxis.set_visible(False)
ax1.legend(loc='right')
# South
ax2 = fig.add_subplot(2,3,2, xlabel="South Region")
#ax2 = plt.subplot(112)
sns.barplot(x="Store", y="Demand Estimate", hue="Store", data= South, ax=ax2,  palette= "flare")
ax2.axes.xaxis.set_visible(False)
ax2.axes.yaxis.set_visible(False)
ax2.legend(loc='right')
# East 
ax3 = fig.add_subplot(2,3,3, xlabel="East Region")
#ax3 = plt.subplot(113, sharey= 121)
sns.barplot(x="Store", y="Demand Estimate", hue="Store", data= East, ax=ax3,  palette= "icefire")
ax3.axes.xaxis.set_visible(False)
ax3.axes.yaxis.set_visible(False)
ax3.legend(loc='right')
# West
ax4 = fig.add_subplot(2,3,4, xlabel="West Region Stores")
#ax4 = plt.subplot(211)
sns.barplot(x="Store", y="Demand Estimate", hue="Store", data= West, ax=ax4,  palette= "pastel")
ax4.axes.xaxis.set_visible(False)
ax4.axes.yaxis.set_visible(False)
ax4.legend(loc='right')
# Central 
ax5 = fig.add_subplot(2,3,5, xlabel="Central Region Stores")
#ax5 = plt.subplot(212)
sns.barplot(x="Store", y="Demand Estimate", hue="Store", data= Central, ax=ax5,  palette= "YlOrRd")
ax5.axes.xaxis.set_visible(False)
ax5.axes.yaxis.set_visible(False)
ax5.legend(loc='right')


plt.close(2)
plt.close(3)
#plt.tight_layout()
# No 0 data
fig2 = plt.figure()


#f, ax = plt.subplots(1, 2, sharex=False)

#sns.displot(data_someZero, x= "Store", y= "Demand", col= "Region", ax= ax[0])

#sns.displot(data_nonZero, x= "Store", y= "Demand", col= "Region", ax=ax[1] )
# Removing distribution centre for demand estimation plot
#data_someZero.drop(index= 55, axis=0, inplace=True)

g = sns.catplot(x= "Region", y= "Demand Estimate", hue="Store", kind="bar", data =data_someZero, dodge=True, col="Region", col_wrap=3, sharex=False, palette=sns.color_palette("rocket"), )
for axes in g.axes.ravel():
    axes.legend()
#g.axes.ravel()
plt.show()




plt.show()
'''