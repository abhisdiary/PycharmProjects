import createAddressDataframe
from geopy.geocoders import ArcGIS

nom = ArcGIS(scheme="http")

df = createAddressDataframe.df

geocode0 = nom.geocode("...")
geocode1 = nom.geocode("19 May Street, Sydney, NSW 2122")
print(geocode1)
print(geocode1.latitude)
print(geocode1.longitude)

df["Coordinates"] = df["Full Address"].apply(nom.geocode)
df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x is not None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x is not None else None)
print(df)
