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
df.head()
df['geometry'] = list(zip(df['LONG'], df['LAT'])) 
df['geometry'] = df['geometry'].apply(Point) 
gdf = gpd.GeoDataFrame(df)
gdf = gdf.set_crs("EPSG:4326") 
#gdf.to_file('HistoricGravityPoints.shp') #Creates .shp for use in ArcPro etc

df = pd.read_csv('OSNIAbsoluteGravity.csv')
del df['Easting.1'], df['Northing.1'], df['Unnamed: 8'], df['latitude'], df ['longitude'] #Removal of superflous coloumns
df['geometry'] = list(zip(df['Easting'], df['Northing'])) 
df['geometry'] = df['geometry'].apply(Point) 
gdf = gpd.GeoDataFrame(df)
gdf = gdf.set_crs("EPSG:2157") #Source data is Irish Transverse Mercator, this needs set before we can transform to WGS84
gdf = gdf.to_crs("EPSG:4326") #Transformation to WGS84 for interoperability (https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.to_crs.html)
#gdf.to_file('AbsoluteGravityPoints.shp') #Creates .shp for use in ArcPro etc
