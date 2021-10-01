import numpy as np
import pandas as pd

def set_boundary(filename):

    location_df = pd.read_csv("WoolworthsLocations.csv")
    stores_df = pd.read_csv(filename)
    stores_df["Region"] = ""
    loc_len = len(stores_df.index)
    
    DC_index = int(location_df[location_df['Store']=='Distribution Centre Auckland'].index.values)
    CD_Birkenhead = int(location_df[location_df['Store']=='Countdown Birkenhead'].index.values)
    CDMetro_ASt = int(location_df[location_df['Store']=='Countdown Metro Albert Street'].index.values)
    CD_PtChev = int(location_df[location_df['Store']=='Countdown Pt Chevalier'].index.values)

    DC_lat = location_df.loc[DC_index]['Lat']
    DC_long = location_df.loc[DC_index]['Long']
    CD_Birkenhead_lat = location_df.loc[CD_Birkenhead]['Lat']
    CD_Birkenhead_long = location_df.loc[CD_Birkenhead]['Long']
    #CDMetro_ASt_lat = location_df.loc[CDMetro_ASt]['Lat']
    CDMetro_ASt_long = location_df.loc[CDMetro_ASt]['Long']
    CD_PtChev_lat = location_df.loc[CD_PtChev]['Lat']
    #CD_PtChev_long = location_df.loc[CD_PtChev]['Long']

    stores_df.iloc[CD_PtChev, 'Region'] = 'Central'
    stores_df.iloc[CDMetro_ASt, 'Region'] = 'Central'    
    
    for i in range (loc_len):

        store_lat = stores_df.loc[i]['Lat']
        store_long = stores_df.loc[i]['Long']

        if store_long < DC_long:
             stores_df.iloc[i, 'Region'] = 'South'
        
        elif store_lat > DC_lat and store_long > DC_long:
            stores_df.iloc[i, 'Region'] = 'East'
        
        elif store_lat >= CD_Birkenhead_lat and store_long >= CD_Birkenhead_long:
            stores_df.iloc[i, 'Region'] = 'North'

        elif store_long > DC_long and store_long < CDMetro_ASt_long and store_lat < DC_lat and store_lat > CD_PtChev_lat:
            stores_df.iloc[i, 'Region'] = 'Central'
        
        else:
            stores_df.iloc[i, 'Region'] = 'West'

    stores_df.to_csv(filename)


if __name__ == "__main__":

    set_boundary()