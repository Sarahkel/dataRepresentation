#Lab 3, Sarah Scholz, GMIT, Webscraping with Python

import requests
from bs4 import  BeautifulSoup
with open("./cars.html") as fp:

    soup = BeautifulSoup(fp, 'html.parser')
print("------------")
print(soup.prettify())