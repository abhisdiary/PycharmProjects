from bs4 import BeautifulSoup

with open("masters.html", encoding='utf-8') as fd:
    html_doc = fd.read()

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.head)
# thing = soup.find_all(class_="hb-qtip")
# thing = soup.find({"div": "data-unitcode"})
# print(thing)
# print(soup.head)
# print(soup.head)
# print(soup.head)

elements = soup.find_all("div", attrs={'data-unitcode': True, 'class': 'col4'})

for e1 in elements:
    print(e1['data-unitcode'] + '\t \t' + e1.get_text())
