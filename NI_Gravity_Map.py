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

#create point feature from Absolute Gravity data csv
df = pd.read_csv('OSNI Absolute Gravity Station Coords + Heights.csv')

#Lat long to decimal
df['Lat'] = df['latitude']
N = 'N' in latitude
d, m, s = map(float, latitude[:-1].split('-'))
latitude = (d + m / 60. + s / 3600.) * (1 if N else -1)



Historic_Gravity = gpd.GeoDataFrame(df[['id', 'OBS (mgal)']], # Only display the ID for each point along with the gravity value in Milligal
                            geometry=gpd.points_from_xy(df['LONG'], df['']), # set the geometry using points_from_xy
                            crs='epsg:4326') # set CRS as WGS84 lat/lon





latitude = "20-55-70.010N"
N = 'N' in latitude
d, m, s = map(float, latitude[:-1].split('-'))
latitude = (d + m / 60. + s / 3600.) * (1 if N else -1)
longitude = "32-11-50.000W"
W = 'W' in longitude
d, m, s = map(float, longitude[:-1].split('-'))
longitude = (d + m / 60. + s / 3600.) * (-1 if W else 1)# ---------------------------------------------------------------------------------------------------------------------
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

#create point feature from Absolute Gravity data csv
df = pd.read_csv('OSNI Absolute Gravity Station Coords + Heights.csv')

#Lat long to decimal
df['Lat'] = df['latitude']
N = 'N' in latitude
d, m, s = map(float, latitude[:-1].split('-'))
latitude = (d + m / 60. + s / 3600.) * (1 if N else -1)



Historic_Gravity = gpd.GeoDataFrame(df[['id', 'OBS (mgal)']], # Only display the ID for each point along with the gravity value in Milligal
                            geometry=gpd.points_from_xy(df['LONG'], df['']), # set the geometry using points_from_xy
                            crs='epsg:4326') # set CRS as WGS84 lat/lon





latitude = "20-55-70.010N"
N = 'N' in latitude
d, m, s = map(float, latitude[:-1].split('-'))
latitude = (d + m / 60. + s / 3600.) * (1 if N else -1)
longitude = "32-11-50.000W"
W = 'W' in longitude
d, m, s = map(float, longitude[:-1].split('-'))
longitude = (d + m / 60. + s / 3600.) * (-1 if W else 1)