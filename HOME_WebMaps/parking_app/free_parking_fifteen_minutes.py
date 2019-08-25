"""
something
"""
import requests
import json


def free_15_minutes_parking():
    send_url = "https://services1.arcgis.com/cNVyNtjGVZybOQWZ/arcgis/rest/services/Free_15_minute_parking/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    full_list = geo_json['features']
    return full_list

