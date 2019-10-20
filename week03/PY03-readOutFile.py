#Lab 3, Sarah Scholz, GMIT, Webscraping with Python
#copied over from Webscraping.py to comply with structure

import requests
from bs4 import  BeautifulSoup
with open("./cars.html") as fp:

    soup = BeautifulSoup(fp, 'html.parser')
rows = soup.findAll("tr")
for row in rows: 
    #print(row)
    cols = row.findAll("td")
    dataList = []
    for col in cols: 
        dataList.append(col.text)
    print(dataList)
