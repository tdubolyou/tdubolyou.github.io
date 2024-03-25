import os, pandas as pd, geopandas as gpd, requests, folium
from bs4 import BeautifulSoup

# URL of the GeoJSON data
url = "https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Major_Crime_Indicators_Open_Data/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"

# Fetch the data
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Load the data into a GeoDataFrame
    gdf = gpd.GeoDataFrame.from_features(data)

    #Display the first few rows of the GeoDataFrame to understand its structure
    print(gdf.info())

    # Summary statistics for numeric columns
    # print(gdf.describe())

    # Count of different crime types, replace 'MCI' with the actual column name if different
    if 'MCI_CATEGORY' in gdf.columns:
        print(gdf['MCI_CATEGORY'].value_counts())
    else:
        print("Column for crime types not found")

    gdf.to_file("data/data_simple_fetch.geojson", driver='GeoJSON')
else:
    print("Failed to fetch data")

