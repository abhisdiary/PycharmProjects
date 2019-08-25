import csv

from bs4 import BeautifulSoup

with open("index.html", encoding='utf-8') as fp:
    html_doc = fp.read()

soup = BeautifulSoup(html_doc, 'html.parser')
data = soup.find_all("div", class_='product')

# CSV Files
relationsFile = csv.reader(open("relations.csv", "r"), delimiter=",")
next(relationsFile, None)  # Skip the header
locationsFile = csv.reader(open("locations.csv", "r"), delimiter=",")
next(locationsFile, None)

# load second file as lookup table
locationData = {}
for row in locationsFile:
    locationData[row[0]] = row

productCSV = "products.csv"
productFile = open(productCSV, "w")
headers = "Description, Price, Stock, Store Location\n"
productFile.write(headers)

# Random counter to track id
# print(data)
for e1 in data:
    for div in soup.find_all("div", {'class': 'featured'}):
        div.decompose()  # For dropping a div
    productID = e1.h2.a['href'].split('/')
    description = e1.h2.a.text
    cost = e1.find("div", class_='cost').text
    stock = e1.find("div", class_='inventory').text
    currency = cost[0]

    print(str(productID[-1]) + '\t \t \t' + description + '\t \t \t \t' + cost.replace('$',
                                                                                       "") + '\t \t' + stock + '\t \t' + currency)
    # productFile.write(description + "," + cost + "," + stock + "," + " \n")
