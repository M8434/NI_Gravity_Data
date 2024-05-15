# ---------------------------------------------------------------------------------------------------------------------
# The following imports the packages used
# ---------------------------------------------------------------------------------------------------------------------

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import folium

# ---------------------------------------------------------------------------------------------------------------------
# Preparation of input data
# ---------------------------------------------------------------------------------------------------------------------

df = pd.read_csv('Ulst6Jan87.csv') #historic gravity data
Hist = gpd.GeoDataFrame(df[['id', 'OBS (mgal)']], #Keep only the ID and the reading in milligals.
                            geometry=gpd.points_from_xy(df['LONG'], df['LAT']),crs='epsg:4326') #OpenStreetMap

Hist.to_crs("EPSG:4326")
Hist.to_file('HistGravData.shp',crs='EPSG:4326') #specified crs as by default it was creating .shp with source CRS

df = pd.read_csv('OSNIAbsoluteGravity.csv') #Absolute Gravity Data
Absolute = gpd.GeoDataFrame(df[['Station Name','GNSS Observation Date']], #Keep only Station Name
                            geometry=gpd.points_from_xy(df['LONG'], df['LAT']),crs='epsg:4326')
Absolute.rename(columns={'Station Name': 'Station', 'GNSS Observation Date': 'ObDate'}, inplace=True) #Current column names too long for .shp
Absolute.to_crs('EPSG:29902')
Absolute.to_file('AbsGravData.shp',crs='EPSG:29902')
# ---------------------------------------------------------------------------------------------------------------------
# Spatial Analysis to identify historic gravity points within 5km of Absolute Gravity Point
# ---------------------------------------------------------------------------------------------------------------------

AbsGravData = gpd.read_file('AbsGravData.shp')
ABbuffer = AbsGravData.buffer(0.1) #Figure represents 10km #Figure represents 10km. Need to buffer on .shp as CRS is projected
ABbuffer.to_crs('EPSG:4326')
ABbuffer.to_file('AB_buffer.shp',crs='EPSG:4326') 
ABbuffer = gpd.read_file('AB_buffer.shp')

CombinedBuffer = ABbuffer.geometry.unary_union #Created to simplify process
within_CombinedBuffer = Hist1[Hist1.geometry.within(CombinedBuffer)]
within_CombinedBuffer.to_file('HistGrav10km_within_AbsoluteGrav.shp',crs='EPSG:4326')
# ---------------------------------------------------------------------------------------------------------------------
# Configuration of basic Folium Map
# ---------------------------------------------------------------------------------------------------------------------

m = AbsGravData.explore('Station Name',marker_type='marker', popup=True, legend=False, tiles= "cartodb positron")

AB_buffer.explore(m=m, popup=False, fill_color = "White",)

within_CombinedBuffer.explore(m=m, popup=True, legend=False,)

m

