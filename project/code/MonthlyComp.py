#Create Monthly Computed

import pandas as pd
from zipfile import ZipFile
import os
import yaml

def process():
    SCRIPTDIR = os.path.dirname(__file__).rstrip("\code")
    OUTPUTDIR=SCRIPTDIR + "\data"
    YAMLFILE = os.path.join(SCRIPTDIR, 'params\\fileParams.yml')
    
    with open(YAMLFILE, 'r') as file:
        params = yaml.safe_load(file)
    
    data = pd.read_csv(os.path.join(OUTPUTDIR, params['file_name']))

    data['DATE'] = pd.to_datetime(data['DATE'])
    data['Month'] = data['DATE'].dt.month
    monthlyValues = data.groupby('Month')[params['field_name']].mean()
    monthlyValues.to_csv(SCRIPTDIR+'/output/monthlyComputed.csv', index=False)

process()