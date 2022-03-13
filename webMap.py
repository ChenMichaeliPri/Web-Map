
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

barsNames = list(barsData["BARS"])
barsLats = list(barsData["LAT"])
barsLons = list(barsData["LON"])
barsLink = list(barsData["LINK"])

# Adding layers to the Map
fgRest = folium.FeatureGroup(name="Restaurants")

for rest, lt, ln, link in zip(restNames, restLats, restLons, restLink):
    fgRest.add_child(folium.Marker(location=[lt, ln], popup=("<a href="+link+">"+rest+" </a>"), tooltip=rest, icon=folium.Icon(color='purple')))

webMap.add_child(fgRest)

fgBars = folium.FeatureGroup(name="Bars")

for bar, lt, ln, link in zip(barsNames, barsLats, barsLons, barsLink):
    fgBars.add_child(folium.Marker(location=[lt, ln], popup=("<a href="+link+">"+bar+"</a>"), tooltip=bar, icon=folium.Icon(color='orange')))

webMap.add_child(fgBars)

# Saving as html file
webMap.save("webMap.html")
