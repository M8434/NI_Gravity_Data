# ---------------------------------------------------------------------------------------------------------------------
# The following imports the packages used
# ---------------------------------------------------------------------------------------------------------------------

import pandas as pd
import geopandas as gpd
import folium

#create point feature from Historic Gravity data csv
df = pd.read_csv('Ulst6Jan87.csv')

Historic_Gravity = gpd.GeoDataFrame(df[['id', 'OBS (mgal)']], # Only display the ID for each point along with the gravity value in Milligal
                            geometry=gpd.points_from_xy(df['LONG'], df['']), # set the geometry using points_from_xy
                            crs='epsg:4326') # set CRS as WGS84 lat/lon

AbsoluteGravity= gpd.GeoDataFrame(df[['id', 'OBS (mgal)']], # Only display the ID for each point along with the gravity value in Milligal
    geometry=gpd.points_from_xy(df['Easting'], df['Northing']), # set the geometry using points_from_xy
    gdf = GeoDataFrame(df, geometry=geometry, crs= 29903) #data is Irish Grid
    gdf = gdf.to_crs(4326) # change CRS to WGS84 lat/lon