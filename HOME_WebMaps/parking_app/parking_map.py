"""
parking data link: https://data.cityofsydney.nsw.gov.au/datasets/parking-meters?geometry=151.183%2C-33.885%2C151.245%2C-33.872

"""

import json

import folium
import pandas
import requests
import parking_app.free_parking_fifteen_minutes as f_15_m_p
import parking_app.off_street_parking as o_s_p


def my_location():
    send_url = "http://api.ipstack.com/check?access_key=9124ce11224f6307e356bc65f5da2f5d"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    city = geo_json['city']
    return [latitude, longitude]


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# Step 1: Load the Map
m = folium.Map(location=my_location(), zoom_start=15)

# Step 2: Load your current location
fg_current_location = folium.FeatureGroup(name="Your Location")
iframe_current_location = folium.IFrame(html="Your Current Location", width=200, height=100)
fg_current_location.add_child(
    folium.CircleMarker(location=my_location(), radius=6, popup=folium.Popup(iframe_current_location, parse_html=True), fill_color='blue', color='white',
                        fill=True, fill_opacity=0.7))

# Step 3: Load 15 Minutes Free Parking Data
fg_15_m_f_p = folium.FeatureGroup(name="Free Parking for 15 Minutes")
for item in f_15_m_p.free_15_minutes_parking():
    iframe_f_for_15_minutes = folium.IFrame(
        html=str(item['attributes']['OBJECTID']) + " " + item['attributes']['Street'] + ", " + item['attributes']['Suburb'], width=200, height=100)
    for coordinate in item['geometry']['rings'][0]:
        fg_15_m_f_p.add_child(
            folium.Marker(location=[coordinate[1], coordinate[0]], popup=folium.Popup(iframe_f_for_15_minutes, parse_html=True), icon=folium.Icon(color="orange")))

# Step 4: Load Paid Paid Parking Data
fg_paid_parking = folium.FeatureGroup(name="Show Paid Parking")
iframe_paid_parking = folium.IFrame(html="Paid Parking", width=200, height=100)

df = pandas.read_json("res/Parking_meters.geojson")
# print(df['features'][0]['geometry']['coordinates'])

for coordinate in df['features']:
    # print(coordinate['geometry']['coordinates'])
    fg_paid_parking.add_child(
        folium.Marker(location=[coordinate['geometry']['coordinates'][1], coordinate['geometry']['coordinates'][0]], radius=6,
                      popup=folium.Popup(iframe_paid_parking, parse_html=True), icon=folium.Icon(color="blue")))

# Step 5: Load off Street Parking Data
o_s_p.off_street_parking()

m.add_child(fg_current_location)
m.add_child(fg_15_m_f_p)
m.add_child(fg_paid_parking)
m.add_child(o_s_p.fg_off_street_parking)

m.add_child(folium.LayerControl())

m.save("views/Parking_Map.html")
