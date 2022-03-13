
# Web Map of loved Restaurants and Bars in Tel Aviv
import folium

# Base layer of the map
webMap = folium.Map(location=[32.063330, 34.772446], zoom_start=16)

# Saving as html file
webMap.save("webMap.html")
