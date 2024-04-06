#Arjun Balamurai - CE20B015
#Download data to project folder
# DO NOT RUN THIS CODE
import os
import random
import requests
import pandas as pd
from bs4 import BeautifulSoup
from zipfile import ZipFile
import yaml

SCRIPTDIR = os.path.dirname(__file__).rstrip("\code")
OUTPUTDIR=SCRIPTDIR + "\data\weather.zip"
YAMLFILE = os.path.join(SCRIPTDIR, 'params\params.yml')

with open(YAMLFILE, 'r') as file:
    params = yaml.safe_load(file)
    
year = params['year']
url = f'https://www.ncei.noaa.gov/data/local-climatological-data/access/{year}/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
rows = soup.find("table").find_all("tr")[2:-2]

fileName = []

total = params.get('n_locs')
print(total)
for i in range(total):
    index = random.randint(0, len(rows))
    data = rows[index].find_all("td")
    fileName.append(data[0].text)
print("HI")
for name in fileName:
    print(name)
    newUrl = url+name
    response = requests.get(newUrl)
    open(name,'wb').write(response.content)
print("HI")
with ZipFile(OUTPUTDIR,'w') as zip:
    for file in fileName:
        zip.write(file)

