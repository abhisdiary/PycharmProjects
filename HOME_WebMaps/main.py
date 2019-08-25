import folium

m = folium.Map(location=[-33.8706057, 150.9669528], zoom_start=12)
# [latitude, longitude]: latitude values can be -90 to 90 and longitude values can be from -180 to 180

fg = folium.FeatureGroup(name="My Map Features")

# Adding Multiple Marker Using Loop
for coordinates in [[-33.788908, 151.084973], [-33.789851, 151.082480]]:
    m.add_child(folium.Marker(location=coordinates, popup="Home", icon=folium.Icon(color="blue")))

m.add_child(fg)
m.save("views/Map1.html")

m = folium.Map(location=[-90, -180], zoom_start=6)
help(folium.Map)
