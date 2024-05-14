# ---------------------------------------------------------------------------------------------------------------------
# The following imports the packages used
# ---------------------------------------------------------------------------------------------------------------------

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import folium

# ---------------------------------------------------------------------------------------------------------------------
# Preparation of source data
# ---------------------------------------------------------------------------------------------------------------------

df = pd.read_csv('Ulst6Jan87.csv') #historic gravity data
HistGravData = gpd.GeoDataFrame(df[['id', 'OBS (mgal)']], #Keep only the ID and the reading in milligals.
                            geometry=gpd.points_from_xy(df['LONG'], df['LAT']),crs='epsg:4326') 

#HistGravData.to_file('HistoricGravityPoints.shp') #Creates .shp for use in ArcPro etc

df = pd.read_csv('OSNIAbsoluteGravity.csv') #Absolute Gravity Data
HistGravData = gpd.GeoDataFrame(df[['Station Name'], #Keep only Station Name
                            geometry=gpd.points_from_xy(df['Easting'], df['Northing']),crs='epsg:2157') #Source data is Irish Transverse Mercator

AbsGravData.to_crs ("EPSG:4326") #Transformation to WGS84 for interoperability (https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.to_crs.html)

#AbsGravData.to_file('AbsoluteGravityPoints.shp') #Creates .shp for use in ArcPro etc


