
# Web Map of loved Restaurants and Bars in Tel Aviv
import folium
import pandas

# Base layer of the map
webMap = folium.Map(location=[32.063330, 34.772446], zoom_start=16)

# Loading the data for the map from CSV files
restaurantsData = pandas.read_csv("Restaurants.csv")
barsData = pandas.read_csv("Bars.csv")

# Extracting relevent data
restNames = list(restaurantsData["RESTAURANT"])
restLats = list(restaurantsData["LAT"])
restLons = list(restaurantsData["LON"])
restLink = list(restaurantsData["LINK"])

barsNames = list(restaurantsData["BARS"])
barsLats = list(restaurantsData["LAT"])
barsLons = list(restaurantsData["LON"])
barsLink = list(restaurantsData["LINK"])

# Saving as html file
webMap.save("webMap.html")
