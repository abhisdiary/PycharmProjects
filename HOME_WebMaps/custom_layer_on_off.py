import folium
import pandas

data = pandas.read_csv("res/Volcanoes.txt")
lat = list(data["LAT"])  # selecting the lat column
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


m = folium.Map(location=[38.58, -99.09], zoom_start=5)
# [latitude, longitude]: latitude values can be -90 to 90 and longitude values can be from -180 to 180

fg_volcanoes = folium.FeatureGroup(name="Show Volcanoes")

html = """
Volcano Name: <br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
# Adding Multiple Marker Using Loop
for lt, ln, el, name in zip(lat, lon, elev, name):
    # for styling add iframe
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    # m.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe, parse_html=True), icon=folium.Icon(color=color_producer(el))))
    fg_volcanoes.add_child(
        folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe, parse_html=True), fill_color=color_producer(el), color='grey',
                            fill=True, fill_opacity=0.7))

fg_population = folium.FeatureGroup(name="Population")
# 3rd Layer
fg_population.add_child(folium.GeoJson(data=(open("res/world.json", "r", encoding="utf-8-sig").read()),
                                       style_function=lambda x: {
                                           'fillColor': 'green' if x['properties']['POP2005'] < 1000000 else 'orange' if 1000000 <= x['properties'][
                                               'POP2005'] < 2000000 else 'red'}))

m.add_child(fg_volcanoes)
m.add_child(fg_population)

m.add_child(folium.LayerControl())

m.save("views/Custom_Layer_On_Off.html")
