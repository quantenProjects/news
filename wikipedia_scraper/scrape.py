#!/bin/env python3

# Inspired by: https://medium.com/@Alexander_H/scraping-wikipedia-with-python-8000fc9c9e6c

import requests
from bs4 import BeautifulSoup
import time
import json

html = requests.get('https://de.wikipedia.org/wiki/Liste_deutscher_Zeitungen')

b = BeautifulSoup(html.text, 'lxml')
links = []

table = b.find("table", {"id": "tageszeitungen"})
for row in table.findAll("tr"):
    cells = row.findAll("td")
    if len(cells) == 10:
        for link in cells[1].findAll('a', href=True):
            links.append(link['href'])


paper_links = ['https://de.wikipedia.org' + i for i in links]

website_links = []



for paper in paper_links:
    html = requests.get(paper)
    #print(paper)
    b = BeautifulSoup(html.text, 'lxml')
    table = b.find("table", class_= "infobox")
    if table != None:
        for row in table.findAll("tr"):
            cells = row.findAll("td")
            if len(cells)==2:
                b =cells[0].findAll("b")[0].string
                if b == "Weblink":
                    website_links.append(cells[1].find_all('a', href=True)[0]['href'])
                    print(website_links[-1])
    time.sleep(0.5)

print(json.dumps(website_links))
