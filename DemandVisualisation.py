# Libraries
import numpy as np
from numpy.core.einsumfunc import _einsum_path_dispatcher  #?????
from numpy.lib.nanfunctions import _nanprod_dispatcher
import pandas as pd
import seaborn as sns
import folium


ORSkey = ""
data = pd.read_csv("Store_Data_Some_zero_GROUPED.csv").to_numpy()


coords = data[['Long', 'Lat']]
coords = coords.to_numpy().to_list()

m = folium.Map(location = list(reversed(coords[2])), zoom_start=10)