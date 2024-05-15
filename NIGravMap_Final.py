# ---------------------------------------------------------------------------------------------------------------------
# The following imports the packages used
# ---------------------------------------------------------------------------------------------------------------------

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import folium
import io
from PIL import Image


# ---------------------------------------------------------------------------------------------------------------------
# Preparation of input data
# ---------------------------------------------------------------------------------------------------------------------

df = pd.read_csv('Ulst6Jan87.csv') #historic gravity data
HistGravData = gpd.GeoDataFrame(df[['id', 'OBS (mgal)']], #Keep only the ID and the reading in milligals.
                            geometry=gpd.points_from_xy(df['LONG'], df['LAT']),crs='epsg:4326') 
HistGravData.to_crs("EPSG:4326")
HistGravData.to_file('Hist.shp',crs='EPSG:4326') #specified crs as by default it was creating .shp with source CRS


df = pd.read_csv('OSNIAbsoluteGravity.csv') #Absolute Gravity Data
AbsGravData = gpd.GeoDataFrame(df['Station Name'], #Keep only Station Name
                            geometry=gpd.points_from_xy(df['LONG'], df['LAT']),crs='epsg:4326') 
AbsGravData.to_file('AbData.shp',crs='EPSG:4326') #Will throw UserWarning about column name length, this is OK - **future dev work**

# ---------------------------------------------------------------------------------------------------------------------
# Spatial Analysis to identify historic gravity points within 5km of absolute gravity point
# ---------------------------------------------------------------------------------------------------------------------

Hist1 = gpd.read_file('Hist.shp')
AbData = gpd.read_file('AbData.shp')
ABbuffer = AbData.buffer(0.1) #Figure represents 10km
ABbuffer.to_file('AB_buffer.shp',crs='EPSG:4326') 
AB_buffer = gpd.read_file('AB_buffer.shp')
AB_buffer.to_crs('EPSG:4326')
CombinedBuffer = AB_buffer.geometry.unary_union
within_CombinedBuffer = Hist1[Hist1.geometry.within(CombinedBuffer)]
within_CombinedBuffer.head()
within_CombinedBuffer.to_file('withincombined.shp',crs='EPSG:4326')

# ---------------------------------------------------------------------------------------------------------------------
# Configuration of Folium Map
# ---------------------------------------------------------------------------------------------------------------------

m = folium.Map(tiles=None)

AbsGravData.explore(m=m, 'Station Name',marker_type='marker', popup=True, legend=False,)

AB_buffer.explore(m=m, popup=False, fill_color = "White", legend_name = "10k buffer of Absolute Gravity Stations",)

within_CombinedBuffer.explore(m=m, popup=True, legend=False,)

m

