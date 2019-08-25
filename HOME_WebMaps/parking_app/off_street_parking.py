"""
Off Street Parking Script
Data: https://opendata.transport.nsw.gov.au/dataset/street-parking
"""

import folium
import pandas

fg_off_street_parking = folium.FeatureGroup(name="Show Off Street Parking")


def off_street_parking():
    df = pandas.read_json("res/OffstreetparkingData.geojson")
    for item in df['features']:
        details = "Owner: " + item['properties']['Owner'] + "<br>" + "Building Name: " + item['properties']['Building_name_location'] + "<br>"
        iframe_off_street_parking = folium.IFrame(html=details, width=200, height=100)
        fg_off_street_parking.add_child(
            folium.Marker(location=[item['geometry']['coordinates'][1], item['geometry']['coordinates'][0]],
                          popup=folium.Popup(iframe_off_street_parking, parse_html=True),
                          icon=folium.Icon(color="beige")))
